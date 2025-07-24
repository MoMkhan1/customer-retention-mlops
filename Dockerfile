FROM python:3.12-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and tests
COPY src/ ./src
COPY tests/ ./tests

CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
