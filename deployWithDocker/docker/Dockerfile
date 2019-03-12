FROM python:3.7.1

RUN apt-get update && apt-get install -y nginx

RUN pip install tensorflow \
    keras \
    falcon \
    falcon-multipart \
    gunicorn \
    pillow

WORKDIR /model_server/

COPY . .

RUN cp ./nginx.conf /etc/nginx/conf.d/

CMD service nginx restart && \
    gunicorn -b 0.0.0.0:5000 model_server:api
