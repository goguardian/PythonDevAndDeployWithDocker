# Build this image on a brand spankin' new Ubuntu 18.04 system
FROM library/ubuntu:18.04

# Make the default shell bash
ENV SHELL=/bin/bash

# Update apt and install some bare essentials
RUN apt-get update && \
    apt-get install -y vim \
                    emacs \
                    nano \
                    python3 \
                    python3-pip

# Upgade pip
RUN pip3 install --upgrade pip

# Copy requirements.txt in so that pip can access it
COPY requirements.txt /home/requirements.txt

# Install the requirements.txt
RUN pip3 install -r /home/requirements.txt

# Set the workdir to the root folder
WORKDIR /root

# Run the app we want to run. In this case, jupyter lab.
CMD jupyter lab --ip=0.0.0.0 --allow-root
