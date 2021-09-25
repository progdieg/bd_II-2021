class Persona():
    def __init__(self):
        self.__perso={}
        self.__listaPersona=[]
    
    def agregarPersona(self,ced,nom,ape,dir,tel):
        self.__perso={
            "Cedula":ced,
            "nombre":nom,
            "Apellido":ape,
            "dir":dir,
            "tel":tel,
        }
        self.__listaPersona.append(self.__perso)

    def mostrarPersona(self):
        print(self.__listaPersona)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
    def mostrarEmpleado(self):
        super().mostrarPersona()

    

def ingresarDatos():
    p1=Persona()
    e1=Empleado()
    cont=True
    while (cont):
        ced=int(input("Cedula:  "))
        nom=input("nombre:  ")
        ape=input("Apellido:  ")
        dir=input("Direccion:  ")
        tel=int(input("Telefono:  "))
        p1.agregarPersona(ced,nom,ape,dir,tel)
        op=input("Desea continuar s/n?")
        op=op.lower()

        if op =="s":
            cont=True
        else: 
            cont=False
    p1.mostrarPersona()
    e1.mostrarEmpleado()

def inicio():
    ingresarDatos()

    


if __name__ == "__main__":
    inicio()