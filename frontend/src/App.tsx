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

interface AggregatedRawMaterial {
    quantity: number;
    extractorCount?: number;
    extractorMachine?: string;
    level?: number;
}

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
    const [totalRequiredItems, setTotalRequiredItems] = useState<{ [key: string]: AggregatedRawMaterial }>({});

    const aggregateRawMaterials = (productionResult: { [key: string]: ProductionNode } | null) => {
        const totals: { [key: string]: AggregatedRawMaterial } = {};

        if (!productionResult) {
            return totals;
        }

        const traverse = (node: ProductionNode, currentItemName: string) => {
            if (node.is_raw) {
                if (!totals[currentItemName]) {
                    totals[currentItemName] = { quantity: 0, extractorCount: 0 };
                }
                totals[currentItemName].quantity += node.required;
                if (node.extractor_count) {
                    totals[currentItemName].extractorCount = (totals[currentItemName].extractorCount || 0) + node.extractor_count;
                }
                if (node.extractor_machine) {
                    totals[currentItemName].extractorMachine = node.extractor_machine;
                }
                if (node.level) {
                    totals[currentItemName].level = node.level;
                }
            }
            if (node.inputs) {
                Object.entries(node.inputs).forEach(([inputItemName, inputNode]) => {
                    traverse(inputNode, inputItemName);
                });
            }
        };

        Object.entries(productionResult).forEach(([itemName, node]) => {
            traverse(node, itemName);
        });

        return totals;
    };

    // New state for Max Output from Extractors feature
    const [maxOutputItem, setMaxOutputItem] = useState<string>('');
    const [numExtractors, setNumExtractors] = useState<string>('1');
    const [maxOutputExtractorLevel, setMaxOutputExtractorLevel] = useState<number>(1);
    const [maxOutputResult, setMaxOutputResult] = useState<number | null>(null);
    const [maxOutputLoading, setMaxOutputLoading] = useState<boolean>(false);
    const [maxOutputError, setMaxOutputError] = useState<string>('');

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

            // Initialize maxOutputItem to the first raw material if available
            const rawMaterials = itemData.filter((item: string) => !recipeData.some((r: Recipe) => r.outputs[0][0].name === item));
            if (rawMaterials.length > 0) {
                setMaxOutputItem(rawMaterials[0]);
            }
        }).catch(error => console.error('Error fetching data:', error));
    }, []);

    const handleAltChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSelectedAlts({ ...selectedAlts, [event.target.name]: event.target.checked });
    };

    const handleLevelChange = (machine: string, level: number) => {
        setBuildingLevels({ ...buildingLevels, [machine]: level });
    };

    const handleSetAllToMaxLevel = () => {
        const newBuildingLevels: { [key: string]: number } = {};
        Object.entries(buildingData).forEach(([name, data]) => {
            if (data.levels) {
                const maxLevel = Math.max(...Object.keys(data.levels).map(Number));
                newBuildingLevels[name] = maxLevel;
            }
        });
        setBuildingLevels(newBuildingLevels);
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
            .then(data => {
                setResult(data);
                setTotalRequiredItems(aggregateRawMaterials(data));
            })
            .catch(error => console.error('Error calculating:', error))
            .finally(() => setLoading(false));
    };

    const handleMaxOutputCalculate = () => {
        if (!maxOutputItem || !numExtractors || !!maxOutputError) return;
        setMaxOutputLoading(true);
        setMaxOutputResult(null);

        const url = `http://127.0.0.1:8000/max_output_from_extractors?item_name=${maxOutputItem}&num_extractors=${numExtractors}&extractor_level=${maxOutputExtractorLevel}`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    return response.json().then(err => Promise.reject(err));
                }
                return response.json();
            })
            .then(data => {
                setMaxOutputResult(data.max_output);
            })
            .catch(error => {
                console.error('Error calculating max output:', error);
                setMaxOutputError(error.detail || 'An unknown error occurred.');
            })
            .finally(() => setMaxOutputLoading(false));
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
                    <Typography variant="h6" gutterBottom sx={{ mb: 2 }}>Options</Typography>
                    <Grid container spacing={1}>
                        <Grid item xs={12} md={6}>
                            <FormControl fullWidth>
                                <InputLabel>Item</InputLabel>
                                <Select value={selectedItem} label="Item" onChange={e => setSelectedItem(e.target.value)}>
                                    {items.map(item => <MenuItem key={item} value={item}>{item}</MenuItem>)}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item xs={12} md={4}>
                            <TextField fullWidth label="Quantity/min" type="number" value={quantity} onChange={e => setQuantity(e.target.value)} />
                        </Grid>
                        <Grid item xs={12} md={2}>
                            <Button fullWidth variant="contained" onClick={handleCalculate} disabled={loading} sx={{ height: '100%' }}>Calculate</Button>
                        </Grid>
                    </Grid>
                </Paper>

                {Object.keys(buildingData).length > 0 &&
                    <Paper sx={{ p: 2, mb: 2 }}>
                        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                            <Typography variant="h6" component="h2" gutterBottom sx={{ mb: 0 }}>Building Levels</Typography>
                            <Button
                                variant="contained"
                                onClick={handleSetAllToMaxLevel}
                                size="small"
                            >
                                Set All to Max Level
                            </Button>
                        </Box>
                        <Grid container spacing={1}>
                            {Object.entries(buildingData).map(([name, data]) => (
                                <Grid item xs={6} md={3} key={name}>
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
{/*
                <Paper sx={{ p: 2, mb: 2 }}>
                    <Typography variant="h6" gutterBottom sx={{ mb: 2 }}>Max Output from Extractors</Typography>
                    <Grid container spacing={1}>
                        <Grid item xs={12} md={6}>
                            <FormControl fullWidth>
                                <InputLabel>Raw Material</InputLabel>
                                <Select value={maxOutputItem} label="Raw Material" onChange={e => setMaxOutputItem(e.target.value)}>
                                    {items.filter(item => !allRecipes.some(r => r.outputs[0][0].name === item)).map(item => <MenuItem key={item} value={item}>{item}</MenuItem>)}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item xs={12} md={3}>
                            <TextField
                                fullWidth
                                label="Number of Extractors"
                                type="number"
                                value={numExtractors}
                                onChange={e => {
                                    setNumExtractors(e.target.value);
                                    if (isNaN(parseFloat(e.target.value)) && e.target.value !== '') {
                                        setMaxOutputError('Please enter a valid number.');
                                    } else {
                                        setMaxOutputError('');
                                    }
                                }}
                                error={!!maxOutputError}
                                helperText={maxOutputError}
                            />
                        </Grid>
                        <Grid item xs={12} md={3}>
                            <FormControl fullWidth>
                                <InputLabel>Extractor Level</InputLabel>
                                <Select
                                    value={maxOutputExtractorLevel}
                                    label="Extractor Level"
                                    onChange={e => setMaxOutputExtractorLevel(e.target.value as number)}
                                >
                                    {buildingData.Extractor && Object.keys(buildingData.Extractor.levels).map(level => <MenuItem key={level} value={level}>{`Level ${level}`}</MenuItem>)}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item xs={12}>
                            <Button
                                fullWidth
                                variant="contained"
                                onClick={handleMaxOutputCalculate}
                                disabled={maxOutputLoading || !!maxOutputError || !maxOutputItem || !numExtractors}
                                sx={{ height: '100%' }}
                            >
                                Calculate Max Output
                            </Button>
                        </Grid>
                    </Grid>
                    {maxOutputLoading && <CircularProgress sx={{ mt: 2 }} />}
                    {maxOutputResult && !maxOutputLoading && (
                        <Typography variant="h6" sx={{ mt: 2 }}>
                            Max Output: {maxOutputResult.toFixed(2)}/min
                        </Typography>
                    )}
                </Paper>
*/}
                <Paper sx={{ p: 2, mb: 2 }}>
                    <Typography variant="h6" gutterBottom sx={{ mb: 2 }}>Alternative Recipes</Typography>
                    <FormGroup sx={{ display: 'flex', flexDirection: 'column' }}>
                        {Array.isArray(allRecipes) &&
                            allRecipes
                                .filter(r => r.is_alternative)
                                .map(recipe => {
                                    const materialNames = recipe.inputs.map(input => input[0].name);
                                    const materialsString = materialNames.join(', ');
                                    const displayLabel = `${recipe.name} (${materialsString})`;

                                    return (
                                        <FormControlLabel
                                            key={recipe.name}
                                            label={displayLabel}
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

                {Object.keys(totalRequiredItems).length > 0 && (
                    <Paper sx={{ p: 2, mt: 2 }}>
                        <Typography variant="h6" gutterBottom>Total Raw Materials Required</Typography>
                        {Object.entries(totalRequiredItems).map(([itemName, data]) => (
                            <Typography key={itemName} variant="body1">
                                {itemName}: {data.quantity.toFixed(2)}/min
                                {data.extractorCount !== undefined && data.extractorMachine && data.level !== undefined &&
                                    ` | ( Requires ${data.extractorCount.toFixed(2)} Level ${data.level.toFixed(0)} ${data.extractorMachine}(s))`
                                }
                            </Typography>
                        ))}
                    </Paper>
                )}

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