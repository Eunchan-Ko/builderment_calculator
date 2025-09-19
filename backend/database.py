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
    # --- machine : Workshop ---
    {
        "name": "Wood Plank",
        "outputs": [({"name": "Wood Plank"}, 1)],
        "inputs": [({"name": "Wood Log"}, 1)],
        "craft_time": 4, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Wood Frame",
        "outputs": [({"name": "Wood Frame"}, 1)],
        "inputs": [({"name": "Wood Plank"}, 4)],
        "craft_time": 8, "machine": "Workshop", "is_alternative": False,
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
        "inputs": [({"name": "Carbon Fiber"}, 1)],
        "craft_time": 8, "machine": "Workshop", "is_alternative": True,
    },
    {
        "name": "Heat Sink",
        "outputs": [({"name": "Heat Sink"}, 1)],
        "inputs": [({"name": "Copper Ingot"}, 5)],
        "craft_time": 6, "machine": "Workshop", "is_alternative": False,
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
        "name": "Iron Plating",
        "outputs": [({"name": "Iron Plating"}, 2)],
        "inputs": [({"name": "Iron Ingot"}, 4)],
        "craft_time": 6, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Steel Rod",
        "outputs": [({"name": "Steel Rod"}, 1)],
        "inputs": [({"name": "Steel"}, 3)],
        "craft_time": 4, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Sand",
        "outputs": [({"name": "Sand"}, 1)],
        "inputs": [({"name": "Stone"}, 1)],
        "craft_time": 1.5, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Condenser Lens",
        "outputs": [({"name": "Condenser Lens"}, 1)],
        "inputs": [({"name": "Glass"}, 3)],
        "craft_time": 3, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Carbon Fiber",
        "outputs": [({"name": "Carbon Fiber"}, 1)],
        "inputs": [({"name": "Graphite"}, 4)],
        "craft_time": 8, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Coupler",
        "outputs": [({"name": "Coupler"}, 1)],
        "inputs": [({"name": "Tungsten Carbide"}, 1)],
        "craft_time": 10, "machine": "Workshop", "is_alternative": False,
    },
    {
        "name": "Particle Glue",
        "outputs": [({"name": "Particle Glue"}, 10)],
        "inputs": [({"name": "Matter Compressor"}, 1)],
        "craft_time": 30, "machine": "Workshop", "is_alternative": False,
    },

    # machine : smelter

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
        "name": "Silicon",
        "outputs": [({"name": "Silicon"}, 1)],
        "inputs": [({"name": "Sand"}, 2)],
        "craft_time": 3, "machine": "Smelter", "is_alternative": False,
    },
    {
        "name": "Glass",
        "outputs": [({"name": "Glass"}, 1)],
        "inputs": [({"name": "Sand"}, 4)],
        "craft_time": 6, "machine": "Smelter", "is_alternative": False,
    },
    {
        "name": "Tungsten Ore",
        "outputs": [({"name": "Tungsten Ore"}, 1)],
        "inputs": [({"name": "Wolframite"}, 5)],
        "craft_time": 2.5, "machine": "Smelter", "is_alternative": False,
    },
    {
        "name": "Enriched Uranium",
        "outputs": [({"name": "Enriched Uranium"}, 1)],
        "inputs": [({"name": "Uranium Ore"}, 30)],
        "craft_time": 60, "machine": "Smelter", "is_alternative": False,
    },

    # machine : Machine shop
    {
        "name": "Electromagnet",
        "outputs": [({"name": "Electromagnet"}, 1)],
        "inputs": [({"name": "Iron Ingot"}, 2),
                   ({"name": "Copper Wire"}, 6)],
        "craft_time": 8, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Alt: Electromagnet",
        "outputs": [({"name": "Electromagnet"}, 12)],
        "inputs": [({"name": "Nano Wire"}, 1),
                   ({"name": "Steel Rod"}, 1)],
        "craft_time": 20, "machine": "Machine Shop", "is_alternative": True,
    },
    {
        "name": "Logic Circuit",
        "outputs": [({"name": "Logic Circuit"}, 1)],
        "inputs": [({"name": "Silicon"}, 2),
                   ({"name": "Copper Wire"}, 3)],
        "craft_time": 6, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Alt: Logic Circuit",
        "outputs": [({"name": "Logic Circuit"}, 1)],
        "inputs": [({"name": "Iron Plating"}, 1),
                   ({"name": "Heat Sink"}, 1)],
        "craft_time": 8, "machine": "Machine Shop", "is_alternative": True,
    },
    {
        "name": "Metal Frame",
        "outputs": [({"name": "Metal Frame"}, 1)],
        "inputs": [({"name": "Wood Frame"}, 1),
                   ({"name": "Iron Plating"}, 4)],
        "craft_time": 12, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Battery",
        "outputs": [({"name": "Battery"}, 1)],
        "inputs": [({"name": "Electromagnet"}, 8),
                   ({"name": "Graphite"}, 8)],
        "craft_time": 24, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Rotor",
        "outputs": [({"name": "Rotor"}, 1)],
        "inputs": [({"name": "Steel Rod"}, 1),
                   ({"name": "Iron Plating"}, 2)],
        "craft_time": 6, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Alt: Rotor",
        "outputs": [({"name": "Rotor"}, 1)],
        "inputs": [({"name": "Copper Ingot"}, 18),
                   ({"name": "Iron Plating"}, 18)],
        "craft_time": 18, "machine": "Machine Shop", "is_alternative": True,
    },
    {
        "name": "Nano Wire",
        "outputs": [({"name": "Nano Wire"}, 1)],
        "inputs": [({"name": "Carbon Fiber"}, 2),
                   ({"name": "Glass"}, 4)],
        "craft_time": 12, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Gyroscope",
        "outputs": [({"name": "Gyroscope"}, 1)],
        "inputs": [({"name": "Copper Wire"}, 12),
                   ({"name": "Rotor"}, 2)],
        "craft_time": 12, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Energy Cube",
        "outputs": [({"name": "Energy Cube"}, 1)],
        "inputs": [({"name": "Battery"}, 8),
                   ({"name": "Industrial Frame"}, 8)],
        "craft_time": 24, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Quantum Entangler",
        "outputs": [({"name": "Quantum Entangler"}, 1)],
        "inputs": [({"name": "Magnetic Field Generator"}, 1),
                   ({"name": "Stabilizer"}, 2)],
        "craft_time": 60, "machine": "Machine Shop", "is_alternative": False,
    },
    {
        "name": "Empty Fuel Cell",
        "outputs": [({"name": "Empty Fuel Cell"}, 1)],
        "inputs": [({"name": "Tungsten Carbide"}, 3),
                   ({"name": "Glass"}, 5)],
        "craft_time": 15, "machine": "Machine Shop", "is_alternative": False,
    },

    # machine : Forge

    {
        "name": "Concrete",
        "outputs": [({"name": "Concrete"}, 1)],
        "inputs": [({"name": "Sand"}, 10),
                   ({"name": "Steel Rod"}, 1)],
        "craft_time": 8,
        "machine": "Forge",
        "is_alternative": False,
    },
    {
        "name": "Alt: Concrete",
        "outputs": [({"name": "Concrete"}, 1)],
        "inputs": [({"name": "Stone"}, 20),
                   ({"name": "Wood Frame"}, 4)],
        "craft_time": 12,
        "machine": "Forge",
        "is_alternative": True,
    },
    {
        "name": "Graphite",
        "outputs": [({"name": "Graphite"}, 1)],
        "inputs": [({"name": "Wood Log"}, 3),
                   ({"name": "Coal"}, 3)],
        "craft_time": 4,
        "machine": "Forge",
        "is_alternative": False,
    },
    {
        "name": "Steel",
        "outputs": [({"name": "Steel"}, 1)],
        "inputs": [({"name": "Iron Ore"}, 6),
                   ({"name": "Graphite"}, 1)],
        "craft_time": 8,
        "machine": "Forge",
        "is_alternative": False,
    },
    {
        "name": "Alt: Steel",
        "outputs": [({"name": "Steel"}, 1)],
        "inputs": [({"name": "Iron Ore"}, 4),
                   ({"name": "Coal"}, 4)],
        "craft_time": 6,
        "machine": "Forge",
        "is_alternative": True,
    },
    {
        "name": "Tungsten Carbide",
        "outputs": [({"name": "Tungsten Carbide"}, 1)],
        "inputs": [({"name": "Graphite"}, 1),
                   ({"name": "Tungsten Ore"}, 2)],
        "craft_time": 5,
        "machine": "Forge",
        "is_alternative": False,
    },
    {
        "name": "Alt: Tungsten Carbide",
        "outputs": [({"name": "Tungsten Carbide"}, 2)],
        "inputs": [({"name": "Steel"}, 1),
                   ({"name": "Tungsten Ore"}, 1)],
        "craft_time": 15,
        "machine": "Forge",
        "is_alternative": True,
    },

    # machine : Industrial Factory

    {
        "name": "Computer",
        "outputs": [({"name": "Computer"}, 1)],
        "inputs": [({"name": "Heat Sink"}, 3),
                   ({"name": "Metal Frame"}, 1),
                   ({"name": "Logic Circuit"}, 3)],
        "craft_time": 8,
        "machine": "Industrial Factory",
        "is_alternative": False,
    },
    {
        "name": "Electric Motor",
        "outputs": [({"name": "Electric Motor"}, 1)],
        "inputs": [({"name": "Iron Gear"}, 4),
                   ({"name": "Rotor"}, 2),
                   ({"name": "Battery"}, 1)],
        "craft_time": 20,
        "machine": "Industrial Factory",
        "is_alternative": False,
    },
    {
        "name": "Alt: Electric Motor",
        "outputs": [({"name": "Electric Motor"}, 1)],
        "inputs": [({"name": "Electromagnet"}, 6),
                   ({"name": "Steel"}, 6),
                   ({"name": "Empty Fuel Cell"}, 1)],
        "craft_time": 22,
        "machine": "Industrial Factory",
        "is_alternative": True,
    },
    {
        "name": "Industrial Frame",
        "outputs": [({"name": "Industrial Frame"}, 1)],
        "inputs": [({"name": "Concrete"}, 6),
                   ({"name": "Metal Frame"}, 2),
                   ({"name": "Tungsten Carbide"}, 8)],
        "craft_time": 20,
        "machine": "Industrial Factory",
        "is_alternative": False,
    },
    {
        "name": "Alt: Industrial Frame",
        "outputs": [({"name": "Industrial Frame"}, 1)],
        "inputs": [({"name": "Steel"}, 18),
                   ({"name": "Iron Plating"}, 10),
                   ({"name": "Carbon Fiber"}, 4)],
        "craft_time": 36,
        "machine": "Industrial Factory",
        "is_alternative": True,
    },
    {
        "name": "Stabilizer",
        "outputs": [({"name": "Stabilizer"}, 1)],
        "inputs": [({"name": "Computer"}, 1),
                   ({"name": "Electric Motor"}, 1),
                   ({"name": "Gyroscope"}, 2)],
        "craft_time": 24,
        "machine": "Industrial Factory",
        "is_alternative": False,
    },
    {
        "name": "Tank",
        "outputs": [({"name": "Tank"}, 1)],
        "inputs": [({"name": "Concrete"}, 4),
                   ({"name": "Glass"}, 2),
                   ({"name": "Tungsten Carbide"}, 4)],
        "craft_time": 10,
        "machine": "Industrial Factory",
        "is_alternative": False,
    },
    {
        "name": "Nuclear Fuel Cell",
        "outputs": [({"name": "Nuclear Fuel Cell"}, 1)],
        "inputs": [({"name": "Enriched Uranium"}, 1),
                   ({"name": "Steel Rod"}, 1),
                   ({"name": "Empty Fuel Cell"}, 1)],
        "craft_time": 30,
        "machine": "Industrial Factory",
        "is_alternative": False,
    },

    # machine : Manufacturer

    {
        "name": "Turbocharger",
        "outputs": [({"name": "Turbocharger"}, 1)],
        "inputs": [({"name": "Iron Gear"}, 8),
                   ({"name": "Coupler"}, 4),
                   ({"name": "Logic Circuit"}, 4),
                   ({"name": "Nano Wire"}, 2)],
        "craft_time": 15,
        "machine": "Manufacturer",
        "is_alternative": False,
    },
    {
        "name": "Alt: Turbocharger",
        "outputs": [({"name": "Turbocharger"}, 1)],
        "inputs": [({"name": "Heat Sink"}, 4),
                   ({"name": "Computer"}, 1),
                   ({"name": "Gyroscope"}, 1),
                   ({"name": "Tungsten Carbide"}, 1)],
        "craft_time": 10,
        "machine": "Manufacturer",
        "is_alternative": True,
    },
    {
        "name": "Atomic Locator",
        "outputs": [({"name": "Atomic Locator"}, 1)],
        "inputs": [({"name": "Concrete"}, 24),
                   ({"name": "Copper Wire"}, 50),
                   ({"name": "Electron Microscope"}, 2),
                   ({"name": "Super Computer"}, 2)],
        "craft_time": 30,
        "machine": "Manufacturer",
        "is_alternative": False,
    },
    {
        "name": "Electron Microscope",
        "outputs": [({"name": "Electron Microscope"}, 1)],
        "inputs": [({"name": "Condenser Lens"}, 4),
                   ({"name": "Electromagnet"}, 8),
                   ({"name": "Metal Frame"}, 2),
                   ({"name": "Nano Wire"}, 2)],
        "craft_time": 24,
        "machine": "Manufacturer",
        "is_alternative": False,
    },
    {
        "name": "Magnetic Field Generator",
        "outputs": [({"name": "Magnetic Field Generator"}, 1)],
        "inputs": [({"name": "Electromagnet"}, 10),
                   ({"name": "Industrial Frame"}, 1),
                   ({"name": "Nano Wire"}, 10),
                   ({"name": "Stabilizer"}, 1)],
        "craft_time": 40,
        "machine": "Manufacturer",
        "is_alternative": False,
    },
    {
        "name": "Matter Compressor",
        "outputs": [({"name": "Matter Compressor"}, 1)],
        "inputs": [({"name": "Electric Motor"}, 2),
                   ({"name": "Industrial Frame"}, 1),
                   ({"name": "Tank"}, 1),
                   ({"name": "Turbocharger"}, 2)],
        "craft_time": 30,
        "machine": "Manufacturer",
        "is_alternative": False,
    },
    {
        "name": "Super Computer",
        "outputs": [({"name": "Super Computer"}, 1)],
        "inputs": [({"name": "Computer"}, 2),
                   ({"name": "Coupler"}, 8),
                   ({"name": "Heat Sink"}, 8),
                   ({"name": "Turbocharger"}, 1)],
        "craft_time": 30,
        "machine": "Manufacturer",
        "is_alternative": False,
    },
    {
        "name": "Alt: Super Computer",
        "outputs": [({"name": "Super Computer"}, 2)],
        "inputs": [({"name": "Computer"}, 2),
                   ({"name": "Silicon"}, 40),
                   ({"name": "Gyroscope"}, 2),
                   ({"name": "Industrial Frame"}, 1)],
        "craft_time": 30,
        "machine": "Manufacturer",
        "is_alternative": True,
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
    }
}