def menu():
    print('Menú Biblioteca')
    print('~~'*10)
    print("""
    1.- Matricular.
    2.- Cancelar Matrícula.
    3.- Cupos Disponibles.
    4.- Salir.""")
    op = input('Ingrese su opción: ')
    return op 

def validar_codigo_verificacion(codigoVerf):
    tieneMayusculas = any(c.isupper() for c in codigoVerf)
    tieneNro = any(c.isdigit() for c in codigoVerf)
    sinEspacios = ' ' not in codigoVerf
    return len(codigoVerf) >= 4 and tieneMayusculas and tieneNro and sinEspacios

def matricular(diccUsuarios, cuposN, cuposA):
    hayCupos = True
    if cuposN == 0 and cuposA == 0:
        print('No hay cupos disponibles para ninguna categoría.')
        hayCupos = False
        #diccUsuarios, cuposN, cuposA
    
    if hayCupos:
        while True:
            codigo = input('Ingrese un código (6 caracteres): ').strip()
            if len(codigo) == 6 and codigo not in diccUsuarios:
                break
            else:
                print('Codigo no valido o ya registrado. Intente nuevamente.')

        while True:
            nombre = input('Ingrese nombre del usuario: ').strip()
            if nombre.replace(' ','').isalpha():
                break
            else:
                print('El nombre solo debe contener letras.')
        
        while True:
            tipo = input('Ingrese tipo de usuario [N: Niños / A: Adultos]: ').upper()
            if tipo == 'N' and cuposN > 0:
                break
            elif tipo == 'A' and cuposA > 0:
                break
            else:
                print('Tipo no valido o sin cupos disponibles. Intente nuevamente.')

        while True:
            codigoVerif = input('Ingrese código de verificación: ')
            if validar_codigo_verificacion(codigoVerif):
                break
            else:
                print('Codigo no valido. Debe tener mínimo 4 caracteres, al menos 1 mayúscula, 1 número y sin espacios.')

        diccUsuarios[codigo] = [nombre, tipo, codigoVerif]        
        if tipo == 'N':
            cuposN -= 1
        else:
            cuposA -= 1
        print(f'¡Matricula registrada con éxito para {nombre}!')        
    return diccUsuarios, cuposN, cuposA
 
def cancelar_matricula(diccUsuarios, cuposN, cuposA):
    codigo = input('Ingrese el código del usuario a cancelar: ').strip()
    if codigo in diccUsuarios:
        tipo = diccUsuarios[codigo][1]
        del diccUsuarios[codigo]
        if tipo == 'N':
            cuposN += 1
        else:
            cuposA += 1
        print('Matricula cancelada correctamente.')         
    else:
        print('No existe usuario con ese código.')
    return diccUsuarios, cuposN, cuposA     

def mostrar_cupos(cuposN, cuposA):
    print(f'Hay {cuposN} cupos de niños disponibles.')
    print(f'Hay {cuposA} cupos de adultos disponibles.')