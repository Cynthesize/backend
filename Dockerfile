FROM python:3.6.6-stretch

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install megatools

WORKDIR /usr/src/

COPY src/ ./
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY collectandmigrate.sh ./
RUN chmod +x ./collectandmigrate.sh
RUN ./collectandmigrate.sh

CMD ["python", "./manage.py", "runserver", "0.0.0.0:8080"]
