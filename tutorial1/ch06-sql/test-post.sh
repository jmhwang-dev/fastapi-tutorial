curl -X POST "http://127.0.0.1:8000/event/new" -H "accept: application/json" -H "Content-Type: application/json" -d '{
    "title": "FastAPI book",
    "image": "fastapi-book.jpeg",
    "description": "test",
    "tags": ["python", "fastapi", "book", "launch"],
    "location": "Google Meet"
}'