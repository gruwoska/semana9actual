class Cola:
     def __init__(self):
         self.cola =[]
     def añadir(self,nombre):
          var=self.cola
          var.append(nombre)
     def sacar(self):
          n = self.cola.pop(0)
          print("Saliendo {}".format(n))
     def salida(self):
          print(self.cola)   
