FROM python:3.11-slim-buster

WORKDIR /app

COPY . .

ENTRYPOINT [ "python", "__main__.py" ]
