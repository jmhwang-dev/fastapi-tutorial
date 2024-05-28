# 이벤트 플래너 개발을 위한 폴더 구조화
##conda activate fastapi

rm -rf planner
mkdir planner && cd planner
touch main.py
mkdir database routes models
touch {database,routes,models}/__init__.py

touch database/connection.py
touch {routes,models}/{events,users}.py

pip install -r ../requirements.txt