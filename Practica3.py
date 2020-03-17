#Ejemplo de clase
  
class Estudiante:
  edad = 0
  carrera = "Desconocida"
  universidad = "Desconocida"
  genero = "Femenino"
  
  #equivalente a constructor en java the hut
  def _init_(self, edad, carrrera):
    self.edad = edad #paso de parametro de constructor
    self.carrera = carrera
    
#definimos una funcion para festejar 

  def festejar(self):
   print("Festejando")

  def estudiar(self, materia):
   print("Estudiando", materia)

  def llorar(self):
   print("llorando")
  
  def dormir(self):
   print("Z, Z, Z, Z,...")  

#ajustamos la edad

  def cambiarEdad(self, edadAlumno):
   self.edad = edadAlumno
   print("nueva edad ", edadAlumno)

#generamos un nuevo estudiante

#miguel = Estudiante()
miguel = Estudiante(32, "Logica para la programacion")
miguel.estudiar("Logica para la programacion")

#imprimimos atributo del objeto

miguel.cambiarEdad(38)
print(miguel.edad)

#hey little sister what have you done
#ti tiri tiri ti tiri
#hey little sister whats your superman
