sw = 1
listaSuper = []
valorSuper = []

print('1. Ingresar los productos del súper.')
print('2. Salir')
op = int(input('Slecciones una opción: '))
if op == 1:
    while sw == 1:
        try:
            producto = input('Agregue el producto, para salir, presione 0:\n')
            if producto != 0:
                listaSuper.append(producto)
                valorProducto = int(input(f'Incorpore el valor del {producto}: '))
                valorSuper.append(valorProducto)
                print('----------DETALLE BOLETA----------')
                print('La lista del super es: ')
                for producto in listaSuper:
                    print(producto)
                print(f'La cantidad de articulos son: {len(listaSuper)}')    
                print(f'Tiene un total de: {sum(valorSuper)}')
            else:
                print('Adiós!')     
                sw = 0
        except:
            print('INGRESO ERRÓNEO.')  
else:
    print('Adiós!')                     