FROM python:3.7.2

RUN pip install tensorflow \
    keras \
    falcon \
    pillow

WORKDIR /model_server/

COPY . .

CMD python model_server.py
