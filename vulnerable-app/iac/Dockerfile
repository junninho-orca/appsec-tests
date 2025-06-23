FROM python:3.7-slim-buste

# Adding a hardcoded secret
ENV API_KEY="a1b2c3d4e5f6g7h8i9j0"

WORKDIR /app
COPY ../app /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"] 