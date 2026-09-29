from fastapi import APIRouter
from .schemas import EventSchema

router = APIRouter()

@router.get("/")
def read_events():
    return {
        "items": [{"id": 1}, {"id": 2}, {"id": 3}]
    }

@router.post("/")
def create_event(data:dict = {}) -> EventSchema:
    print(type(data))
    return {
        "id": 123
    }

@router.get("/{event_id}")
def read_events(event_id: int) -> EventSchema:
    return {
        "id": event_id
    }