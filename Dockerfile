FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY ./app /code/

EXPOSE 8003

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003" ]
