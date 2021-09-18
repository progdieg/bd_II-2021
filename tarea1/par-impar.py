# def capturarNombre():
#     nombre=input("Nombre de empleado")
#     print(nombre)


# def main():
#     capturarNombre()


# if __name__ == "__main__":
#     main()

def parImpar():
    numero= int(input("ingrese un numero ==>"))
    if numero%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")

#numero perfecto 

def perfecto():
    input("lista de numeros perfectos o imperfectos")
    ent=int(input())
    for i in range(2, ent+1):
        b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        print("%s es perfecto" %i)
    else:
        print("%s no es perfecto" %i)

def main():
    parImpar()

def segundo():
    perfecto()


if __name__ == "__main__":
    main()
    segundo()


    