from typing import Dict, List, Optional
import json

from .models import Item, Recipe
from .database import ITEMS, RECIPES, BUILDING_DATA

# A dictionary to hold all items, keyed by name for quick lookups.
ALL_ITEMS: Dict[str, Item] = {item_data["name"]: Item(**item_data) for item_data in ITEMS}

# A dictionary mapping an item name to a LIST of recipes that can produce it.
ALL_RECIPES: Dict[str, List[Recipe]] = {}
for recipe_data in RECIPES:
    recipe_craft_time = recipe_data.get("craft_time", 1)

    parsed_inputs = []
    for item_info, quantity in recipe_data["inputs"]:
        item_name = item_info["name"]
        if item_name in ALL_ITEMS:
            parsed_inputs.append((ALL_ITEMS[item_name], quantity))

    parsed_outputs = []
    for item_info, quantity in recipe_data["outputs"]:
        item_name = item_info["name"]
        if item_name in ALL_ITEMS:
            parsed_outputs.append((ALL_ITEMS[item_name], quantity))

    if parsed_outputs:
        recipe = Recipe(
            name=recipe_data["name"],
            inputs=parsed_inputs,
            outputs=parsed_outputs,
            machine=recipe_data["machine"],
            is_alternative=recipe_data["is_alternative"],
            craft_time=recipe_craft_time
        )
        output_item_name = recipe.outputs[0][0].name
        if output_item_name not in ALL_RECIPES:
            ALL_RECIPES[output_item_name] = []
        ALL_RECIPES[output_item_name].append(recipe)


def is_raw_material(item_name: str) -> bool:
    """Checks if an item is a raw material (i.e., has no recipes to produce it)."""
    return item_name not in ALL_RECIPES

def calculate_max_raw_output(item_name: str, num_extractors: int, extractor_level: int) -> float:
    """
    Calculates the maximum output of a raw material given a number of extractors and their level.
    """
    if num_extractors > 500 :
        raise ValueError("Number of extractors cannot exceed 500.")

    if not is_raw_material(item_name):
        raise ValueError(f"{item_name} is not a raw material and cannot be extracted.")

    if 'Extractor' not in BUILDING_DATA:
        raise ValueError("Extractor building data not found.")

    extractor_levels_data = BUILDING_DATA['Extractor']['levels']
    if extractor_level not in extractor_levels_data:
        raise ValueError(f"Invalid Extractor level: {extractor_level}. Available levels: {list(extractor_levels_data.keys())}")

    speed_multiplier = extractor_levels_data[extractor_level]['speed_multiplier']
    base_rate = BUILDING_DATA['Extractor']['base_rate']

    total_output = num_extractors * base_rate * speed_multiplier
    return total_output

def _resolve_dependencies(
    item_name: str,
    quantity_per_minute: float,
    production_tree: Dict,
    active_alts: List[str],
    building_levels: Dict[str, int],
):
    """Helper function to recursively resolve dependencies."""

    recipe_to_use: Optional[Recipe] = None
    possible_recipes = ALL_RECIPES.get(item_name, [])
    for r in possible_recipes:
        if r.is_alternative and r.name in active_alts:
            recipe_to_use = r
            break
    if not recipe_to_use:
        for r in possible_recipes:
            if not r.is_alternative:
                recipe_to_use = r
                break

    if not recipe_to_use:
        level = building_levels.get('Extractor', 1)
        speed_multiplier = BUILDING_DATA['Extractor']['levels'][level]['speed_multiplier']
        base_rate = BUILDING_DATA['Extractor']['base_rate']
        extractor_rate = base_rate * speed_multiplier
        num_extractors = quantity_per_minute / extractor_rate

        if item_name in production_tree:
            production_tree[item_name]['required'] += quantity_per_minute
            production_tree[item_name]['extractor_count'] += num_extractors
        else:
            production_tree[item_name] = {
                'required': quantity_per_minute,
                'is_raw': True,
                'extractor_machine': 'Extractor',
                'extractor_count': num_extractors,
                'level': level,
            }
        return

    machine_name = recipe_to_use.machine
    level = building_levels.get(machine_name, 1)
    speed_multiplier = BUILDING_DATA[machine_name]['levels'][level]['speed_multiplier']
    
    output_per_run = recipe_to_use.outputs[0][1]
    items_per_minute_per_machine = (60 / recipe_to_use.craft_time) * output_per_run * speed_multiplier
    machine_count = quantity_per_minute / items_per_minute_per_machine

    if item_name in production_tree:
        production_tree[item_name]['required'] += quantity_per_minute
        production_tree[item_name]['machine_count'] += machine_count
    else:
        production_tree[item_name] = {
            'required': quantity_per_minute,
            'recipe_name': recipe_to_use.name,
            'machine': machine_name,
            'machine_count': machine_count,
            'level': level,
            'inputs': {},
        }

    for input_item, input_quantity_per_run in recipe_to_use.inputs:
        runs_per_minute = quantity_per_minute / output_per_run
        total_input_required = input_quantity_per_run * runs_per_minute
        _resolve_dependencies(
            input_item.name,
            total_input_required,
            production_tree[item_name]['inputs'],
            active_alts,
            building_levels,
        )

def calculate_requirements(
    target_item_name: str, 
    quantity_per_minute: float, 
    active_alts: List[str] = [],
    building_levels: Dict[str, int] = {}
) -> Dict:
    """
    Calculates the required resources and machines for a given target item and quantity,
    considering selected alternative recipes and building levels.
    """
    production_tree = {}
    _resolve_dependencies(target_item_name, quantity_per_minute, production_tree, active_alts, building_levels)
    
    # Debugging: Print the final tree to the console
    print(json.dumps(production_tree, indent=2))
    
    return production_tree