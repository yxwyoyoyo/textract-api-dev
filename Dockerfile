FROM python:slim

RUN apt-get update && \
  apt-get install -y libxml2-dev libxslt1-dev antiword poppler-utils zlib1g-dev

RUN pip install flask

RUN pip install textract

COPY ./app /app

EXPOSE 5000

ENTRYPOINT [ "python", "/app/main.py" ]
