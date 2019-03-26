
#specify cloud provider you would like Terraform to create infrastructure with
#if you have multiple AWS accounts, specify non-default accounts here
provider "aws" {
    region = "us-west-2"
}
