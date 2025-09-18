# This file will act as our simple in-memory database.
# In a real application, this data would likely come from a database.

ITEMS = [
    {"name": "Wood Log"},
    {"name": "Copper Ore"},
    {"name": "Iron Ore"},
    {"name": "Stone"},
    {"name": "Wolframite"},
    {"name": "Coal"},
    {"name": "Wood Plank"},
    {"name": "Wood Frame"},
    {"name": "Iron Ingot"},
    {"name": "Iron Plating"},
    {"name": "Iron Gear"},
    {"name": "Rotor"},
    {"name": "Copper Ingot"},
    {"name": "Copper Wire"},
    {"name": "Heat Sink"},
    {"name": "Electromagnet"},
    {"name": "Sand"},
    {"name": "Concrete"},
    {"name": "Steel"},
    {"name": "Steel Rod"},
    {"name": "Silicon"},
    {"name": "Glass"},
    {"name": "Condenser Lens"},
    {"name": "Nano Wire"},
    {"name": "Graphite"},
    {"name": "Carbon Fiber"},
    {"name": "Battery"},
    {"name": "Energy Cube"},
    {"name": "Metal Frame"},
    {"name": "Logic Circuit"},
    {"name": "Computer"},
    {"name": "Super Computer"},
    {"name": "Tungsten Ore"},
    {"name": "Tungsten Carbide"},
    {"name": "Coupler"},
    {"name": "Electric Motor"},
    {"name": "Gyroscope"},
    {"name": "Industrial Frame"},
    {"name": "Turbocharger"},
    {"name": "Stabilizer"},
    {"name": "Electron Microscope"},
    {"name": "Quantum Entangler"},
    {"name": "Magnetic Field Generator"},
    {"name": "Atomic Locator"},
    {"name": "Tank"},
    {"name": "Matter Compressor"},
    {"name": "Particle Glue"},
    {"name": "Matter Duplicator"},
    {"name": "Uranium Ore"},
    {"name": "Enriched Uranium"},
    {"name": "Empty Fuel Cell"},
    {"name": "Nuclear Fuel Cell"},
    {"name": "Earth Token"},
]
##
# name : The output item name
# outputs : The output item name and quantity
# inputs : The input items name and quantity
# craft_time : The time to create output item
# machine : The building
# is_alternative : Type bool, The Recipe is alternative or not
##
RECIPES = [
    # --- Column 1 ---
    {
        "name": "Wood Plank",
        "outputs": [({"name": "Wood Plank"}, 1)],
        "inputs": [({"name": "Wood Log"}, 1)],
        "craft_time": 4, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Iron Ingot",
        "outputs": [({"name": "Iron Ingot"}, 1)],
        "inputs": [({"name": "Iron Ore"}, 1)],
        "craft_time": 2, "machine": "Smelter", "is_alternative": False,
    },
    {
        "name": "Copper Ingot",
        "outputs": [({"name": "Copper Ingot"}, 1)],
        "inputs": [({"name": "Copper Ore"}, 1)],
        "craft_time": 2, "machine": "Smelter", "is_alternative": False,
    },
    {
        "name": "Iron Gear",
        "outputs": [({"name": "Iron Gear"}, 1)],
        "inputs": [({"name": "Iron Ingot"}, 2)],
        "craft_time": 4, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Alt: Iron Gear",
        "outputs": [({"name": "Iron Gear"}, 8)],
        "inputs": [({"name": "Steel"}, 1)],
        "craft_time": 8, "machine": "Workshop", "is_alternative": True,
    },
    {
        "name": "Copper Wire",
        "outputs": [({"name": "Copper Wire"}, 2)],
        "inputs": [({"name": "Copper Ingot"}, 3)],
        "craft_time": 4, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Alt: Copper Wire",
        "outputs": [({"name": "Copper Wire"}, 8)],
        "inputs": [({"name": "Graphite"}, 1)],
        "craft_time": 8, "machine": "Workshop", "is_alternative": True,
    }, ##TODO Change Recipes under here.
    {
        "name": "Sand",
        "outputs": [({"name": "Sand"}, 1)],
        "inputs": [({"name": "Stone"}, 2)],
        "craft_time": 5, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Glass",
        "outputs": [({"name": "Glass"}, 1)],
        "inputs": [({"name": "Sand"}, 4)],
        "craft_time": 6, "machine": "Smelter", "is_alternative": False,
    },
    {
        "name": "Alt: Glass",
        "outputs": [({"name": "Glass"}, 1)],
        "inputs": [({"name": "Stone"}, 5)],
        "craft_time": 2.5, "machine": "Smelter", "is_alternative": True,
    },

    # --- Column 2 ---
    {
        "name": "Wood Frame",
        "outputs": [({"name": "Wood Frame"}, 1)],
        "inputs": [({"name": "Wood Plank"}, 4)],
        "craft_time": 12, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Logic Circuit",
        "outputs": [({"name": "Logic Circuit"}, 1)],
        "inputs": [({"name": "Wood Plank"}, 1), ({"name": "Copper Wire"}, 6)],
        "craft_time": 8, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Computer",
        "outputs": [({"name": "Computer"}, 1)],
        "inputs": [({"name": "Logic Circuit"}, 4), ({"name": "Iron Gear"}, 4)],
        "craft_time": 6, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Iron Plating",
        "outputs": [({"name": "Iron Plating"}, 1)],
        "inputs": [({"name": "Iron Ingot"}, 1), ({"name": "Copper Ingot"}, 2)],
        "craft_time": 6, "machine": "Workshop", "is_alternative": False,
    },

    # --- Column 3 ---
    {
        "name": "Concrete",
        "outputs": [({"name": "Concrete"}, 1)],
        "inputs": [({"name": "Stone"}, 1)], # Water is not in ITEMS list, so omitted
        "craft_time": 40, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Steel",
        "outputs": [({"name": "Steel"}, 1)],
        "inputs": [({"name": "Iron Ingot"}, 1), ({"name": "Coal"}, 2)],
        "craft_time": 60, "machine": "Forge", "is_alternative": False,
    },
    {
        "name": "Steel Rod",
        "outputs": [({"name": "Steel Rod"}, 1)],
        "inputs": [({"name": "Steel"}, 8), ({"name": "Concrete"}, 4), ({"name": "Coal"}, 2)],
        "craft_time": 24, "machine": "Industrial Factory", "is_alternative": False,
    },
    {
        "name": "Alt: Steel Rod",
        "outputs": [({"name": "Steel Rod"}, 1)],
        "inputs": [({"name": "Steel"}, 2), ({"name": "Iron Gear"}, 4), ({"name": "Concrete"}, 2)],
        "craft_time": 15, "machine": "Industrial Factory", "is_alternative": True,
    },
    {
        "name": "Industrial Frame",
        "outputs": [({"name": "Industrial Frame"}, 1)],
        "inputs": [({"name": "Steel Rod"}, 2), ({"name": "Iron Gear"}, 8), ({"name": "Concrete"}, 5)],
        "craft_time": 30, "machine": "Manufacturer", "is_alternative": False,
    },
    {
        "name": "Electric Motor",
        "outputs": [({"name": "Electric Motor"}, 2)],
        "inputs": [({"name": "Steel"}, 2), ({"name": "Iron Gear"}, 24), ({"name": "Logic Circuit"}, 50)],
        "craft_time": 30, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Super Computer",
        "outputs": [({"name": "Super Computer"}, 1)],
        "inputs": [({"name": "Computer"}, 1)], # Gem is not in ITEMS list, so omitted
        "craft_time": 90, "machine": "Manufacturer", "is_alternative": False,
    },

    # --- Last Column ---
    {
        "name": "Turbocharger",
        "outputs": [({"name": "Turbocharger"}, 1)],
        "inputs": [({"name": "Electric Motor"}, 3), ({"name": "Steel Rod"}, 5)],
        "craft_time": 15, "machine": "Machine Shop", "is_alternative": False,
    }
]

