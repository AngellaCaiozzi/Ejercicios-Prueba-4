import FuncionesMatricula as fc

opcion = ''
usuarios = {}
cupos_ninos = 25
cupos_adulto = 25

while opcion != '4':
    opcion = fc.menu()
    if opcion == '4':
        print('Programa Terminado.')
    elif opcion == '1':
        print('Matricular Nuevo Usuario')
        usuarios, cupos_ninos, cupos_adulto = fc.matricular(usuarios, cupos_ninos, cupos_adulto)  
        print(usuarios)  
    elif opcion == '2':
        print('Cancelar Matrícula.')
        usuarios, cupos_ninos, cupos_adulto = fc.cancelar_matricula(usuarios, cupos_ninos, cupos_adulto)
        print(usuarios)
    elif opcion == '3':
        print('Cupos disponibles.') 
        fc.mostrar_cupos(cupos_ninos, cupos_adulto)  
    else:
        print('Error. Opción no existe. ')     
