FROM python:3.11

WORKDIR /the/workdir/path

COPY . .

ENTRYPOINT [ "executable", "main" ]