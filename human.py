class Human:
    def __init__(self, nombre, edad):
        self.edad = edad
        self.nombre = nombre
        print 'El nombre es: ' + self.nombre, 'y su edad es: ' + str(self.edad)

    def multiplyAge(self):
        print ('La edad multiplicada por 3 es: ' + str(self.edad * 3))
        
