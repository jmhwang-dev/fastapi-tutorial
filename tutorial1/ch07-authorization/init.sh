cp -r ../ch06-nosql/planner ./planner

mkdir -p ./planner/auth
cd ./planner/auth && touch {__init__,jwt_handler,authenticate,hash_password}.py

find '../ch06-nosql' -type f -name 'mongodb-*' -exec cp {} './planner' \;