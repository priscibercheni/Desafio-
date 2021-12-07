def menu():
    print('------MENU------')
    print('1.- Crear contacto')
    print('2.- Busqueda en agenda')
    print('3.- Editar contacto')
    print('4.- Mostrar contactos')
    print('5.- Salir')
    print()
 
def menu2():
    print('a.- Busqueda por nombre')
    print('b.- Busqueda por telefono')
    
 
def menu3():
    print("Editar contacto")
    print('1.- Eliminar un contacto')
    print('2.- Editar un contacto')
 
agenda = {'Nicole':'3621234', 'Flavio':'3627894', 'Jose':'36249874', 'Sofi':'3625698', 'Vero':'3625216'}
telefonos = {}
nombres = {}
opcionmenu = 0
menu()


for x in range(10):
    opcionmenu = int(input("Inserta un numero para elegir una opcion: "))
    
    if opcionmenu == 1:
        print("Agregar Nombre, telefono")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        telefonos[nombre] = telefono
        nombres[telefono] = nombre
        agenda[nombre]=telefono
        menu()
 
    elif opcionmenu == 2:
        print("Busqueda")
        menu2()
        opcionmenu2 = input("Inserta una letra para elegir una opcion: ")
        if opcionmenu2=="a":
             nombre = input("Nombre: ")
        if nombre in telefonos:
            print("El telefono es", telefonos[nombre])
        else:
            print(nombre, "no se encuentra")
 
        if opcionmenu2=="b":
            telefono = input("Telefono: ")
        if telefono in nombres:
            print("El Nombre es", nombres[telefono])
        else:
            print(telefono, "no se encuentra")
 
        
    elif opcionmenu == 3:
        menu3()
        opcionmenu3 = input("Inserta un numero para elegir una opcion: ")
        if opcionmenu3=="1":
            nombre=input("Nombre: ")
            if nombre not in telefonos:
                print ("No encontrado")
            else:
                del telefonos[nombre]
                print("El telefono se ha borrado correctamente")
                
        elif opcionmenu3=="2":
            nombre = input("Nombre: ")
            telefono=int(input("Telefono: "))
            telefonos[nombre]=telefono
            print("El telefono se ha modificado")
        else:
            print(nombre, "no encontrado")
 
    elif opcionmenu == 4:
            print("\nContactos: ",agenda)
            menu()
 
 
    elif opcionmenu != 5:
        menu()