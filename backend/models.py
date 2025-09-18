from pydantic import BaseModel
from typing import List, Optional, Tuple

class Item(BaseModel):
    name: str
    image_url: Optional[str] = None

class Recipe(BaseModel):
    name: str
    # The first element of the tuple is the item, the second is the quantity
    outputs: List[Tuple[Item, int]]
    inputs: List[Tuple[Item, int]]
    machine: str
    craft_time: float # Crafting time in seconds
    is_alternative: bool = False
