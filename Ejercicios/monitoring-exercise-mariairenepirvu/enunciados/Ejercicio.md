# Objetivos Teóricos y Prácticos

1. **Comprender la Arquitectura de Kube-Prometheus-Stack**
    - Prometheus server
    - Alertmanager
    - Pushgateway
    - Exporters
    - Grafana


1. **Instalación del Chart de Kube-Prometheus-Stack**

   - Seguir la guía de instalación del [Kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack)


1. **Visualización de Datos**

   - Importar y crear dashboards en Grafana para visualizar métricas del clúster, como:
     - Memoria RAM en uso
     - CPU en uso
     - Espacio libre en disco
     - Ancho de banda de entrada y salida
     - etc
       
    > Sugerencia: Se suele importar dashboards ya existentes por la complejidad que conlleva crearlos. Para el ejercicio, se pide *de mínima* crear un dashboard simple e importa otro.

1. **Reutilización de Aplicaciones Laravel y MySQL Desplegadas Previamente**

    - Desplegar la aplicación de Laravel utilizada en el ejercicio semanal de Kubernetes.
    - Desplegar la aplicación de MySQL utilizada en el ejercicio semanal de Kubernetes.


1. **Creación de Alertas con PromQL**

   - Crear una alerta sencilla que indique el estado de la aplicación Laravel.
   - Crear una alerta sencilla que indique el estado de la base de datos MySQL.
   - Considerar el envío de mensajes de alerta por diferentes medios. (al menos dos distintos)
 

1. **Agregar Persistencia para las configuraciones de grafana utilizando Base de Datos**

   - Implementar persistencia para las configuraciones de grafana (dashboards, alertas) usando la `base de datos` MySQL existente.

1. **Agregar Persistencia de métricas**

   - Implementar persistencia para las métricas recolectadas.
   - Verificar su correcto funcionamiento eliminando un pod y viendo que las métricas anteriores a la eliminación siguen presentes.

1. **Configuración inicial (Opcional)**
   - Configura un values.yaml que permita incluir todas las personalizaciones realizadas en Prometheus y Grafana, como dashboards, alertas y contact points. El objetivo es que cualquier persona que despliegue el chart correspondiente usando este archivo tenga automáticamente disponibles todas las configuraciones iniciales que implementaste.

1. **Ejercicio sobre OpenWeather y su API (Opcional)**

   - https://github.com/stemdo-labs/Getting-Started-with-Prometheus-and-Grafana


## Entregables
- values.yaml con persistencias y configuración inicial (este último, es *opcional*)
- ficheros con las exportaciones de alertas, contact points, dashboards, etc.
- README detallando todo lo realizado
- chart del semanal de Helm de la semana anterior

> Todos estos elementos deben estar dentro de la carpeta **soluciones**