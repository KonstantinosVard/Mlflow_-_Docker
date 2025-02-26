FROM python:3.10.7-slim

WORKDIR /app

# Upgrade pip and tools to avoid source builds
RUN pip install --upgrade pip setuptools wheel

# Install dependencies without build-essential
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY templates templates
COPY model.pkl model.pkl
COPY main.py main.py

CMD ["python", "main.py"]