from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="SmartMove - AI Travel Planner")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TripRequest(BaseModel):
    destination: str
    budget: str
    dates: str
    interests: str
    travel_style: str = "balanced"
    days: Optional[int] = 3

@app.get("/")
def home():
    return {"status": "FastAPI Running", "service": "SmartMove AI Planner"}

@app.post("/api/generate-itinerary")
def generate_itinerary(req: TripRequest):
    # Generative AI Prompt Engineering Logic
    prompt = f"""
    Create personalized itinerary for {req.destination},
    Budget: {req.budget}, Interests: {req.interests},
    Travel Style: {req.travel_style}, Duration: {req.days} days.
    Optimize: attractions, dining, accommodation, transport.
    """

    # Simulated AI-generated curated recommendations
    itinerary = {
        "destination": req.destination,
        "budget": req.budget,
        "travel_style": req.travel_style,
        "prompt_used": prompt,
        "optimized_plan": [
            {
                "day": 1,
                "theme": f"Arrival & {req.interests} exploration",
                "attractions": [f"Top attractions in {req.destination} for {req.interests}"],
                "dining": ["Curated local restaurants - budget: " + req.budget],
                "accommodation": ["Recommended stay based on " + req.travel_style],
                "transport": ["Optimized route with minimal travel time"]
            },
            {
                "day": 2,
                "theme": "Culture & Local Experience",
                "attractions": ["City tour, museums, hidden gems"],
                "dining": ["Affordable + curated dining options"],
                "accommodation": ["Same stay or alternative"],
                "transport": ["Public transport + walking optimized"]
            }
        ],
        "features": {
            "save_trip": "Ready for Supabase save",
            "edit_regenerate": "Endpoint supports regeneration",
            "dashboard": "Data ready for SaaS dashboard"
        }
    }
    return itinerary