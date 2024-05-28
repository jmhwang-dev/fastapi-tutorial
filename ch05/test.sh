echo "POST /signup test"
curl -X POST http://127.0.0.1:8000/user/signup \
-H accept:application/json \
-H Content-Type:application/json \
-d '{
    "email": "fastapi@packt.com",
    "password": "Stro9ng!"
}'

echo -e "\n"

echo "POST /signin test"
curl -X POST http://127.0.0.1:8000/user/signin \
-H accept:application/json \
-H Content-Type:application/json \
-d '{
    "email": "fastapi@packt.com",
    "password": "qwerqwerqwer!"
}'