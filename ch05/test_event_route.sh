echo -e "\n"
echo "test: POST /new"
curl -X POST http://127.0.0.1:8000/event/new \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-d '{
    "id": 1,
    "title": "FastAPI",
    "image": "https://~~~~",
    "description": "blah blah",
    "tags": ["test", "test"],
    "location": "Google Meet"
}'

echo -e "\n"

echo "test: DELETE /event/1"
curl \
-X DELETE http://127.0.0.1:8000/event/1

echo -e "\n"

echo "test: GET /event/"
curl \
-X GET http://127.0.0.1:8000/event/ \
-H Accept:application/json

echo -e "\n"


echo "test: DELETE /event/"
curl \
-X DELETE http://127.0.0.1:8000/event/

echo -e "\n"
echo "test: GET /event/"
curl \
-X GET http://127.0.0.1:8000/event/ \
-H Accept:application/json