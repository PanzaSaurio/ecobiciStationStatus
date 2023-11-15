# ecobiciStationStatus

Este proyecto utiliza la API de transporte de Buenos Aires para extraer información sobre las estaciones de Ecobici y su disponibilidad actual.

## Descripción

El script `ecobiciStationStatus.py` se encarga de realizar consultas a la API mencionada anteriormente, extrayendo detalles relevantes sobre las estaciones de Ecobici. La información se guarda en una base de datos Redshift para análisis posteriores.

## Estructura de la Tabla

La estructura de la tabla para guardar estos datos se encuentra en el archivo `ecobici_stations.sql`.

## Instalación

1. **Clona el repositorio**:
  git clone https://github.com/PanzaSaurio/ecobiciStationStatus.git


2. **Navega al directorio del proyecto**:
   ```
    cd ecobiciStationStatus
   
## Dependencias

Este proyecto utiliza las siguientes librerías:

### Librerías utilizadas:

  1. **requests**: Usada para hacer llamadas HTTP a la API.
  2. **pandas**: Usada para el manejo de datos en forma de DataFrames.

### Instrucciones de instalación:

  Para instalar estas bibliotecas, abre la terminal o línea de comandos y ejecuta los siguientes comandos:
    
     pip install requests
     pip install pandas
     pip install requests
     pip install psycopg2

## Uso

1. Ejecuta el script:
   ```
   python ecobiciStationStatus.py

3. Los datos se almacenarán en la base de datos Redshift configurada.

## Información Adicional

Para más detalles sobre la API utilizada, puedes visitar [API de Transporte de Buenos Aires] (https://api-transporte.buenosaires.gob.ar/).

