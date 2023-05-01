<p align="center">
<FONT FACE="times new roman" SIZE=5>
<i><b>Big Data e Ingeniería de Datos</b></i>
<br>
<img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png"
width="150" height="150">
</img>
<br>
<i><b>Docente:</b></i><br> Camilo Rodriguez
<br>
<i><b>Autores:</b></i>
<br>
Santiago Nohrá Nieto
<br>
Juan Camilo Rodríguez Fonseca
<br>
<i><b>Programa:</b></i>
<br>
Ciencias de la computación e inteligencia artificial
<br>

# Proyecto de Extracción, Transformación y Carga (ETL) en AWS Glue

Este proyecto tiene como objetivo realizar una descarga diaria de la página principal de los periódicos El Tiempo, El Espectador y Publimetro, para luego extraer la categoría, el titular y el enlace de cada noticia y almacenar esta información en un archivo CSV en un bucket de Amazon S3. Además, se actualizará el catálogo de AWS Glue y se permitirá la visualización de los datos en AWS Athena. Finalmente, se insertarán los datos en una base de datos MySQL alojada en Amazon RDS.

Este proyecto utiliza los siguientes servicios de AWS:

- AWS Glue: servicio de ETL totalmente administrado y escalable.
- AWS S3: almacenamiento de objetos en la nube de Amazon.
- AWS Athena: servicio interactivo de consultas de datos en S3.
- AWS RDS: servicio de bases de datos relacionales administrado por Amazon.

---

### Requerimientos

Para poder ejecutar este proyecto es necesario tener acceso a una cuenta en AWS y tener configuradas las siguientes herramientas:

- AWS Glue
- AWS S3
- AWS RDS (MySQL)
- AWS IAM (para los permisos necesarios)

Además, se necesita tener instalado:

- Python 3.8 o superior
- pip

### Configuración

Antes de ejecutar el proyecto, es necesario realizar las siguientes configuraciones:

1. Clonar el repositorio en la máquina local.

```bash
git clone https://github.com/tu_usuario/aws-glue-etl-periódicos.git
```

2. Crear un bucket en S3. Este será el lugar donde se almacenarán los datos crudos y procesados.

```bash
aws s3 mb s3://tu-bucket
```

3. Crear una base de datos en RDS. Este será el lugar donde se almacenarán los datos procesados.

4. Configurar los permisos necesarios en IAM para poder acceder a los servicios de AWS. Se deben configurar los permisos necesarios para poder acceder a S3, Glue y RDS.

5. Crear un archivo `credentials` en el directorio raíz del proyecto, con las credenciales necesarias para acceder a los servicios de AWS. Este archivo debe contener lo siguiente:

```ini
[aws]
aws_access_key_id = <tu_access_key_id>
aws_secret_access_key = <tu_secret_access_key>
aws_session_token = <tu_aws_session_token (Cuenta academy)>
region = <tu_region>
```

### Ejecución

Para ejecutar el proyecto, se debe seguir el siguiente flujo:

1. Ejecutar el job de Glue que descarga las páginas principales de los periódicos:

```bash
python3.9 job_parcial2.py
```

2. Esperar a que el job termine la descarga y procesamiento de las páginas. Luego, ejecutar el job de Glue que procesa los datos utilizando Beautifulsoup:

```bash
python3.9 job_parcial2_b.py
```

3. Esperar a que el job termine el procesamiento de los datos. Luego, ejecutar el archivo .py que actualiza los jobs:

```bash
python3.9 actualiza_jobs.py
```

4. Esperar a que terminen de actualizarse los jobs. Finalmente, el workflow de amazon se ejecutará diariamente con los códigos actualizados. Por lo mismo no será necesario hacer nada más que actualizar los jobs.
