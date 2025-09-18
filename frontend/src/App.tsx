import React, { useState, useEffect } from 'react';
import {
    Container, Typography, FormControl, InputLabel, Select, MenuItem, TextField, 
    Button, Box, CircularProgress, Paper, createTheme, ThemeProvider, CssBaseline,
    FormGroup, FormControlLabel, Checkbox, Grid
} from '@mui/material';

const darkTheme = createTheme({
    palette: {
        mode: 'dark',
        primary: {
            main: '#4caf50',
        },
        background: {
            default: '#121212',
            paper: '#1e1e1e',
        },
    },
});

interface InputMaterial {
    name: string;
}
type RecipeInput = [InputMaterial, number];
interface ProductionNode {
    required: number;
    recipe_name?: string;
    machine?: string;
    machine_count?: number;
    level?: number;
    inputs?: { [itemName: string]: ProductionNode };
    is_raw?: boolean;
    extractor_machine?: string;
    extractor_count?: number;
}

interface Recipe {
    name: string;
    inputs: RecipeInput[];
    outputs: [InputMaterial, number][]; // outputs도 동일한 구조일 것으로 예상하여 추가
    craft_time: number;
    machine: string;
    is_alternative: boolean;
}
interface BuildingData { [key: string]: { levels: { [key: number]: any } } }

