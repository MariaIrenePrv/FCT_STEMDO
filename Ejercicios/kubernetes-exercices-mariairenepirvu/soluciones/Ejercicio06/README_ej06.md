# Ejercicio 06
Utilizo 3 métodos diferentes para modificar las réplicas:
* Utilizando el comando **edit**
* Utilizando el comando **scale** 
* Editándolo manualmente y aplicando los cambios 

## Comando Edit
Edito el archivo con el comando que se muestra a continuación, guardo el archivo y lo listo para observar el cámbio. 
```powershell
kubectl edit deploy demogat-yaml
```
<img src="../../auxiliar/ej6.1.png">
<img src="../../auxiliar/ej6.png">

### Listo los pods 

```powershell
kubectl get pods
```
<img src="../../auxiliar/ej6.2.png">


## Comando Scale
Utilizando el comando **scale** aumento a las réplicas deseadas. 
```powershell
kubectl scale deploy demogat-yaml --replicas=4
kubectl get pods
```
<img src="../../auxiliar/ej6.3.png">

## Edición manual 
Abro el documento de forma manual o por comandos, modifico las réplicas y aplico los cambios. 
```powershell
kubectl apply -f deployment05.yaml
kubectl get pods
```
<img src="../../auxiliar/ej6.5.png">


## Eliminar DEPLOYMENT

 ```powershell 
 kubectl delete deployment demogat-yaml
 ```

 <img src="../../auxiliar/ej6.4.png">