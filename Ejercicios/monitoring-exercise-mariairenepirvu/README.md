# Unidad Didáctica: Observabilidad y Alertas en Kubernetes usando Prometheus y Grafana

## Objetivos de Aprendizaje

    - Entender los conceptos de observabilidad en sistemas distribuidos.
    - Configurar Prometheus y Grafana en un clúster de Minikube.
    - Crear alertas y analizar métricas en Grafana.

## Contenido

### Introducción a la Observabilidad

    - Definición de observabilidad.
    - Importancia en sistemas distribuidos.
    - Componentes principales: logs, métricas y trazas.

### Introducción a Prometheus y Grafana

    - ¿Qué es Prometheus?
    - ¿Qué es Grafana?
    - Caso de uso: Monitoreo de una aplicación Laravel y MySQL en Kubernetes.

### Despliegue y Configuración de Prometheus y Grafana en Minikube

    - Instalación de Prometheus y Grafana usando Helm.
    - Configuración de Prometheus y Grafana.
    - Creación de dashboards en Grafana para visualizar métricas.

### Creación de Alertas en Grafana

    - Configuración de canales de notificación.
    - Añadir y configurar alertas en paneles de Grafana.

### Análisis de Métricas y Alertas en Grafana

    - Visualización de métricas en dashboards.
    - Análisis de datos y toma de decisiones.
    - Respuesta a alertas y acciones correctivas.

# Módulo 1: Introducción a la Observabilidad

### Objetivo

Comprender la importancia y los componentes de la observabilidad en sistemas distribuidos.

## Contenidos

    - Concepto de observabilidad.
    - Logs, métricas y trazas.
    - Herramientas de observabilidad.

## Concepto de Observabilidad

La observabilidad es una propiedad de los sistemas que permite medir su estado interno mediante
la inspección de las salidas externas. Este concepto proviene de la teoría de control y se ha
adaptado al campo de la ingeniería de software para facilitar el monitoreo y la gestión de sistemas
complejos y distribuidos.

En el contexto de la ingeniería de software, la observabilidad es esencial porque:

    - Permite a los equipos de desarrollo y operaciones entender cómo se comporta el sistema.
    - Ayuda a identificar y resolver problemas de manera proactiva.
    - Facilita el mantenimiento de la salud y el rendimiento del sistema a largo plazo.

## Componentes Principales de la Observabilidad

La observabilidad se compone de tres pilares fundamentales:

1. **Logs**

   - Los logs son registros cronológicos de eventos que ocurren en un sistema.
   - Proporcionan un registro detallado de las actividades del sistema y son útiles para el diagnóstico de problemas.
   - Ejemplo: Los registros de acceso a un servidor web, errores de aplicaciones, eventos del sistema operativo.

2. **Métricas**

   - Las métricas son datos numéricos cuantificables que describen el rendimiento y el estado de un sistema.
   - Se recopilan a intervalos regulares y se utilizan para el monitoreo en tiempo real.
   - Ejemplo: Tasa de solicitudes por segundo, uso de CPU, memoria utilizada.

3. **Trazas**

   - Las trazas rastrean la ejecución de transacciones o peticiones a través de los componentes distribuidos de un sistema.
   - Permiten identificar cuellos de botella y dependencias entre servicios.
   - Ejemplo: Una traza de una solicitud HTTP que pasa por varios microservicios antes de devolver una respuesta al cliente.

## Importancia de la Observabilidad en Sistemas Distribuidos

En sistemas distribuidos, donde múltiples servicios interactúan entre sí, la observabilidad se vuelve crucial por varias razones:

1. **Detección y Resolución Rápida de Problemas**

   - La observabilidad permite identificar rápidamente problemas y su causa raíz.
   - Facilita la resolución proactiva de incidentes antes de que afecten a los usuarios finales.

2. **Optimización del Rendimiento**

   - Proporciona información detallada sobre el comportamiento del sistema bajo diferentes cargas de trabajo.
   - Ayuda a optimizar el uso de recursos y mejorar el rendimiento general del sistema.

