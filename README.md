# Proyecto de Despliegue Red social en AWS con Terraform
Este proyecto implementa una infraestructura de despliegue automático de una infraestrutura de red social con Terraform como IaaS, implementando Docker en una instancia EC2. Todo esto usando Github ActiOns, AWS y Terraform

### Autora:
- **María José Ledesma** - [@MajoLedC](https://github.com/MajoLedC)

## 🏗️ Arquitectura

```
┌─────────────────┐
│  GitHub Actions │
│   (CI/CD)       │
└────────┬────────┘
         │
         ├─── Terraform ───┐
         │                 │
         ▼                 ▼
    ┌─────────┐      ┌──────────┐
    │   AWS   │      │  Docker  │
    │   EC2   │◄─────│Container │
    └─────────┘      └──────────┘
         │
         ▼
    ┌─────────┐
    │Streamlit│
    │   App   │
    └─────────┘
```

## 📂 Estructura del Proyecto

```plaintext
ProyectoTelematica/
├── main.tf                    # Definición principal de la infraestructura AWS
├── variables.tf               # Variables de configuración de Terraform
├── outputs.tf                 # Salidas del despliegue (IP pública, DNS, etc.)
├── terraform.tfvars          # Valores de las variables (no incluir en Git)
├── frontend/                  # Código de la aplicación
│   ├── Dockerfile            # Configuración del contenedor Docker
│   ├── requirements.txt      # Dependencias de Python
│   └── app.py                # Aplicación Streamlit
├── .github/
│   └── workflows/
│       ├── apply.yml         # Workflow para desplegar infraestructura
│       └── destroy.yml       # Workflow para destruir infraestructura
├── .gitignore                # Archivos a ignorar en Git
└── README.md                 # Este archivo
```

## Requisitos

1. **Cuenta de AWS activa**
2. **Credenciales de AWS** (Access Key ID, Secret Access Key y Session Token)
3. **Terraform** instalado localmente (versión ≤ 3.9) - *Opcional, solo para testing local*
4. **Cuenta de GitHub** con acceso al repositorio
5. **Git** instalado en tu máquina local
   
## Instrucciones 

### 1. Configurar GitHub Secrets
Agrega los siguientes secrets:

| Secret Name | Descripción | Ejemplo |
|------------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | Tu Access Key ID de AWS | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | Tu Secret Access Key de AWS | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `AWS_REGION` | Región de AWS a utilizar | `us-east-1` |
   
Para crearlos, navega a **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

### 2. Crear par de llaves en AWS
1. Accede a la consola de AWS, ve a **EC2** → **Key Pairs**
2. Crea una nueva llave con el nombre: **`ProyectoTele_Key`** y guarda.

### 3. Clona el repositorio

```bash
git clone https://github.com/MajoLedC/ProyectoTelematica.git
cd ProyectoTelematica
```
## Comprobación

Una vez desplegada la infraestructura:

1. Obtén la **IP pública** de la instancia desde los outputs de Terraform o desde la consola de AWS
2. Accede a la aplicación en tu navegador:
   ```
   http://<IP_PUBLICA>:8501
   ```

## 🚀 Despliegue

El despliegue se realiza automáticamente mediante GitHub Actions.

### Opción 1: Despliegue Manual (Trigger)

1. Ve a la pestaña **Actions** en tu repositorio de GitHub
2. Selecciona el workflow **"Apply Infrastructure"** (`apply.yml`)
3. Haz clic en **Run workflow**
4. Selecciona la rama (generalmente `main`)
5. Confirma la ejecución

### Opción 2: Despliegue Automático

El workflow se ejecutará automáticamente cuando:
- Hagas `push` a la rama `main`
- Realices cambios en los archivos `.tf` o en el directorio `frontend/`

### Monitorear el despliegue

1. Ve a **Actions** en GitHub
2. Observa el progreso del workflow en tiempo real
3. Una vez completado, verás las salidas en los logs, incluyendo:
   - IP pública de la instancia EC2
   - URL de acceso a la aplicación

## Destrucción de Infraestructura

Se añadió un workflow para eliminar todos los recursos creados y evitar costos innecesarios:

1. Ve a **Actions** en GitHub
2. Selecciona el workflow **"Destroy Infrastructure"** (`destroy.yml`)
3. Haz clic en **Run workflow**
4. Confirma la ejecución

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
|-----------|-----------|
| **Terraform** | Infrastructure as Code para provisionar recursos en AWS |
| **AWS EC2** | Servicio de cómputo en la nube para alojar la aplicación |
| **Docker** | Containerización de la aplicación para portabilidad |
| **Streamlit** | Framework de Python para crear la interfaz web de la red social |
| **GitHub Actions** | Automatización de CI/CD para despliegue continuo |
| **Python** | Lenguaje de programación principal |

⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub!
