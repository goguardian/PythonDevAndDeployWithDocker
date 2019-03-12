variable "docker_tag" {
    type = "string"
    description = "Tag of docker image containing model server"
}

variable "docker_ami" {
    type = "string"
    description = "ID of AMI with Docker installed"
}

resource "aws_security_group" "model_server_security_group" {
    name = "model_server_security_group"

    ingress {
        from_port = 8081
        to_port = 8081
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 443
        to_port = 443
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "model_server" {
    ami = "${var.docker_ami}"
    instance_type = "t2.medium"
    vpc_security_group_ids = ["${aws_security_group.model_server_security_group.id}"]
    user_data = <<-EOF
        #!/bin/bash
        sudo docker run -p 8081:8081 "${var.docker_tag}"
        EOF

    tags = {
        Name = "model_server"
    }
}

output "instance_ip_address" {
    value = "${aws_instance.model_server.public_ip}"
    description = "The public IP address of the model server"
}
