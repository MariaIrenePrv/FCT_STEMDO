# Ejercicio 01
Después de instalar minikube y kubectl comienzo con la ejecución de los ejercicios. 
Empezamos por lo básico, creación de pods, listado, descripción y eliminación. Los comandos los encuentro en la documentación oficial (kubernetes.io). 

## Crear POD
Creo un POD llamado **apache**, con la imagen **httpd** y de **forma imperativa**. 
```powershell
kubectl run apache --image=httpd
```
<img src="../../auxiliar/ej1.png">

## Listar POD
```powershell
kubectl get pods
```
<img src="../../auxiliar/ej1.1.png">


## Describir POD
Con este comando obtengo las propiedades del pod. 
```powershell
kubectl describe pod apache 
```
<img src="../../auxiliar/ej1.2.png">
<img src="../../auxiliar/ej1.3.png">

## Eliminar POD
```powershell
kubectl delete pod apache 
```
<img src="../../auxiliar/ej1.4.png">