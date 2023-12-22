# Proyecto de Monitoreo de Ecobici y Vehículos de Transporte Público

Este proyecto utiliza la API de transporte de Buenos Aires para recopilar y almacenar información sobre las estaciones de Ecobici y la posición de los vehículos de transporte público. El objetivo es facilitar el monitoreo y la gestión de la movilidad urbana en la ciudad.

## Descripción

El proyecto consta de dos componentes principales:

1. **Monitoreo de Estaciones de Ecobici (`ecobiciStationStatus.py`)**: Recopila datos sobre las estaciones de Ecobici, incluyendo disponibilidad de bicicletas y estado de las estaciones.

2. **Monitoreo de Posiciones de Vehículos (`vehicleData.py`)**: Obtiene información en tiempo real sobre la ubicación y el estado de los vehículos de transporte público.

Los datos se almacenan en una base de datos Redshift para su posterior análisis.

## Requisitos Previos

- Docker y Docker Compose.
- Clave de acceso a la API de Transporte de Buenos Aires.
- Acceso a una instancia de AWS Redshift.

## Configuración del Entorno

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/PanzaSaurio/ecobiciStationStatus.git

Claro, aquí tienes el contenido del README.md en formato Markdown, listo para ser utilizado en tu repositorio de Git:

markdown

# Proyecto de Monitoreo de Ecobici y Vehículos de Transporte Público

Este proyecto utiliza la API de transporte de Buenos Aires para recopilar y almacenar información sobre las estaciones de Ecobici y la posición de los vehículos de transporte público. El objetivo es facilitar el monitoreo y la gestión de la movilidad urbana en la ciudad.

## Descripción

El proyecto consta de dos componentes principales:

1. **Monitoreo de Estaciones de Ecobici (`ecobiciStationStatus.py`)**: Recopila datos sobre las estaciones de Ecobici, incluyendo disponibilidad de bicicletas y estado de las estaciones.

2. **Monitoreo de Posiciones de Vehículos (`vehicleData.py`)**: Obtiene información en tiempo real sobre la ubicación y el estado de los vehículos de transporte público.

Los datos se almacenan en una base de datos Redshift para su posterior análisis.

## Requisitos Previos

- Docker y Docker Compose.
- Clave de acceso a la API de Transporte de Buenos Aires.
- Acceso a una instancia de AWS Redshift.

## Configuración del Entorno

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/PanzaSaurio/ecobiciStationStatus.git

    Navegar al Directorio del Proyecto:

    bash

    cd tu-repositorio

    Configurar las Credenciales: Modificar el archivo credentials.json con tus credenciales de la API y detalles de conexión a Redshift.

Uso con Docker

El proyecto está configurado para ejecutarse en un entorno Dockerizado, utilizando Airflow para la programación y ejecución de tareas.

    Construir y Levantar los Contenedores:

    bash

    docker-compose up -d

    Acceder a Airflow:
        Abre un navegador y visita http://localhost:8080.
        Utiliza las credenciales predeterminadas (airflow/airflow) para iniciar sesión.

    Programar y Ejecutar DAGs:
        En la interfaz de Airflow, habilita y ejecuta los DAGs dag_ecobiciStationStatus y dag_vehicle_position_data para comenzar a recopilar datos.

Estructura de Datos

Las estructuras de las tablas para almacenar los datos están definidas en los archivos SQL (ecobici_stations.sql y vehicle_positions.sql).
Información Adicional

Para más detalles sobre la API utilizada, puedes visitar la documentación de la API de Transporte de Buenos Aires.
Soporte y Contribuciones

Para soporte, sugerencias o contribuciones, por favor abre un issue o pull request en el repositorio de GitHub.
