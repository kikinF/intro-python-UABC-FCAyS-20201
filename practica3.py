class Mesa:  

  nombre = "Desconocido"
  ID = "Desconocido"
  color = "Desconocido"
  altura = 0
  forma = "Desconocido"
  material = "Desconocido"
  
  
  def pararse(self):
    print("Estar de pie")
  
  def sostener(self):
    print("Sostiene algo en su superficie")
  
  def cortar(self, cosa):
    print("corta algo con la sierra" + cosa)
    
  def doblarse(self):
    print("se ha doblado la mesa")
    
  def cambiarMaterial(self, materialMesa):
    self.material = materialMesa
    print("material: " + materialMesa)

valle = Mesa()
valle.cortar("cortando una tabla")

valle.cambiarMaterial("acero")
print(valle.material)

#Ejemplo de clase
  
#class Estudiante:
#  edad = 0
#  carrera = "Desconocida"
#  universidad = "Desconocida"
#  genero = "Femenino"

##definimos una funcion para festejar 

#  def festejar(self):
#   print("Festejando")

#  def estudiar(self, materia):
#   print("Estudiando", materia)

#  def llorar(self):
#   print("llorando")
  
#  def dormir(self):
#   print("Z, Z, Z, Z,...")  

##ajustamos la edad

#  def cambiarEdad(self, edadAlumno):
#   self.edad = edadAlumno
#   print("nueva edad ", edadAlumno)

##generamos un nuevo estudiante

#miguel = Estudiante()
#miguel.estudiar("Logica para la programacion")

##imprimimos atributo del objeto

#miguel.cambiarEdad(21)
#print(miguel.edad)