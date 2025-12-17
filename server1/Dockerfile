from python:3.11-slim
workdir /app
copy requiremants.txt .
run pip install --no-cache-dir -r requiremants.txt
copy . .
expose 8000
cmd ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]