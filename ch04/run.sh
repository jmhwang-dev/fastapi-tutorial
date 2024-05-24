# conda activate fastapi
pip install -r ../requirements.txt

mkdir -p template
touch {home,todo}.html

cp ../ch03/todo.py ../ch03/model.py ../ch03/api.py .