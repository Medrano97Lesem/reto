def suma(a,b):
    if a % 1 == 0 and b % 1 == 0:
      print (f'la suma de los numeros es: {a+b} SW')
    
    else :
     print('Ambos parametros deben ser numeros enteros')
     
a = input("Ingrese el primer numero: ")
b = input("ingrese el segundo numero: ")
try:
  A = float(a)
  B = float(b)
  suma(A,B)

except ValueError:
  if a.isalpha():
    print(f'A es un string: {a}')
    print("Ambos numeros tienen que ser enteros")
  elif b.isalpha():
    print(f'b es un string: {b}')
    print("Ambos numeros tienen que ser enteros")
  else:
    print("el tipo de dato ingresado es incorrecto")
    print("Ambos numeros tienen que ser enteros")