# conda activate fastapi
pip install -r ../requirements.txt

mkdir -p templates && touch templates/{home,todo}.html

cp -n ../ch03/todo.py ../ch03/model.py ../ch03/api.py .