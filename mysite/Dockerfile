FROM python:3.11.2
ENV PYTHONUNBFFERED 1
RUN apt-get -y update

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python","manage.py","runserver","127.0.0.1:8000"]

