provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "acceso_web" {
  name        = "acceso_web"
  description = "Permitir trafico HTTP para Streamlit"

  ingress {
    description = "Puerto Streamlit"
    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH acceso"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "streamlit_frontend" {
  ami                    = "ami-0c398cb65a93047f2"
  instance_type          = "t3.micro"
  key_name               = "ProyectoTele_Key"
  vpc_security_group_ids = [aws_security_group.acceso_web.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install -y docker.io docker-compose git

              sudo systemctl enable docker
              sudo systemctl start docker

              cd /home/ubuntu
              sudo git clone https://github.com/MajoLedC/ProyectoTelematica.git
              cd ProyectoTelematica/app/frontend

              sudo docker-compose up -d --build
              EOF


  tags = {
    Name = "StreamlitFrontend"
  }

  depends_on = [aws_security_group.acceso_web]
}

output "public_ip" {
  value       = aws_instance.streamlit_frontend.public_ip
  description = "IP pública para acceder a la app"
}