# Development with Docker

---


### Steps:

1. [Install Docker](https://docs.docker.com/docker-for-mac/)
2. From the `devWithDocker` directory in the repo, run "`docker-compose up -d`".
  * If you make changes to the Dockerfile and want to rebuild the image, you can simply use `docker-compose up --build -d` to rebuild and run the image.
3. Run "`. listjupyterservers.sh`" to get a link to the jupyter lab server.
  * If that doesn't work, run "`docker exec devwithdocker_jupyter_1 jupyter notebook list`", and the link should print out! 
  * Click the link, or copy and paste into your browser. Jupyter lab should open!
4. When you're done, run "`docker-compose donwn -v`" from this directory to stop and remove the docker container.

### Customizing the resources here:

* To add new Python libraries, add to the `requirements.txt`. You can add versions by adding `<package>==<version_number>`.
* To add new functionality through `apt`, add new packages throught the `Dockerfile`.
* Change startup behavior, alter the `CMD` line in the `Dockerfile`.
* To change what files show up inside the container, alter the `volumes` in the `docker-compose.yml`.
* Re-run `docker-compose up --build -d` for your new changes to take effect!