# AMI: Ubuntu with Docker installed
data "aws_ami" "ubuntu" {
    
}

# EC2 instance
resource "aws_instance" "web" {
    ami = "${data.aws_ami.ubuntu.id}"
    instance_type = "t2.micro"
    vpc_security_group_ids = ["${aws_security_group.instance.id}"]
    user_data = <<-EOF
        #!/usr/bin/env bash
        docker run lgjohnson/model_server:latest
        EOF

    tags = {
        Name = "model_server"
    }
}

# Security group to allow incoming traffic
resource "aws_security_group" "instance" {
    name = "model_server_security_group"

    ingress {
        from_port = 8080
        to_port = 8080
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}
