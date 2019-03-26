# Development with Docker

---


### Steps:

1. [Install Docker](https://docs.docker.com/docker-for-mac/)
2. Create a [docker hub](hub.docker.com) account (not necessary for this demo)
3. From this folder in the repo, run `docker-compose up --build -d`.
  * If you _don't_ want to rebuild the image, you can simply use `docker-compose up -d` after the build is complete.
4. Run `. listjupyterservers.sh` to get links to the jupyter lab server. 
5. When you're done, run `docker-compose donwn -v` from this folder to stop and remove the docker container.

### Customizing the resources here:

* To add new Python libraries, add to the `requirements.txt`. You can add versions by adding `<package>==<version_number>`.
* To add new functionality through `apt`, add new packages throught the `Dockerfile`.
* Change startup behavior, alter the `CMD` line in the `Dockerfile`.
* To change what files show up inside the container, alter the `volumes` in the `docker-compose.yml`.
* Re-run `docker-compose up --build -d` for your new changes to take effect!