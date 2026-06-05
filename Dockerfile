# Programming Visualization Platform
# Developed by issu321
# https://github.com/issu321/Programming-Visualization

FROM python:3.11-slim

LABEL maintainer="issu321"
LABEL description="Programming Visualization - AI-Powered Code Analysis Platform"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y     gcc     graphviz     && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p uploads reports database static/images

# Initialize database
RUN python -c "from database import init_db; init_db()"

# Expose port (Hugging Face Spaces uses 7860)
EXPOSE 7860

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV PORT=7860

# Run the application
CMD ["python", "app.py"]
