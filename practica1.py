#Codigo que solicita una variable
nombre = input("como te llamas?")
print("hola " + nombre)

edad = input("Cuantos años tienes?")
x = int(edad)
if x < 18:
  print("Eres menor de edad")
if x >= 18:
  print("Eres mayor de edad")

print("Buen dia!")