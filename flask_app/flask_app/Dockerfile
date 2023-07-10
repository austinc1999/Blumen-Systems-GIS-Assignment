FROM python:3.10-slim
WORKDIR /flaskapp
EXPOSE 5000
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y libkrb5-dev gcc python3-dev

RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
