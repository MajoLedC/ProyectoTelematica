provider "aws" {
  region = "us-east-1"
}

# Security Group con puertos correctos
resource "aws_security_group" "allow_web" {
  name        = "allow_web"
  description = "Permitir trafico HTTP para Streamlit"

  # Puerto de Streamlit
  ingress {
    description = "Puerto Streamlit"
    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # SSH para debugging
  ingress {
    description = "SSH acceso"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Tráfico de salida
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "streamlit-security-group"
  }
}

# Instancia EC2
resource "aws_instance" "streamlit_frontend" {
  ami                    = "ami-0c398cb65a93047f2"
  instance_type          = "t3.micro"
  key_name               = "ProyectoTele_Key"
  vpc_security_group_ids = [aws_security_group.allow_web.id]

  user_data = <<-EOF
              #!/bin/bash
              
              # Redirigir toda la salida a un log
              exec > /var/log/user-data.log 2>&1
              set -ex

              # Actualizar sistema
              apt update -y
              apt upgrade -y

              # Instalar Docker y Git
              apt install -y docker.io docker-compose git

              # Iniciar Docker
              systemctl enable docker
              systemctl start docker

              # Agregar ubuntu al grupo docker
              usermod -aG docker ubuntu

              cd /home/ubuntu

              # Clonar repositorio
              git clone https://github.com/MajoLedC/ProyectoTelematica.git
              cd ProyectoTelematica

              # Cambiar permisos
              chown -R ubuntu:ubuntu /home/ubuntu/ProyectoTelematica

              echo "=== Verificando estructura ==="
              ls -la
              pwd

              # Ir al directorio correcto según tu estructura
              cd frontend

              echo "=== Contenido de frontend ==="
              ls -la

              # Levantar docker-compose (sin sudo, ya estamos como root)
              docker-compose up -d --build

              echo "=== Verificando contenedores ==="
              docker ps -a

              echo "=== Logs de contenedores ==="
              docker-compose logs

              echo "=== Instalación completada $(date) ==="
              echo "Accede a: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4):8501"
              EOF

  tags = {
    Name = "StreamlitFrontend"
  }

  depends_on = [aws_security_group.allow_web]
}

# Output con la URL completa
output "public_ip" {
  value       = aws_instance.streamlit_frontend.public_ip
  description = "IP pública de la instancia"
}

output "streamlit_url" {
  value       = "http://${aws_instance.streamlit_frontend.public_ip}:8501"
  description = "URL completa para acceder a Streamlit"
}

output "ssh_command" {
  value       = "ssh -i ~/.ssh/ProyectoTele_Key.pem ubuntu@${aws_instance.streamlit_frontend.public_ip}"
  description = "Comando para conectarte por SSH"
}