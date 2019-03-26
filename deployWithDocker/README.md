# Deploy a model server

## Prerequisites

* [Docker]([https://docs.docker.com/install/](https://www.docker.com/)) installed. Instructions [here](https://docs.docker.com/install/).
* A [Docker Hub](https://hub.docker.com/) account. Sign-up [here](https://hub.docker.com/signup).
* An MNIST model file entitled `model.h5` produced by the script `../devWithDocker/train_mnist.py`.

To deploy on an AWS EC2:

* An [Amazon Web Services](https://aws.amazon.com/) account. Sign-up [here](https://portal.aws.amazon.com/billing/signup#/start).
* [Terraform](https://www.terraform.io/) installed. Instructions [here](https://learn.hashicorp.com/terraform/getting-started/install).

## Deploy an MNIST Model Server Locally

1. Open terminal and `cd` your bash process to `PythonDevAndDeploymentWithDocker/deployWithDocker`.
2. Build the `model_server` docker image: `docker build -t model_server docker/`.
3. Deploy the model server by running the docker image locally: `docker run -p 8081:8081 docker/`.
4. Check the health of the model server is running: `curl localhost:8081/health`.
5. Classify a picture of a digit: `curl -F "image=@images/img_1.jpg" localhost:8081/predict`.

### Clean-up

1. Remove docker image: `docker rmi model_server`.

## Deploy an MNIST Model Server on an AWS EC2

1. Open terminal and `cd` your bash process to `PythonDevAndDeploymentWithDocker/deployWithDocker`.
2. Build the `model_server` docker image, making sure to include your dockerhub account as a prefix e.g. `docker build -t <dockerhub_account>/model_server docker/`.
3. Push the `model_server` docker image to your public dockerhub account: e.g. `docker push <dockerhub_account>/model_server`.
4. Initiate terraform: `terraform init tf/`.
5. Check the terraform plan: `terraform plan tf/`.
6. Execute the plan with: `terraform apply tf/`. When asked for `docker_ami`, enter `ami-025e0be861ac07f91` and when asked for `docker_tag`, enter the tag specified in step 2 e.g. `<dockerhub_account>/model_server`.
7. Check if the model server is running at the returned public IP address: e.g. my IP address was `54.185.153.142` so I ran `curl http://54.185.153.142:8081/health`.
8. Classify a picture of a digit: e.g. `curl -F "image=@images/img_1.jpg" http://54.185.153.142:8081/predict`.

### Clean-up

1. Remove AWS infrastrucure: `terraform destroy tf/`.
2. Remove Docker image (optional): `docker rmi <dockerhub_account>/model_server`.

## Bonus: Create the AMI

An AMI (Amazon Machine Image) with a working docker installation has already been created using the server-templating tool Packer. It is publicly available under the AMI ID given in the above deployment guide. If you'd like to run this process yourself and create your own AMI, follow these steps:

1. In the `packer` directory, run `packer validate model_server.json` to ensure that the template is valid.
2. Run `packer build model_server.json` to build the AMI.
3. Take not of the AMI ID that is returned and use it in place of the provided AMI ID in the above deployment guide.
