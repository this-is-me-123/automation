FROM node:18-slim

WORKDIR /app
COPY . .

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Puppeteer install (with Chromium)
RUN npm install

CMD ["node", "login.js"]
