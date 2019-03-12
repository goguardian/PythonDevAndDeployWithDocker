FROM python:3.7.1

# install NGINX
RUN apt-get update && apt-get install -y nginx

# install python packages
RUN pip install tensorflow==1.13.1 \
    keras==2.2.4 \
    falcon==1.4.1 \
    falcon-multipart==0.2.0 \
    gunicorn==19.9.0 \
    pillow==5.4.1

# set working directory
WORKDIR /model_server/

# copy falcon app, model, and NGINX configuration into docker image
COPY . .

# move NGINX config to its proper place
RUN cp ./nginx.conf /etc/nginx/conf.d/

# restart NGINX and ask Gunicorn to start serving the Falcon API
CMD service nginx restart && \
    gunicorn -b 0.0.0.0:5000 model_server:api
