"""
* Desarrolla una clase para modelar triangulos
* Los attibutos de la clase seran los lados del triangulo
* crea un metodo constructor para inicializar los attributos.
* Crea ademas los siguientes metodos:
    - metodo que imprime el valor del lado  de mayor tamaño
    - metodo que imprime el tipo de triangulo  que es 
    (equilatero, isoceles y escanleno)
* crear un metodo que devuelva al valor de los attributos 
de los triangulos
* instancia de dos triangulos diferentes e invoca  a sus metodos
"""

from traceback import print_tb


class triangulos:
    def __init__(self, L1, L2, L3):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        
    def ladomayor(self):
        if self.L1 > self.L2:
            if self.L1 > self.L3:                
                print(f"lado L1 mayor {self.L1}")
            else:
                print(f"lado L3 mayor {self.L3}")
        elif self.L2 > self.L3:
            print(f"lado L2 mayor {self.L2}")    
        else:
            print(f"lado L3 mayor {self.L3}")
    
    def tipoTriangulo(self):
        if self.L1 == self.L2 and self.L1 == self.L3:
            print ("Triangulo equilatero")
        elif self.L1 == self.L2 and self.L1 != self.L3 and self.L2 != self.L3:
            print("Triangulo isoceles")
        elif self.L1 != self.L2 and self.L1 != self.L3 and self.L2 != self.L3:
            print("Triangulo Escaleno")
        else:
            print("Triangulo diferente")
    
    def devolverAttributos(self):
        return self.L1, self.L2, self.L3    

        
T1 = triangulos(15,10,10) # la variable lado envia los valores a la clase triangulos
T1.ladomayor()
T1.tipoTriangulo()
_T1 = T1.devolverAttributos()
print(_T1)

T2 = triangulos(10,10,15)
T2.ladomayor()
T2.tipoTriangulo()
_T2 = T2.devolverAttributos()
print(_T2)

