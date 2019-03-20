FROM library/ubuntu:18.04

ENV SHELL=/bin/bash

RUN apt-get update && \
    apt-get install -y vim \
                    emacs \
                    nano \
                    python3 \
                    python3-pip

RUN pip3 install --upgrade pip
COPY requirements.txt /home/jovyan/requirements.txt
RUN pip3 install -r /home/jovyan/requirements.txt
EXPOSE 8888
WORKDIR /root
CMD jupyter lab --ip=0.0.0.0 --allow-root
