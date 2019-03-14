# Deploy a model server

## Prerequisites

* A [Docker Hub](https://hub.docker.com/) account. Sign-up [here](https://hub.docker.com/signup).
* An [Amazon Web Services](https://aws.amazon.com/) account. Sign-up [here](https://portal.aws.amazon.com/billing/signup#/start).
* [Terraform](https://www.terraform.io/) installed. Instructions [here](https://learn.hashicorp.com/terraform/getting-started/install).
* An MNIST model file entitled `model.h5` produced by the script `../devWithDocker/train_mnist.py`.

## Deploy an MNIST Model Server

1. Open terminal and `cd` your bash process to `PythonDevAndDeploymentWithDocker/deployWithDocker`.
2. Move the `model.h5` file into the folder `docker` (so that the docker daemon has access to it when building our `model_server` docker image).
3. Build the `model_server` docker image, making sure to include your dockerhub account as a prefix e.g. `docker build -t lgjohnson/model_server docker/`.
4. Push the `model_server` docker image to your public dockerhub account: e.g. `docker push lgjohnson/model_server`.
5. Initiate terraform: `terraform init tf/`.
6. Check the terraform plan: `terraform plan tf/`.
7. Execute the plan with: `terraform apply tf/`. When asked for `docker_ami`, enter `ami-025e0be861ac07f91` and when asked for `docker_tag`, enter the tag specified in step 2 e.g. `lgjohnson/model_server`.
8. Check if the model server is running at the returned public IP address: e.g. my IP address was `54.185.153.142` so I ran `curl http://54.185.153.142:8081/health`.
9. Classify a picture of a digit: e.g. `curl -F "image=@images/img_1.jpg" http://localhost:8081/predict`

## Clean-up

1. Remove AWS infrastrucure: `terraform destroy tf/`.
2. 

## Bonus: Create the AMI

An AMI (Amazon Machine Image) with a working docker installation has already been created using the server-templating tool Packer. It is publicly available under the AMI ID given in the above deployment guide. If you'd like to run this process yourself and create your own AMI, follow these steps:

1. In the `packer` directory, run `packer validate model_server.json` to ensure that the template is valid.
2. Run `packer build model_server.json` to build the AMI.
3. Take not of the AMI ID that is returned and use it in place of the provided AMI ID in the above deployment guide.

## Troubleshooting

* >>Fill this out from dry-runs with data science, eng and friends
