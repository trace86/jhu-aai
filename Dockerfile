# Retrieve image from Dockerhub
FROM python:3.8

# Install Vim
RUN apt-get update
RUN apt-get -y install git curl vim

# Install pip
RUN mkdir /opt/capstone
WORKDIR /opt/capstone
COPY requirements.txt /opt/capstone/requirements.txt
RUN pip install -r /opt/capstone/requirements.txt
