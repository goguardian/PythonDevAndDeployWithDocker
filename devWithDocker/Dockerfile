FROM jupyter/scipy-notebook:latest

USER root

COPY requirements.txt /home/jovyan/requirements.txt
RUN pip install -r /home/jovyan/requirements.txt

USER jovyan

CMD jupyter lab