BUILDING_DATA = {
    "Extractor": {
        "base_rate": 7.5, # items per minute at level 1
        "levels": {
            1: {"speed_multiplier": 1.0},
            2: {"speed_multiplier": 1.5},
            3: {"speed_multiplier": 2.0},
            4: {"speed_multiplier": 3.0},
            5: {"speed_multiplier": 4.0},
        }
    },
    "Workshop": {
        "levels": {
            1: {"speed_multiplier": 1.0},
            2: {"speed_multiplier": 1.5},
            3: {"speed_multiplier": 2.0},
            4: {"speed_multiplier": 3.0},
        }
    },
    "Smelter": {
        "levels": {
            1: {"speed_multiplier": 1.0},
            2: {"speed_multiplier": 1.5},
            3: {"speed_multiplier": 2.0},
            4: {"speed_multiplier": 3.0},
        }
    },

    "Machine Shop": {
        "levels": {
            1: {"speed_multiplier": 1.0},
            2: {"speed_multiplier": 1.5},
            3: {"speed_multiplier": 2.0},
            4: {"speed_multiplier": 3.0},
        }
    },
    "Forge": {
        "levels": {
            1: {"speed_multiplier": 1.0},
            2: {"speed_multiplier": 1.5},
            3: {"speed_multiplier": 2.0},
            4: {"speed_multiplier": 3.0},
        }
    },
    "Industrial Factory": {
        "levels": {
            1: {"speed_multiplier": 1.0},
            2: {"speed_multiplier": 1.5},
            3: {"speed_multiplier": 2.0},
            4: {"speed_multiplier": 3.0},
        }
    },
    "Manufacturer": {
        "levels": {
            1: {"speed_multiplier": 1.0},
            2: {"speed_multiplier": 1.5},
            3: {"speed_multiplier": 2.0},
            4: {"speed_multiplier": 3.0},
        }
    },
    "Earth Teleporter": {
        "levels": {
            1: {"speed_multiplier": 1.0}
        }
    },
}