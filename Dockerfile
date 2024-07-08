# Base image olarak Python 3 
FROM python:3.8-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli dosyaları kopyala
COPY server.py /app/server.py
COPY requirements.txt /app/requirements.txt

# Gerekli bağımlılıkları yükle
RUN pip install -r requirements.txt

# Uygulamayı çalıştır
CMD ["python", "server.py"]

