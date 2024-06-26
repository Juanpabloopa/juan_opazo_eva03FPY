import os
import json

def agregar(jsonf):
    if not jsonf.exists():
        jsonf.touch()
        print('el archivo no existia , pero acaba de ser credo')
    if jsonf.stat().st_size==0:
        json_file=[]
        codp=380560
    else:
        with open(jsonf,mode='r') as stream:
            json_file=json.load(stream)
            for elementos in json_file:
                codp=[]
                codp.append(elementos['codigo'])
            codp= max(codp)+1
    while True:
        print('Seleciona el color de la pintura\n')
        nombre=input('COLOR:\n').upper()
        ans=input(f'Es correcto esto{nombre}\n1.SI\n2.NO\n')
        if ans == '1':
            break
        else:
            os.system('cls')
    while True:
        print('seleiona el tio de pintura')
        tipo= input(f'1.ACRILICO\n2.LATEX\n')
        if ans== '1':
            break
        if ans == '2':
            break
        else:
            os.system('cls')
            print('opcion no valida')
    while True:
        print('Ingresa el valor del producto')
        valor=input('VALOR:\n')
        ans=input(f'Esto es correcto{valor}')
        if ans == '1'and valor.isnumeric():
            valor=int(valor)
            break
        else:
            os.system('cls')
            print('Solo se aceptan caracter numericos')
    while True:
        print('Ingresa el valor del producto')
        stock=input('STOCK:\n')
        ans= input(f'Esto es correcto{stock}\n1.si\n2.no\n')
        if ans == '1' and stock.isnumeric():
            stock= int(stock)
            break
        else:
            os.system('cls')
            print('Solo se aceptan caracteres numericos\n')
    data={codp:'CODIGO',
          nombre:'NOMBRE',
          tipo:'TIPO',
          valor:'VALOR',
          stock:'STOCK'}
    json_file.apped(data)
    with open(jsonf,mode='w') as stream:
        json_file= json.dumps(json_file,stream)
    print('PRODUCTO AGREGADO CORRECTAMENTE:)')