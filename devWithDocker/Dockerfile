# Build this image on a brand spankin' new Ubuntu 18.04 system
FROM library/ubuntu:18.04

# Make the default shell bash
ENV SHELL=/bin/bash

# Update apt and install some bare essentials
RUN apt-get update && \
    apt-get install -y vim \
                    emacs \
                    nano \
                    wget \
                    curl \
                    python3 \
                    python3-pip \
                    sudo


# Upgade pip
RUN pip3 install --upgrade pip

# Copy requirements.txt in so that pip can access it
COPY requirements.txt /home/requirements.txt

# Install the requirements.txt
RUN pip3 install -r /home/requirements.txt

# Create the dev user
RUN useradd -m dev && echo "dev:dev" | chpasswd && adduser dev sudo

# Change the workdir to /home/dev
WORKDIR /home/dev

# Make the user dev
USER dev

# Run the app we want to run. In this case, jupyter lab.
CMD jupyter lab --ip=0.0.0.0
