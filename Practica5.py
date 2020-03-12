#El siguiente algoritmo resuleve el problema
#para realizar la suma o multiplicacio de dos numeros decimales
#dependiendo su valor

a = 0
b = 0 
c = 0

a = float(input("Ingrese el primer numero"))
b = float(input("Ingrese el segundo valor"))

if (a > 0 or b > 0):
  print("suma de numeros")
  c = a + b
else:
  print("Multiplicación de numeros")
  c = a * b

print("El resultado es: " + str(c))