FROM python:3.11-slim

# Define timezone
ENV TZ=America/Sao_Paulo

# Define diretório de trabalho
WORKDIR /app

# Copia o projeto inteiro
COPY . .

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Instala dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do server.py (se o front acessa ele)
EXPOSE 8080

# Comando final — inicia o loop do main
CMD ["python", "main.py"]


