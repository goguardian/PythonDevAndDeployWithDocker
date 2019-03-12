# Deploy a model server

## Prerequisites

* A [Docker Hub](https://hub.docker.com/) account. Sign-up [here](https://hub.docker.com/signup).
* An [Amazon Web Services](https://aws.amazon.com/) account. Sign-up [here](https://portal.aws.amazon.com/billing/signup#/start).
* [Terraform](https://www.terraform.io/) installed. Instructions [here](https://learn.hashicorp.com/terraform/getting-started/install).
* An MNIST model file entitled `model.h5` produced by the script `../devWithDocker/train_mnist.py`.

## Deploy an MNIST Model Server

1. Move the `model.h5` file into the folder `docker` (so that the docker daemon has access to it when building our `model_server` image).
2. Build the `model_server` docker image; make sure to include your dockerhub account as a prefix: `docker build -t lgjohnson/model_server` 
3. Push the `model_server` docker image to your public dockerhub account: `docker push lgjohnson/model_server`.
4. Initiate terraform: `terraform init`.
5. Check the terraform plan: `terraform plan`.
6. Execute the plan, supplying the dockerhub URI when prompted: `terraform make`.
7. Ping the server at the returned IP address.

## Troubleshooting

* >>Fill this out from dry-runs with data science, eng and friends
