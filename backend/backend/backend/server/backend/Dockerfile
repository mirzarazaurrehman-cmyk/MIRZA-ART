FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run FastAPI app
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
