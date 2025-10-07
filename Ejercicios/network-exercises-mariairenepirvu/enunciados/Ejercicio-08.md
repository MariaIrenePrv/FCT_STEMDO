# Ejercicio 8 - Laboratorio Cisco Packet Tracer
## Objetivos
1. Crear Una red funcional ajustada a lo que nos piden
## Consideraciones
 1. En vuestro repositorio `<vuestro nombre>-network-exercises` crear el archivo **Ejercicio-8.md** donde estaran vuestras respuestas.

## Enunciado
- Configurar una red LAN simple en Cisco Packet Tracer que incluya múltiples switches y routers, utilizando VLANs para segmentar la red y RIP como protocolo de enrutamiento para interconectar diferentes segmentos de la red.
 
## Topología de la red
3 Switches: Switch0, Switch1, Switch2
2 Routers: Router0, Router1
6 PCs: PC0, PC1, PC2, PC3, PC4, PC5

## Tarea
- Crear dos VLANs en cada switch:
  - VLAN 10: Red para el departamento de Ventas
  - VLAN 20: Red para el departamento de Soporte Técnico

- Asignar las PCs de manera que:
  - PC0 y PC1 estén en VLAN 10 en Switch0.
  - PC2 y PC3 estén en VLAN 20 en Switch1.
  - PC4 y PC5 estén en VLAN 10 y VLAN 20 respectivamente, en Switch2.

- Configuración de Ruteo Inter-VLAN:
  - Configurar Router-on-a-Stick en Router0 para manejar el ruteo entre VLAN 10 y VLAN 20.
  - Habilitar las subinterfaces en Router0 para las VLANs correspondientes.

- Configuración de Enrutamiento entre Routers:
  - Conectar Router0 y Router1 utilizando un enlace serial.
  - Configurar RIP v2 en ambos routers para permitir el ruteo dinámico entre las diferentes redes (VLANs y segmentos de red).

- Configuración de Switches:
  - Configurar trunking entre los switches para permitir la propagación de VLANs a través de todos los switches.
  - Asegurarse de que el tráfico de cada VLAN se propague correctamente entre los switches.

- Configuración de PCs:
  - Asignar direcciones IP a cada PC de acuerdo con las VLANs configuradas.
  - Configurar las puertas de enlace predeterminadas para cada PC, apuntando a la subinterfaz del router correspondiente.

- Pruebas de Conectividad:
  - Verificar la conectividad entre PCs en la misma VLAN.
  - Verificar la conectividad entre PCs en diferentes VLANs.
  - Verificar la conectividad entre PCs en diferentes redes a través del protocolo RIP.

- Solución de Problemas:
  - Realizar ping entre las diferentes PCs para asegurarse de que la red está correctamente configurada.
  - Usar herramientas como Traceroute para verificar las rutas que sigue el tráfico.
Resolver cualquier problema de conectividad ajustando configuraciones en los routers y switches.
