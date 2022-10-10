FROM python:3.7-slim-buster
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    python3-setuptools 
RUN apt-get install -y python-all-dev
RUN apt-get install -y wget
RUN apt install -y python-opencv

COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED True
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD [ "python3", "main.py" ]