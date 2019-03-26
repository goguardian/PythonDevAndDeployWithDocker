#Input variables; terraform will ask for input at the command line when 
#you run terraform plan, apply, and destroy.

variable "docker_tag" {
    type = "string"
    description = "Tag of docker image containing model server"
}

variable "docker_ami" {
    type = "string"
    description = "ID of AMI with Docker installed"
}

#We must attach a security group to the EC2 that specifies what kind
#of incoming traffic is allowed. We are going to allow 8081 (Nginx) and
#443 (SSL)

resource "aws_security_group" "model_server_security_group" {
    name = "model_server_security_group"

    # allow incoming requests through port 8081 (where NGINX is listening)
    ingress {
        from_port = 8081
        to_port = 8081
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    # allow outgoing requests through https (important for EC2 to reach docker registry)
    egress {
        from_port = 443
        to_port = 443
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

#Here we specify the EC2 that will host our model server.
#user_data specifies the start-up script for the EC2; we are asking that it 
#pulls and runs the docker image of our model_server

resource "aws_instance" "model_server" {
    ami = "${var.docker_ami}"
    instance_type = "t2.medium"
    vpc_security_group_ids = ["${aws_security_group.model_server_security_group.id}"]
    #specify a bash script to run upon start-up
    user_data = <<-EOF
        #!/bin/bash
        sudo docker run -p 8081:8081 "${var.docker_tag}"
        EOF
    tags = {
        Name = "model_server"
    }
}

#output the EC2's public IP address after running terraform apply

output "instance_ip_address" {
    value = "${aws_instance.model_server.public_ip}"
    description = "The public IP address of the model server"
}
