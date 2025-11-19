FROM python:3.11-slim

# Define timezone
ENV TZ=America/Sao_Paulo

# Define work dir
WORKDIR /app

# Copy project
COPY . .

# Install debug helpers
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default expose, overwrite before.
EXPOSE 8080

# Run the main script
CMD ["python", "main.py", "8", "0"]



