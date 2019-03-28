![](https://media.glassdoor.com/sqll/1065069/goguardian-squarelogo-1444844793154.png)

# Development and Deployment with Docker and Python
---

This repo is for the SoCal Python Meetup at GoGuardian, on Thursday, 3/28/2019.
In this repo are resources to build your own development environment and deploy a toy machine learning model using Docker!

## Getting Started:

1. [**Install Docker CE**](https://www.docker.com/get-started)
2. **(Optional)** Create a [**Docker Hub**](https://hub.docker.com) account and log in to Docker on your machine through the GUI or with `docker login`
3. Run the following commands:

```
$ git clone https://github.com/goguardian/PythonDevAndDeployWithDocker.git
$ docker pull python:3.7.1
$ cd PythonDevAndDeployWithDocker/devWithDocker
$ docker-compose up -d
```

You should now be building a docker image! If any of these steps fail, especially the `docker pull`, try again in a few minutes!

## Additional Resources:


* [**GoGuardian Careers**](https://www.goguardian.com/careers.html), check out our jobs!
* [**Docker documentation**](https://docs.docker.com/)
* [**tf.Keras**](https://www.tensorflow.org/guide/keras), the API we used to develop our ML model
* [**Jupyter Lab Documentation**](https://jupyterlab.readthedocs.io/en/stable/)
* [**Theia IDE**](https://github.com/theia-ide/theia-apps), an alternative to developing in Jupyter that's closer to VSCode

