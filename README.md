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
```python
  print (f'la suma de los numeros es: {a+b} SW')
```
Casos válidos (números enteros)
```
Entrada	Salida esperada
a = 5, b = 3	El resultado de la suma es: 8 SW
a = -10, b = 4	El resultado de la suma es: -6 SW
a = 0, b = 0	El resultado de la suma es: 0 SW
a = 123, b = 877	El resultado de la suma es: 1000 SW
```
Casos inválidos (no enteros)
```

Entrada	Salida esperada	Motivo del error
a = 5.5, b = 2	"Ambos parámetros deben ser números enteros."	a es un número decimal
a = "10", b = 5	"Ambos parámetros deben ser números enteros."	a es string
a = 8, b = nil (null)	"Ambos parámetros deben ser números enteros."	b no es un número
a = true, b = 3	"Ambos parámetros deben ser números enteros."	a es booleano
a = [], b = {}	"Ambos parámetros deben ser números enteros."	Ambos son tipos incorrectos

```
Se utilizo excepciones en prython
```python

except ValueError:
  if a.isalpha(): # Verifica si el parámetro a es un string 
    print(f'A es un string: {a}')
    print("Ambos numeros tienen que ser enteros")
  elif b.isalpha():
    print(f'b es un string: {b}') # Verifica si el parámetro b es un string 
    print("Ambos numeros tienen que ser enteros")
  else: # De lo contrario cualquier parámetro ingresado que no sea un numero sera marcado como incorrecto 
    print("el tipo de dato ingresado es incorrecto")
    print("Ambos numeros tienen que ser enteros")
```

