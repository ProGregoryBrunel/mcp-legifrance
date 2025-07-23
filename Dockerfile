FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir .
CMD ["legifrance-mcp", "--host", "0.0.0.0", "--port", "7777"]
