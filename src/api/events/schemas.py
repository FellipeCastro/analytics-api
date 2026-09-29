from typing import List
from pydantic import BaseModel

class EventSchema(BaseModel):
    id: int

class EventListSchema(EventSchema):
    results: List[EventSchema]