# Ejercicio 6 - Proxy inverso con Nginx y Apache
## Objetivos
1. Entender para que sirve un proxy reverso.
2. Comprender que usos puede tener un proxy reverso.

## Consideraciones
 1. En vuestro repositorio `<vuestro nombre>-network-exercises` crear el archivo **Ejercicio-6.md** donde estaran vuestro documento resolviendo el laboratorio.

## Consejos
1. Crea una red de docker para que los dos contenedores esten en la misma red
2. Crea una carpeta en local para modificar mas sencillamente el nginx.conf
3. Si has usado una misma red e docker podras referenciarlo en el proxy_pass dentro del nginx.conf

## Tarea
- Configurar un entorno de proxy reverso utilizando Nginx como proxy inverso y Apache como servidor web backend, todo implementado dentro de contenedores Docker. Al finalizar el ejercicio, el usuario deberá ser capaz de acceder al contenido servido por Apache a través de Nginx, que actuará como intermediario y redireccionador de las solicitudes HTTP

## Instrucciones
1. Desplegar un contenedor de Apache
2. Desplegar y configurar Nginx como proxy reverso
3. Configurar Nginx para que escuche en un puerto específico y redirija las solicitudes al contenedor de Apache
4. Acceder a Apache a traves de Nginx

