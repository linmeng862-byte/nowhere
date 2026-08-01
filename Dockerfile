FROM python:3.12-slim
WORKDIR /app
RUN pip install fastmcp httpx numpy scipy skyfield timezonefinder uvicorn opencc-python-reimplemented ephem tzdata
COPY . .
EXPOSE 8000
CMD ["python", "-m", "nowhere.server_http", "--port", "8000"]
