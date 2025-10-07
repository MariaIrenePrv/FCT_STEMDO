# Ejercicio 7 - Balanceador de carga con Nginx y Apache
## Objetivos
1. Entender para que sirve un Balanceador de carga.
2. Comprender que usos puede tener un Balanceador de carga.

## Consideraciones
 1. En vuestro repositorio `<vuestro nombre>-network-exercises` crear el archivo **Ejercicio-7.md** donde estaran vuestro documento resolviendo el laboratorio.

## Consejos
1. Crea una red de docker para que los dos contenedores esten en la misma red
2. Crea una carpeta en local para modificar mas sencillamente el nginx.conf
3. Si has usado una misma red e docker podras referenciarlo en el proxy_pass dentro del nginx.conf

## Tarea
El objetivo de este ejercicio es crear un entorno de balanceo de carga simple utilizando Nginx como balanceador de carga y dos contenedores Apache como servidores web. El balanceador de carga distribuirá el tráfico entre los dos servidores web Apache.

## Instrucciones
1. Desplegar dos contenedores de Apache
2. Desplegar y configurar Nginx como Balanceador de carga
3. Configurar Nginx para que escuche en un puerto específico y redirija las solicitudes a los dos contenedores de Apache
4. Acceder a los dos contenedores Apache a traves del Balanceador de carga de Nginx
