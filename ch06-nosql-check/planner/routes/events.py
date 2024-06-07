from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import select
from typing import List

from models.events import Event, EventUpdate
from beanie import PydanticObjectId
from database.connection import Database

event_database = Database(Event)

event_router = APIRouter(
    tags=["Events"]
)

# events = []

@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

@event_router.get('/{id}', response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if event:
        return event
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
@event_router.post('/new')
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Event created successfully."
    }

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = event_database.update(id, body)
    if updated_event:
        return updated_event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

@event_router.delete('/{id}')
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if event:
        return {
            "message": "Event deleted successfully."
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

# @event_router.delete('/')
# async def delete_all_events() -> dict:
#     events.clear()
#     return {
#         "message": "Event deleted all events successfully."
#     }