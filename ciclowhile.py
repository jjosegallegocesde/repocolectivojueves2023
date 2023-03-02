controlador=5
while controlador<10:
    print ("Estoy saltando")
    controlador=controlador+1


controlador1=100
print("***EMPANADAS")
print("1.agrega el sabor")
print("2.ver el sabor")
print("3.Salir")
while controlador1!=0:
    controlador1=int(input("Digita una opcion: "))
    if(controlador1==1):
        sabor=input("que sabor quieres: ")
    elif (controlador1==2):
        print(f"el sabor es {sabor}")
    elif (controlador1==3): 
        print("opcion 3")
    else :
        print ("Opcion invalida")


