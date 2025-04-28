resource "aws_security_group" "app_sg" {
  description = "This is security group of app servers"
  name        = "app_sg"
  vpc_id      = "vpc-091b4904819ac2682"

  #ingress
  ingress {
    description = "None"
    from_port   = 1
    to_port     = 1
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["5.6.7.8/32"]
  }

  egress {
    description = "None"
    from_port   = 1
    to_port     = 1
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


   tags = {
    Name = "app_sg"
  }
}