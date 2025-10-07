# Ejercicio 2 - DockerHub
## Objetivos
Familiarizarse con la documentación de Dockerhub

## Consideraciones
 En la carpeta `soluciones` se creara una carpeta con el siguiente formato  `<vuestro nombre>-Ejercicio-2`.

## Tarea
 Responded a las siguientes cuestiones leyendo la documentación de DockerHub y razonando.

 1. ¿Qué significa que una imagen sea "oficial"? ¿Cuáles son las ventajas de utilizar imágenes oficiales?
 
 Que sea oficial significa que pasan por procesos de mantenimiento, revisión y aumento o mejora de la información ... Todo esto por parte de la plataforma pero también por parte de voluntarios, ingenieros de Docker, desarrolladores ... 

 Las ventajas son:
 * Seguridad
 * Compatibilidad entre intraestructuras y sistemas operativos
 * Constante actualización de la información
 * Variedad en versiones para diferentes usos
 * ...
 
 2. Elige una imagen que te interese y revisa su documentación en Docker Hub. ¿Qué información proporciona la documentación?

 Me centro en python ya que es la imagen que utilicé en la anterior práctica. 
 La documentación muestra bastante información de interés, esta es:
 * Información sobre el mantenimiento
 * Etiquetas compatibles 
 * Dockerfile
 * Definición de Python
 * Guía para la utilización de la imagen 
 * Variables de entorno 
 * Licencia 
 * Versiones o Tags
 * Vulnerabilidades, SO/Arquitectura, tamaño... de las diferentes versiones.


 3. ¿Cómo puede influir la versión de una imagen en su uso? ¿Qué estrategia usarías para seleccionar una versión específica?
 Puede influir bastante ya que puede tener cambios en su funcionalidad, seguridad, rendimiento y compatibilidad. 
 Según mis necesidades seleccionaría una versión u otra observando la documentación de cada una. Seleccionaría siempre alguna de las versones anteriores a "latest", ya que la última no suele ser tan estables. Además las versiones más recientes suelen tener mas problemas de compatibilidad ya que no suelene star preparadas para absolutamente todas las aplicaciones. 
 
 4. En la imagen de MySQL, ¿qué variables de entorno se pueden configurar? ¿Hay alguna que sea obligatoria?

 Las variables de entorno que se pueden configurar son:
 * MYSQL_ROOT_PASSWORD
 * MYSQL_DATABASE
 * MYSQL_USER,MYSQL_PASSWORD
 * MYSQL_ALLOW_EMPTY_PASSWORD
 * MYSQL_RANDOM_ROOT_PASSWORD
 * MYSQL_ONETIME_PASSWORD
 * MYSQL_INITDB_SKIP_TZINFO

 Según la documentación la única que es obligatoria es `MYSQL_ROOT_PASSWORD`

 5. En la imagen de Postgres, ¿cómo puedes establecer la contraseña para el usuario postgres utilizando una variable de entorno?
 Al iniciar el contenedor de Postgres debemos proporcionarle un valor a la variable `POSTGRES_PASSWORD`. Por lo tanto debemos declarar la variable al hacer el docker run; `docker run --name mipirvu_postgres -e POSTGRES_PASSWORD=contraseña  postgres`

 -e > Se utiliza para establecer variables de entorno

 6. En la imagen de NGINX, ¿es posible configurar variables de entorno para personalizar el comportamiento del servidor? Si es así, ¿qué opciones están 
    disponibles y qué efecto tienen?

Sí, es posible configurar variables de entorno en la configuración de nginx a partir de la versión 1.19. 

Las variables a modificar son:

* NGINX_ENVSUBST_TEMPLATE_DIR -> Define el directorio en el que se encontrarán los archivos de plantillas.
* NGINX_ENVSUBST_TEMPLATE_SUFFIX -> Define el sufijo de los archivos de plantilla
* NGINX_ENVSUBST_OUTPUT_DIR -> Define el directorio en el que se colocarán los resultados de **envsubst**

  
 7. ¿Qué puerto expone la imagen oficial de NGINX por defecto? ¿Cómo puedes mapear este puerto a uno diferente en tu máquina local cuando ejecutas el 
    contenedor?

El puerto por defecto es el **80**.

Puedes mapear el puerto a uno diferente con el siguiente comando: 

`$ docker run --name some-nginx -d -p 8080:80 some-content-nginx`
 
 `-p 8080:80`

 * 80 -> Es el puerto de Nginx
 * 8080 -> Es el al que se desea mapear 

 8. En la imagen de NGINX, ¿dónde debes montar un volumen para reemplazar el archivo index.html por defecto y servir tu propio contenido?

 Debes montarlo en `/usr/share/nginx/html`
 
 9. Para la imagen de Postgres, ¿dónde puedes montar un volumen para persistir las bases de datos que se generen en el contenedor?¿Qué pasa si no 
    configuras un volumen y el contenedor se reinicia o se elimina?
 
 El volumen debes montarlo en `/var/lib/postgresql/data`.

Si no configuras un volumen y el contenedor se reinicia o elimina, los datos se perderán ya que estos se guardarán en un volumen anónimo en lugar del volumen de datos deseado. 