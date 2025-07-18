FROM python:3.10-slim

# Install Chrome and dependencies
RUN apt-get update && apt-get install -y \
    wget gnupg unzip curl \
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver

# Set working directory
WORKDIR /app
COPY . /app

# Install Python packages
RUN pip install -r requirements.txt

# Create session folder
RUN mkdir -p /app/session

# Run script
CMD ["bash", "entrypoint.sh"]
