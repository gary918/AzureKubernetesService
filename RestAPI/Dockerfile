FROM python:3.9-slim-bullseye

COPY ./requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /opt/app/src

CMD ["uvicorn", "--app-dir", "src", "app:app", "--workers", "2", "--host", "0.0.0.0", "--port", "8080"]
