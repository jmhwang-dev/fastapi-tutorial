curl \
    -X POST 'http://127.0.0.1:8000/event/new' \
    -H 'accept: applcation/json' \
    -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoicmVhZGVyQHBhY2t0LmNvbSIsImV4cGlyZXMiOjE3MTg4NjQ3NjcuMzg3NTgyfQ.1qQIXG0LdRvcQ-S-NT6TM4lLBbLkzZmJB_8oWHHzmhc' \
    -H 'Content-Type: application/json' \
    -d '{
        "title": "FastAPI Book Launch CLI",
        "image": "https://linktomyimage.com/image.png",
        "description": "열심히 열심히",
        "tags": ["python", "fastapi", "book", "launch"],
        "location": "Google Meet"
    }'