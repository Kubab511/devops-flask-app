FROM python:3.14

WORKDIR /usr/src/app

RUN pip install flask

COPY hello.py .

EXPOSE 5000

ENV FLASK_APP=hello.py

CMD ["python", "hello.py"]