function App() {
    const [items, setItems] = useState<string[]>([]);
    const [allRecipes, setAllRecipes] = useState<Recipe[]>([]);
    const [buildingData, setBuildingData] = useState<BuildingData>({});
    const [selectedItem, setSelectedItem] = useState('');
    const [quantity, setQuantity] = useState('60');
    const [selectedAlts, setSelectedAlts] = useState<{ [key: string]: boolean }>({});
    const [buildingLevels, setBuildingLevels] = useState<{ [key: string]: number }>({});
    const [result, setResult] = useState<ProductionNode | null>(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        Promise.all([
            fetch('http://127.0.0.1:8000/items').then(res => res.json()),
            fetch('http://127.0.0.1:8000/recipes').then(res => res.json()),
            fetch('http://127.0.0.1:8000/buildings').then(res => res.json()),
        ]).then(([itemData, recipeData, buildingData]) => {
            setItems(itemData);
            if (itemData.length > 0) setSelectedItem(itemData[0]);
            setAllRecipes(recipeData);
            setBuildingData(buildingData);
            // Initialize building levels to 1
            const initialLevels: { [key: string]: number } = {};
            Object.keys(buildingData).forEach(b => initialLevels[b] = 1);
            setBuildingLevels(initialLevels);
        }).catch(error => console.error('Error fetching data:', error));
    }, []);

    const handleAltChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSelectedAlts({ ...selectedAlts, [event.target.name]: event.target.checked });
    };

    const handleLevelChange = (machine: string, level: number) => {
        setBuildingLevels({ ...buildingLevels, [machine]: level });
    };

    const handleCalculate = () => {
        if (!selectedItem || !quantity) return;
        setLoading(true);
        setResult(null);

        const activeAlts = Object.entries(selectedAlts).filter(([, v]) => v).map(([k]) => k);
        
        const requestBody = {
            item_name: selectedItem,
            quantity: parseFloat(quantity),
            active_alts: activeAlts,
            building_levels: buildingLevels,
        };

        fetch('http://127.0.0.1:8000/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(requestBody),
        })
            .then(response => response.json())
            .then(data => setResult(data))
            .catch(error => console.error('Error calculating:', error))
            .finally(() => setLoading(false));
    };

    const renderTree = (node: ProductionNode, itemName: string) => (
        <Paper key={itemName} variant="outlined" sx={{ p: 2, my: 1, bgcolor: 'background.paper' }}>
            <Typography variant="h6">{itemName}: {node.required.toFixed(2)}/min</Typography>
            {node.is_raw && (
                <Typography variant="body2" color="text.secondary">
                    Requires {node.extractor_count?.toFixed(2)} Level {node.level} {node.extractor_machine}(s)
                </Typography>
            )}
            {node.machine && (
                <Typography variant="body2" color="text.secondary">
                    Recipe: {node.recipe_name} | Requires {node.machine_count?.toFixed(2)} Level {node.level} {node.machine}(s)
                </Typography>
            )}
            {node.inputs && Object.keys(node.inputs).length > 0 && (
                <Box sx={{ pl: 2, borderLeft: '1px solid #444' }}>
                    {Object.entries(node.inputs).map(([childName, childNode]) => renderTree(childNode, childName))}
                </Box>
            )}
        </Paper>
    );

    return (
        <ThemeProvider theme={darkTheme}>
            <CssBaseline />
            <Container maxWidth="lg" sx={{ my: 4 }}>
                <Typography variant="h4" component="h1" gutterBottom>Builderment Calculator</Typography>
                <Paper sx={{ p: 2, mb: 2 }}>
                    <Typography variant="h6" gutterBottom>Options</Typography>
                    <Grid container spacing={2}>
                        <Grid xs={12} md={6}>
                            <FormControl fullWidth>
                                <InputLabel>Item</InputLabel>
                                <Select value={selectedItem} label="Item" onChange={e => setSelectedItem(e.target.value)}>
                                    {items.map(item => <MenuItem key={item} value={item}>{item}</MenuItem>)}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid xs={12} md={4}>
                            <TextField fullWidth label="Quantity/min" type="number" value={quantity} onChange={e => setQuantity(e.target.value)} />
                        </Grid>
                        <Grid xs={12} md={2}>
                            <Button fullWidth variant="contained" onClick={handleCalculate} disabled={loading} sx={{ height: '100%' }}>Calculate</Button>
                        </Grid>
                    </Grid>
                </Paper>

                {Object.keys(buildingData).length > 0 &&
                    <Paper sx={{ p: 2, mb: 2 }}>
                        <Typography variant="h6" gutterBottom>Building Levels</Typography>
                        <Grid container spacing={2}>
                            {Object.entries(buildingData).map(([name, data]) => (
                                <Grid xs={6} md={3} key={name}>
                                    <FormControl fullWidth>
                                        <InputLabel>{name}</InputLabel>
                                        <Select
                                            value={buildingLevels[name] || 1}
                                            label={name}
                                            onChange={e => handleLevelChange(name, e.target.value as number)}
                                        >
                                            {data.levels && Object.keys(data.levels).map(level => <MenuItem key={level} value={level}>{`Level ${level}`}</MenuItem>)}
                                        </Select>
                                    </FormControl>
                                </Grid>
                            ))}
                        </Grid>
                    </Paper>
                }

                <Paper sx={{ p: 2, mb: 2 }}>
                    {/* 1. 제목을 한국어로 변경했습니다. */}
                    <Typography variant="h6" gutterBottom>Alternative Recipe</Typography>
                    <FormGroup sx={{ display: 'flex', flexDirection: 'row', flexWrap: 'wrap' }}>
                        {Array.isArray(allRecipes) &&
                            allRecipes
                                .filter(r => r.is_alternative)
                                .map(recipe => {
                                    // 2. 재료 이름을 추출하여 라벨을 동적으로 생성합니다.
                                    const materialNames = recipe.inputs.map(input => input[0].name);
                                    const materialsString = materialNames.join(', ');
                                    const displayLabel = `${recipe.name} (${materialsString})`;

                                    return (
                                        <FormControlLabel
                                            key={recipe.name}
                                            label={displayLabel} // 생성된 라벨을 여기에 적용
                                            control={
                                                <Checkbox
                                                    checked={selectedAlts[recipe.name] || false}
                                                    onChange={handleAltChange}
                                                    name={recipe.name}
                                                />
                                            }
                                        />
                                    );
                                })}
                    </FormGroup>
                </Paper>

                {loading ? <CircularProgress /> : result &&
                    <Paper sx={{ p: 2, mt: 2 }}>
                        <Typography variant="h6" gutterBottom>Production Requirements</Typography>
                        {Object.entries(result).map(([itemName, node]) => renderTree(node, itemName))}
                    </Paper>
                }
            </Container>
        </ThemeProvider>
    );
}

export default App;