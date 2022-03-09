# Retrieve image from Dockerhub
FROM python:3.8

# Install Vim
USER root
RUN sudo apt-get update
RUN sudo apt-get -y install git curl vim python-

# Install pip
RUN mkdir /opt/capstone
WORKDIR /opt/capstone
COPY requirements.txt /opt/capstone/requirements.txt