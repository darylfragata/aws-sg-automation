terraform {
  backend "s3" {
    bucket         = "dev-tfstatefile-backend"
    key            = "dev/aws-sg.tfstate"
    region         = "us-east-1"
    encrypt = true
    use_lockfile = true #Native S3  locking
  }
}