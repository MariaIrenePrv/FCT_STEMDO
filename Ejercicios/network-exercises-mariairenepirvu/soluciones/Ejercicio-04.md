# Ejercicio 4 - Subnetting

## Fórmulas Subnetting
Este es un resumen de las fórmulas que he utilizado para los tres ejercicios. 

#### 1. Hosts por subred
```plaintext
Hosts = 2^n - 2

n= Número de bits para hosts
Se restan 2 porque uno está reservado para la dirección de red y otro para broadcast
```
#### 2. Subredes posibles 
```plaintext
Subredes = 2^n

n= Número de bits para crear subredes 
```
#### 3. Tamaño de cada subred  
```plaintext
Tamaño de subred = 2^n

n= Número de bits disponibles para hosts
```
#### 4. Nueva máscara a partir del número de subredes necesarias 
```plaintext
2^n ≥ número de subredes necesarias
Nueva máscara = máscara original + n
```
#### 5. Nueva máscara a partir del número de hosts necesarios 
```plaintext
2^n - 2 ≥ número de hosts necesarios
Nueva máscara = 32 - n
```

#### 6. Número de subredes posibles entre dos máscaras
```plaintext
Subredes posibles = 2^(máscara nueva - máscara original)
```

#### 7. Número de direcciones totales en una red 
```plaintext
Direcciones totales = 2^(32 - máscara)
```



## Tarea
1. Tienes la red 10.0.0.0/8 y necesitas dividirla en subredes que soporten 1000 hosts cada una. ¿Cuantas subredes puedes crear?.

```plaintext
-> Bits necesarios para los 1000 hosts
2^n -2 ≥ 1000
n=10 porque 2^10= 1024 ||  1024 > 1000

-> Bits de la red para crear subredes
Máscara original = /8
Bits para hosts = 10

Los bits para la red son 32 - 8 - 10 = 14 bits 

-> Número de subredes 
Subredes = 2^
n= Número de bits de la red para las subredes

Subredes = 2^14 = 16384 

```
**Puedo Crear 16.384 subredes**

2. Tienes la red 172.16.0.0/16. Necesitas crear 20 subredes con el máximo número posible de hosts por subred. ¿Cuantos hosts caben en cada subred?.

```plaintext 
-> Bits necesarios para crear al menos 20 subredes
2^n ≥ 20
n = 5 porque 2^5 = 32 || 32 > 20

-> Bits para hosts en cada subred
Máscara original = /16 
Nuevos bits para subredes = 5

La nueva máscara es /16 + 5 = /21

-> Cálculo de los hosts por subred
Bits para hosts = 32 - 21 = 11 bits

Número de hosts = 2^11 - 2 = 2048 - 2 = 2046 hosts
```
**En cada subred caben 2046 hosts**


2. Tienes la red 192.168.1.0/24. Debes dividirla en subredes que puedan soportar 6 hosts **utilizables** cada una. ¿Cuantas subredes se pueden crear con esa condición?.

```plaintext
-> Bits necesarios para 6 hosts utilizables
2^n - 2 ≥ 6
2^3 - 2 = 8 - 2 = 6  ||  3 bits son suficientes para 6 hosts

-> Bits para crear subredes
Máscara original = /24 
Bits para hosts = 3
Los bits para subredes = 32 - 24 - 3 = 5 bits

-> Cálculo de subredes posibles
Subredes = 2^5 = 32 subredes
```

**Se pueden crear 32 subredes**