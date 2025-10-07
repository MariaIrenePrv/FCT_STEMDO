# Ejercicio 04
En este ejercicio creo el deployment, listo el pod y el deployment, elimino el deployment y vuelvo a listar el pod para comprobar la correcta eliminación. 


## Crear DEPLOYMENT
Creo el depoyment de forma imperativa, la estructura es la misma simplemente cambiamos pod por deployment.
```powershell
kubectl create deployment demogato --image=tomcat 
```

<img src="../../auxiliar/ej4.png">

## Listar POD 
Listo de manera más detallada. 
```powershell
kubectl get pods -o wide
```
<img src="../../auxiliar/ej4.1.png">


## Listar DEPLOYMENT

```powershell
kubectl get deployments
```
<img src="../../auxiliar/ej4.2.png">


## Eliminar DEPLOYMENT
Al eliminar el deployment lo compruebo listando el deployment aunque en el siguiente ejercicio liste el pod, me gusta siempre realizar todas las comprobaciones necesarias. 

```powershell
 kubectl delete deployment demogato
```
<img src="../../auxiliar/ej4.3.png">

## Listar POD 

<img src="../../auxiliar/ej4.4.png">