3. **Planificación de Capacidad**

   - Permite anticipar la demanda futura basada en tendencias de uso actuales.
   - Ayuda en la planificación de la capacidad y la escalabilidad del sistema.

## Herramientas de Observabilidad

Existen varias herramientas que ayudan a implementar la observabilidad en sistemas modernos. Algunas de las más populares incluyen:

1.  **Prometheus** [Documentación oficial](https://prometheus.io/docs/introduction/overview/)

    - Sistema de monitoreo y alerta de código abierto.
    - Almacena sus datos como una serie temporal, permitiendo consultas poderosas a través de PromQL.
    - Facilita la recopilación de métricas y la generación de alertas.

2.  **Grafana** [Documentación oficial](https://grafana.com/docs/grafana/latest/)

    - Plataforma de análisis y monitoreo de código abierto.
    - Permite visualizar métricas a través de dashboards dinámicos y personalizables.
    - Soporta múltiples fuentes de datos, incluyendo Prometheus.

3. **Elasticsearch, Logstash, and Kibana (ELK Stack)** [Documentación oficial](https://www.elastic.co/what-is/elk-stack)

    - Conjunto de herramientas para la búsqueda, análisis y visualización de datos de logs.
    - Elasticsearch almacena y busca datos, Logstash procesa y transporta datos, y Kibana visualiza datos.
    - Facilita el análisis de logs y la detección de patrones y anomalías.
4. **Jaeger** [Documentación oficial](https://www.jaegertracing.io/docs/1.18/)

    - Sistema de rastreo distribuido de código abierto.
    - Ayuda a monitorear y solucionar problemas de microservicios.
    - Proporciona capacidades de rastreo end-to-end.


---
# Módulo 2: Introducción a Prometheus y Grafana

### Objetivo

Familiarizarse con Prometheus y Grafana y entender su rol en la observabilidad.

### Contenidos

- Arquitectura de Prometheus.
- Funcionalidades de Grafana.
- Integración de Prometheus y Grafana.

## Prometheus

**Prometheus** es un sistema de monitoreo y alerta de código abierto desarrollado inicialmente por SoundCloud. Desde su lanzamiento en 2012, ha ganado popularidad y se ha convertido en un proyecto oficial de la Cloud Native Computing Foundation (CNCF).

### **Características Clave de Prometheus**

1. **Modelo de Datos de Series Temporales**:

    - Las métricas se almacenan como series temporales, que consisten en una secuencia de pares de valores de tiempo.
    - Cada serie temporal tiene una etiqueta de nombre y un conjunto de etiquetas de clave-valor que identifican de manera única la serie.

2. **Lenguaje de Consultas PromQL**:

    - Prometheus ofrece un potente lenguaje de consultas llamado PromQL.
    - Permite seleccionar y agregar datos de series temporales en tiempo real.

3. **Extracción de Datos**:

    - Prometheus extrae datos de los puntos finales configurados mediante HTTP.
    - Utiliza el formato de texto de Prometheus para exportar métricas.

4. **Alertas**:

    - Prometheus tiene una herramienta de gestión de alertas que permite definir reglas de alerta basadas en las consultas de PromQL.
    - Las alertas pueden ser enviadas a través de varios métodos de notificación como email, Slack, etc.

5. **Arquitectura de Módulos**:

    - Prometheus consta de varios componentes, cada uno de los cuales puede funcionar de manera independiente:
      - **Prometheus Server**: Recopila y almacena métricas.
      - **Alertmanager**: Gestiona las alertas.
      - **Exporters**: Herramientas que exponen métricas a Prometheus.
      - **Pushgateway**: Permite que los trabajos de corta duración envíen métricas a Prometheus.

### **Arquitectura de Prometheus**

- **Prometheus Server**:
  - Es el núcleo de Prometheus.
  - Extrae métricas en intervalos regulares y las almacena localmente.

- **Exporters**:
  - Prometheus puede recopilar métricas de varios sistemas y servicios a través de Exporters.
  - Ejemplos comunes incluyen Node Exporter para métricas de hardware, Blackbox Exporter para monitoreo de endpoints HTTP.

- **Alertmanager**:
  - Gestiona las alertas enviadas por Prometheus.
  - Deduplica, agrupa y enruta las alertas a los canales de notificación configurados.

- **Pushgateway**:
  - Utilizado para trabajos de corta duración.
  - Permite que estos trabajos envíen métricas a Prometheus que luego las extrae desde el Pushgateway.

## Grafana

**Grafana** es una plataforma de análisis y monitoreo de código abierto que permite crear y compartir dashboards interactivos. Es ampliamente utilizada para visualizar métricas de sistemas, aplicaciones y bases de datos.

### Características Clave de Grafana
1. **Dashboards Personalizables**:

    - Los usuarios pueden crear dashboards altamente personalizables que visualizan datos de múltiples fuentes.

2. **Soporte para Múltiples Fuentes de Datos**:

    - Grafana soporta una amplia variedad de fuentes de datos, incluyendo Prometheus, Graphite, InfluxDB, Elasticsearch, MySQL, PostgreSQL, y muchas más.

3. **Paneles Interactivos**:

    - Ofrece una variedad de paneles para mostrar diferentes tipos de visualización, como gráficos de líneas, gráficos de barras, tablas, mapas de calor, entre otros.

4. **Alertas**:

    - Permite configurar alertas que pueden enviarse a través de varios canales como email, Slack, PagerDuty, etc.

5. **Usuarios y Roles**:

    - Grafana proporciona control de acceso basado en roles, permitiendo gestionar permisos para usuarios y equipos.

6. **Plugins**:

    - Grafana cuenta con una gran cantidad de plugins que extienden sus funcionalidades, como nuevos tipos de paneles, integraciones de datos y aplicaciones.

### Arquitectura de Grafana

- **Frontend**:

  - La interfaz de usuario de Grafana está basada en web, lo que permite crear y compartir dashboards de forma intuitiva.

- **Backend**:

  - El backend de Grafana está escrito en Go y proporciona APIs para manejar la autenticación, la gestión de datos y las notificaciones de alertas.

- **Plugins**:

  - Los plugins extienden las funcionalidades de Grafana, y pueden ser desarrollados por la comunidad o por el equipo oficial de Grafana.


---
# Módulo 3: Despliegue y Configuración de Prometheus y Grafana en Minikube

### Objetivo

Desplegar y configurar Prometheus y Grafana en un clúster de Minikube para monitorear una aplicación Laravel y una base de datos MySQL.

### Contenidos
Instalación de Prometheus y Grafana usando Helm.
Configuración de Prometheus y Grafana.
Creación de dashboards en Grafana para visualizar métricas.

## Despliegue de Prometheus y Grafana en Minikube
Prometheus y Grafana son herramientas de código abierto ampliamente utilizadas para el monitoreo y la visualización de métricas. Este módulo proporciona una guía detallada para su despliegue y configuración en un clúster de Minikube.

## Requisitos Previos
1. Minikube instalado y en ejecución (Guía de instalación).
2. Kubectl instalado (Guía de instalación).
3. Helm instalado (Guía de instalación).

## Paso 1: Instalación de [Kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack)
Prometheus se puede instalar fácilmente en Kubernetes usando Helm. Helm es un gestor de paquetes para Kubernetes que facilita el despliegue de aplicaciones.



1. **Añadir el repositorio de Helm de Kube-prometheus-stack**

2. **Desplegar Kube-prometheus-stack usando Helm**

3. **Verificar el despliegue de Kube-prometheus-stack**

4. **Acceder a la interfaz web de Prometheus**

    - Para acceder a la interfaz web de Prometheus, realiza un port-forward del servicio de Prometheus


4. **Acceder a la interfaz web de Grafana**:

    - Para acceder a la interfaz web de Prometheus, realiza un port-forward del servicio de Grafana



## Paso 2: Creación de Dashboards en Grafana

1. **Crear un nuevo dashboard**:

  - Ve a Dashboards > New Dashboard.
  - Haz clic en Add new panel.

2. **Configurar el panel**:

  - Selecciona Prometheus como la fuente de datos.

  - Ingresa una consulta de PromQL para las métricas que deseas visualizar. Ejemplo:

  ```promql
  rate(http_requests_total[5m])
  ```
  - Configura las opciones de visualización según tus preferencias.

3. **Guardar el dashboard**:

  - Haz clic en Apply para guardar el panel.
  - Haz clic en Save dashboard para guardar el dashboard completo.
  - Asigna un nombre descriptivo al dashboard.

## Paso 3: Despliegue de la Aplicación Laravel y MySQL en Kubernetes
Para completar el entorno de monitoreo, desplegaremos una aplicación Laravel y una base de datos MySQL en el clúster de Minikube.

1. **Despliegue de MySQL**:

  - Crea un archivo mysql-deployment.yaml:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
spec:
  selector:
    matchLabels:
      app: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: mysql:5.7
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: password
        ports:
        - containerPort: 3306
          name: mysql
---
apiVersion: v1
kind: Service
metadata:
  name: mysql
spec:
  ports:
  - port: 3306
  selector:
    app: mysql
```

2. **Aplica la configuración**:

```sh
kubectl apply -f mysql-deployment.yaml
```

3. **Despliegue de Laravel**:

  - Crea un Dockerfile para Laravel:

  ```dockerfile
  FROM php:7.4-fpm
  RUN docker-php-ext-install pdo pdo_mysql
  WORKDIR /var/www
  COPY . /var/www
  CMD php artisan serve --host=0.0.0.0 --port=8000
  ```

 - Construye y sube la imagen de Docker a un registro (Docker Hub por ejemplo):

```sh
docker build -t <your-dockerhub-username>/laravel-app .
docker push <your-dockerhub-username>/laravel-app
```

- Crea un archivo laravel-deployment.yaml:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: laravel
spec:
  selector:
    matchLabels:
      app: laravel
  template:
    metadata:
      labels:
        app: laravel
    spec:
      containers:
      - name: laravel
        image: <your-dockerhub-username>/laravel-app
        ports:
        - containerPort: 8000
        env:
        - name: DB_HOST
          value: mysql
        - name: DB_DATABASE
          value: laravel
        - name: DB_USERNAME
          value: root
        - name: DB_PASSWORD
          value: password
---
apiVersion: v1
kind: Service
metadata:
  name: laravel
spec:
  ports:
  - port: 8000
  selector:
    app: laravel
```

  - Aplica la configuración:

```sh
kubectl apply -f laravel-deployment.yaml
```

3. Exposición del Servicio Laravel:

  - Crea un archivo laravel-ingress.yaml:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: laravel-ingress
spec:
  rules:
  - host: laravel.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: laravel
            port:
              number: 8000
```

  - Aplica la configuración:

```sh
kubectl apply -f laravel-ingress.yaml
```

  - Añade una entrada en tu archivo hosts para laravel.local:

```sh
echo "$(minikube ip) laravel.local" | sudo tee -a /etc/hosts
```

### Recursos Adicionales
- [Documentación de Prometheus](https://prometheus.io/docs/introduction/overview/)
- [Documentación de Grafana]( https://grafana.com/docs/grafana/latest/introduction/)
- [Guía de Helm](https://helm.sh/docs/intro/install/)
- [Guía de Minikube](https://minikube.sigs.k8s.io/docs/start/)


Evaluación del Módulo
Actividades de Evaluación:
Cuestionarios: Evaluaciones teóricas sobre los conceptos y funcionalidades de Prometheus y Grafana.
Prácticas: Implementación práctica de la configuración de Prometheus y Grafana en Minikube.
Análisis de Casos: Creación de dashboards y configuración de alertas en Grafana utilizando datos de Prometheus.
Conclusión
Al finalizar este módulo, los estudiantes habrán adquirido habilidades prácticas y teóricas en la configuración y gestión de Prometheus y Grafana en un entorno Kubernetes usando Minikube. Estas habilidades son esenciales para monitorear y mantener sistemas distribuidos de manera efectiva.

---

# Módulo 4: Creación de Alertas en Grafana
### Objetivo
Configurar alertas en Grafana para monitorear el rendimiento del sistema y recibir notificaciones proactivas sobre problemas potenciales.

### Contenidos
- Introducción a las alertas en Grafana.
- Configuración de canales de notificación.
- Creación de alertas en paneles de Grafana.

## Introducción a las Alertas en Grafana
Grafana permite configurar alertas basadas en las métricas que visualiza. Estas alertas pueden ser configuradas para monitorear diversas métricas y enviar notificaciones cuando se cumplan ciertas condiciones.

### Características de las Alertas en Grafana:

1. **Condiciones de Alerta**: Define las condiciones bajo las cuales se disparará una alerta.
2. **Canales de Notificación**: Define los medios a través de los cuales se enviarán las notificaciones (correo electrónico, Slack, PagerDuty, etc.).
3. **Grupos de Alerta**: Permite agrupar varias alertas para facilitar la gestión.
4. **Silenciamiento de Alertas**: Permite desactivar temporalmente las alertas para evitar notificaciones innecesarias durante periodos de mantenimiento.

## Configuración de Canales de Notificación
Antes de crear alertas, es necesario configurar los canales de notificación a través de los cuales recibirás las alertas.

1. **Accede a la Configuración de Grafana**:

  - Inicia sesión en tu instancia de Grafana.
  - Ve a la sección de Alerting > Notification channels.

2. **Añadir un Nuevo Canal de Notificación**:

  - Haz clic en Add channel.
  - Configura los detalles del canal de notificación según tus preferencias. A continuación se muestran algunos ejemplos comunes:

    **Ejemplo de Configuración de Email**:

    - Name: Email Notifications
    - Type: Email
    - Addresses: tuemail@example.com
    - Configura las opciones adicionales según tus necesidades.
    - Haz clic en Send Test para verificar la configuración.
    - Haz clic en Save para guardar el canal de notificación.

    **Ejemplo de Configuración de Slack**:

    - Name: Slack Notifications
    - Type: Slack
    - Url: Tu Webhook URL de Slack
    - Configura las opciones adicionales según tus necesidades.
    - Haz clic en Send Test para verificar la configuración.
    - Haz clic en Save para guardar el canal de notificación.

3. **Verificar los Canales de Notificación**:

 - Después de configurar los canales de notificación, asegúrate de que todos funcionen correctamente enviando pruebas de notificación.

## Creación de Alertas en Paneles de Grafana

1. **Accede al Dashboard de Grafana**:

  - Ve al dashboard donde deseas añadir una alerta.
  - Selecciona el panel que deseas monitorear.

2. **Editar el Panel y Configurar la Alerta**:

  - Haz clic en el título del panel y selecciona **Edit**.
  - Ve a la pestaña **Alert**.
  - Haz clic en **Create Alert**.

3. **Configurar las Condiciones de la Alerta**:

  - Define las condiciones bajo las cuales se disparará la alerta.
  - **Ejemplo de Condición**:
    - **Query**: A (PromQL query to monitor the metric)
    - **Condition**: WHEN avg() OF query (A, 5m, now) IS ABOVE 10
  - Configura las opciones adicionales como la duración y el intervalo de evaluación.

4. **Configurar las Notificaciones**:

  - Selecciona los canales de notificación configurados previamente.
  - **Ejemplo**:
    - **Notification**: Slack Notifications, Email Notifications

5. Guardar la Configuración del Panel:

  - Haz clic en **Apply** para aplicar la configuración de la alerta.
  - Haz clic en **Save dashboard** para guardar el dashboard completo.

## Ejemplo Completo de Creación de Alerta en Grafana
Supongamos que queremos crear una alerta para monitorear la tasa de solicitudes HTTP (**'http_requests_total'**) en nuestra aplicación.

1. **Añadir el Panel de Métrica**:

  - Ve a Dashboards > New Dashboard.
  - Añade un nuevo panel y selecciona Prometheus como fuente de datos.
  - Configura la métrica que deseas visualizar:

```promql
rate(http_requests_total[5m])
```

2. **Crear y Configurar la Alerta**:

  - En el panel, ve a la pestaña **Alert**.
  - Haz clic en **Create Alert**.
  - Define la condición de alerta:

```sh
WHEN avg() OF query (A, 5m, now) IS ABOVE 10
```

  - Configura el canal de notificación:
    - Selecciona Slack **Notifications y Email Notifications**.

3. **Guardar la Configuración**:

  - Haz clic en **Apply** para aplicar la configuración de la alerta.
  - Guarda el dashboard con un nombre descriptivo.

### Recursos Adicionales
- [Documentación de Prometheus](https://prometheus.io/docs/introduction/overview/)
- [Documentación de Grafana]( https://grafana.com/docs/grafana/latest/introduction/)
- [Guía de Helm](https://helm.sh/docs/intro/install/)
- [Guía de Minikube](https://minikube.sigs.k8s.io/docs/start/)


Evaluación del Módulo
Actividades de Evaluación:
Cuestionarios: Evaluaciones teóricas sobre los conceptos y funcionalidades de las alertas en Grafana.
Prácticas: Implementación práctica de la configuración de alertas en Grafana.
Análisis de Casos: Creación y prueba de alertas en Grafana utilizando datos de Prometheus.
Conclusión
Al finalizar este módulo, los estudiantes habrán adquirido habilidades prácticas y teóricas en la configuración de alertas en Grafana. Estas habilidades son esenciales para monitorear de manera proactiva el rendimiento del sistema y recibir notificaciones oportunas sobre problemas potenciales.

---

# Módulo 5: Análisis de Métricas y Alertas en Grafana
### Objetivo
Analizar métricas y responder a alertas usando Grafana para identificar problemas y optimizar el rendimiento del sistema.

### Contenidos
- Visualización de métricas en dashboards.
- Análisis de datos y toma de decisiones.
- Respuesta a alertas y acciones correctivas.

## Visualización de Métricas en Dashboards
Grafana proporciona una plataforma intuitiva para visualizar y analizar métricas a través de dashboards interactivos. Los dashboards en Grafana permiten a los usuarios monitorear el rendimiento del sistema en tiempo real y detectar anomalías de manera eficiente.

### Creación y Personalización de Dashboards

1. **Acceso a Grafana**:

  - Abre tu navegador y navega a la interfaz de Grafana (http://localhost:3000).
  - Inicia sesión con tus credenciales de administrador.

2. **Creación de un Nuevo Dashboard**:

  Ve a Dashboards > New Dashboard.
  Haz clic en Add new panel para comenzar a agregar paneles al dashboard.

3. **Configuración de Paneles**:

  - Selecciona la fuente de datos (por ejemplo, Prometheus).

  - Escribe una consulta PromQL para las métricas que deseas visualizar. Ejemplo:

```promql
rate(http_requests_total[5m])
```

  - Personaliza la visualización del panel (tipo de gráfico, leyendas, ejes, etc.).

4. Guardar el Dashboard:

  - Haz clic en Save dashboard.
  - Asigna un nombre descriptivo al dashboard.

## Análisis de Datos
Grafana facilita el análisis de métricas a través de diversas funcionalidades como consultas avanzadas, visualizaciones interactivas y filtros.

### Utilización de PromQL para Consultas Avanzadas
PromQL es el lenguaje de consultas de Prometheus que permite seleccionar y agregar datos de series temporales en tiempo real. A continuación, se presentan algunas consultas comunes y su propósito:

- **Tasa de Solicitudes HTTP**:

```promql
rate(http_requests_total[1m])
```
Esta consulta devuelve la tasa de solicitudes HTTP por segundo.

- **Uso de CPU Promedio**:

```promql
avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) by (instance)
```
Esta consulta devuelve el uso promedio de CPU por instancia.

- **Uso de Memoria Promedio**:

```promql
avg(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100
```
Esta consulta devuelve el uso promedio de memoria como un porcentaje.

### Aplicación de Filtros y Variables
Los filtros y variables en Grafana permiten personalizar las visualizaciones y analizar métricas específicas:

1. **Crear Variables**:

  - Ve a Dashboard settings > Variables > New.
  - Configura la variable según tus necesidades (por ejemplo, una lista de instancias).

2. **Utilizar Variables en Paneles**:

  - Usa las variables creadas en tus consultas PromQL para filtrar datos dinámicamente.
  
  Ejemplo:

  ```promql
  rate(http_requests_total{instance=~"$instance"}[5m])
  ```
### Visualización de Métricas con Paneles Interactivos
Grafana ofrece diversos tipos de paneles para visualizar datos de manera efectiva:

- **Gráfico de Líneas**: Ideal para mostrar tendencias a lo largo del tiempo.
- **Gráfico de Barras**: Útil para comparar valores entre diferentes categorías.
- **Panel de Estadísticas**: Proporciona una vista rápida de los valores clave.
- **Mapa de Calor**: Muestra la densidad de eventos a lo largo del tiempo.

## Respuesta a Alertas
Responder a alertas de manera oportuna es crucial para mantener la disponibilidad y el rendimiento del sistema.

### Gestión de Alertas en Grafana

1. **Visualización de Alertas Activas**:

  - Ve a **Alerting** > **Alert rules**.
  - Aquí puedes ver una lista de todas las alertas configuradas y su estado actual.

2. **Silenciamiento de Alertas**:

  - Si necesitas realizar mantenimiento o si una alerta está causando demasiadas notificaciones, puedes silenciarla temporalmente.
  - Ve a **Alerting** > **Silences** > **New Silence**.
  - Configura la alerta para silenciarla por un periodo específico.

3. **Análisis de Alertas y Respuesta**:

  - Al recibir una alerta, analiza el dashboard correspondiente para identificar la causa raíz.
  - Toma acciones correctivas según sea necesario (por ejemplo, ajustar la capacidad del sistema, investigar errores específicos).

### Notificaciones y Escalación
Configurar notificaciones adecuadas y escalaciones ayuda a garantizar que las alertas críticas sean atendidas de manera oportuna.

1. **Configuración de Canales de Notificación**:

  - Ve a Alerting > Notification channels.
  - Configura los canales de notificación según tus necesidades (correo electrónico, Slack, PagerDuty, etc.).

2. **Políticas de Escalación**:

  - Define políticas de escalación para asegurarte de que las alertas críticas sean atendidas si no se resuelven en un tiempo determinado.

## Ejemplo Completo de Análisis de Métricas y Respuesta a Alertas en Grafana
1. **Crear un Dashboard para Monitorear Solicitudes HTTP**:

  - Ve a Dashboards > New Dashboard.
  - Añade un panel con la consulta:

```promql
rate(http_requests_total[5m])
```
  - Personaliza el panel y guarda el dashboard.

2. **Configurar una Alerta para Tasa Alta de Solicitudes**:

  - En el panel, ve a la pestaña Alert.
  - Haz clic en Create Alert.
  - Configura la condición de alerta:

```sh
WHEN avg() OF query (A, 5m, now) IS ABOVE 100
```
  - Configura los canales de notificación (por ejemplo, Slack, Email).
  - Guarda la configuración y aplica los cambios.

3. **Responder a una Alerta Activa**:

  - Al recibir una notificación de alerta, ve al dashboard correspondiente.
  - Analiza las métricas y verifica las posibles causas del aumento en la tasa de solicitudes.
  - Toma acciones correctivas (por ejemplo, aumentar la capacidad del servidor, revisar el código para posibles errores).

### Recursos Adicionales

- [Grafana Dashboards Documentation](https://grafana.com/docs/grafana/latest/dashboards/)
- [Prometheus PromQL Documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- [PromQL Examples](https://logz.io/blog/promql-examples-introduction/)
- [Grafana Alerts Documentation](https://grafana.com/docs/grafana/latest/alerting/)



Evaluación del Módulo
Actividades de Evaluación:
Cuestionarios: Evaluaciones teóricas sobre los conceptos y funcionalidades de análisis de métricas y gestión de alertas en Grafana.
Prácticas: Implementación práctica de dashboards y alertas en Grafana.
Análisis de Casos: Respuesta a alertas y análisis de métricas en escenarios simulados.
Conclusión
Al finalizar este módulo, los estudiantes habrán adquirido habilidades prácticas y teóricas en el análisis de métricas y la respuesta a alertas usando Grafana. Estas habilidades son esenciales para monitorear y mantener sistemas distribuidos de manera efectiva, asegurando así un rendimiento y disponibilidad óptimos.