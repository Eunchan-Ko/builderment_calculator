from typing import List, Optional, Dict
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from backend.calculator import calculate_requirements, ALL_ITEMS, ALL_RECIPES, BUILDING_DATA, calculate_max_raw_output
from backend.models import Recipe

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    item_name: str
    quantity: float
    active_alts: Optional[List[str]] = []
    building_levels: Optional[Dict[str, int]] = {}

@app.get("/")
def read_root():
    return {"message": "Builderment Calculator API is running."}

@app.get("/items")
def get_items() -> List[str]:
    return list(ALL_ITEMS.keys())

@app.get("/recipes", response_model=List[Recipe])
def get_recipes() -> List[Recipe]:
    all_recipes_flat = [recipe for recipes_list in ALL_RECIPES.values() for recipe in recipes_list]
    return all_recipes_flat

@app.get("/buildings")
def get_buildings() -> Dict:
    return BUILDING_DATA

@app.get("/max_output_from_extractors")
def get_max_output_from_extractors(
    item_name: str,
    num_extractors: int,
    extractor_level: int = 1
):
    try:
        max_output = calculate_max_raw_output(item_name, num_extractors, extractor_level)
        return {"item_name": item_name, "max_output": max_output}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/calculate")
def post_calculation(request: CalculationRequest):
    return calculate_requirements(
        request.item_name, 
        request.quantity, 
        request.active_alts, 
        request.building_levels
    )
