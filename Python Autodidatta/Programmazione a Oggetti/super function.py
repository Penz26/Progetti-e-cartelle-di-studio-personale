#super() = Funzione usata per dare accesso ai metodi un classe padre
#          ritorna un oggetto temporaneo di una classe padre quando usata

#super() va a chiamare la funzione (.__init__) della classe padre

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)  #utilizziamo super() per utilizzare il metodo __init__ della classe Padre(Rectangle)
                                        #in modo da non dover riscrivere self.length = length e self.width = width
    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height   
    

square = Square(3, 3) #noi stiamo passando 3 per length e 3 per width
cube = Cube(3, 3, 3) #qua stessa roba ma visto che il 3° parametro non esiste in __init__ di rectangle troverà allocazione in height di Cube

print(square.area())
print(cube.volume())




