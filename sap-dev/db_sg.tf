resource "aws_security_group" "db_sg" {
  description = "This is security group of app servers"
  name        = "db_sg"
  vpc_id      = "vpc-091b4904819ac2682"

  #ingress
  ingress {
    description = "DB"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "DB"
    from_port   = 123
    to_port     = 123
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["1.2.3.4/32"]
  }


   tags = {
    Name = "db_sg"
  }
}