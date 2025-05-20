# Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Default to production
ENV ENV=production

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Playwright browsers and Chromium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libasound2 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcb-dri3-0 \
    libdrm2 \
    libxss1 \
    libxshmfence1 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for better cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (chromium, firefox, webkit)
RUN playwright install --with-deps

# Copy the rest of the app code
COPY . .

# Expose port
EXPOSE 8000

# Run Uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
