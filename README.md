# Reto
implementar una función `sumarNumeros(a, b)`
## Descripcion 
El usuario ingresa los parámetros `a y b `

````python

a = input("Ingrese el primer numero: ")
b = input("ingrese el segundo numero: ")

````

Verifique que ambos parámetros `a y b `sean números enteros.
```python
def suma(a,b):
    if a % 1 == 0 and b % 1 == 0: ## Verifica si el numero ingresado es entero
      print (f'la suma de los numeros es: {a+b} SW')
    
    else :
     print('Ambos parametros deben ser numeros enteros')
```

Si alguno de los parámetros no es un número entero, la función debe retornar el mensaje: "Ambos parámetros deben ser números enteros.".
```python
 else :
     print('Ambos parametros deben ser numeros enteros')
```
Si ambos parámetros son válidos, debe sumar los dos números y retornar un string con el siguiente formato: 

"El resultado de la suma es: Resultado SW", donde Resultado es la suma de a y b y "SW" son las iniciales.

