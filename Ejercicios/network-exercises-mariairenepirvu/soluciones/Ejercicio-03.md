# Ejercicio 3 - Modelos OSI y TCP/IP

  Indicar de cada ejemplo a que capa de los dos modelos pertenece, justifica tu respuesta.
   
- Codificación de los datos en bits y manejo de la transmisión física de los datos a través de un cable de red.
  * Modelo OSI ->  Capa Física
  * Modelo TCP/IP -> Capa de Acceso a Red

    Esta capa realiza la transmisión de bits por medios físicos.


- Aseguramiento de la entrega de mensajes completos entre dos dispositivos, incluyendo la corrección de errores y la retransmisión si es necesario.
  * Modelo OSI -> Capa de Transporte
  * Modelo TCP/IP -> Capa de Transporte

    Esta capa garantiza que los datos lleguen completos y correctamente. Además corrige erores y gestiona la retrasmisión.  

- Asignación de direcciones IP y encaminamiento de paquetes a través de diferentes redes hasta su destino final.
  * Modelo OSI -> Capa de Red 
  * Modelo TCP/IP -> Capa de Internet

     Esta capa se ocupa del direccionamiento lógico y del enrutamiento. 

- Establecimiento, mantenimiento y finalización de una sesión de comunicación entre dos dispositivos.
  * Modelo OSI -> Capa de Sesión
  * Modelo TCP/IP -> Capa de Aplicación 

     Controla el diálogo entre aplicaciones, la duración de este, el comienzo y el final.

- Conversión de los datos a un formato común para que puedan ser comprendidos por diferentes sistemas (p. ej., codificación de caracteres, cifrado).
  * Modelo OSI ->  Capa de Presentación
  * Modelo TCP/IP -> Capa de Aplicación

    Traduce, cifra o comprime los datos para ser comprendidos por diferentes sitemas. 


- Manejo de las conexiones de red, incluyendo el control de flujo y la secuenciación de los datos.
  * Modelo OSI -> Capa de Transporte 
  * Modelo TCP/IP -> Capa de Transporte

     Asegura el envío ordenado de los datos y la correcta velocidad del receptor, controlando el flujo y la secuencia.  


- Presentación de la interfaz al usuario final y manejo de la interacción entre aplicaciones (p. ej., navegación web, envío de correos electrónicos).
  * Modelo OSI -> Capa de Aplicación
  * Modelo TCP/IP -> Capa de Aplicación 

    Capa en la que interactúan directamente los usuarios con sus aplicaciones. 