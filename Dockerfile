FROM python:3.14-alpine

WORKDIR /usr/src/app

RUN pip install flask redis

COPY hello.py .

EXPOSE 5000

ENV FLASK_APP=hello.py

CMD ["python", "hello.py"]
