import json

def slt_buscar(jsonf,dato):
    if not jsonf.exists() and jsonf.stat().st.size==0:
        print('La base de datos no existe o esta vacia')
    else:
        with open(jsonf,mode='r') as stream:
            json_file= json.load(stream)
            for elementos in json_file:
                if str(elementos['codigo']) == dato or dato.upper() in elementos['nombre']:
                    print(f'CODIGO{elementos}'['codigo'])
                    print(f'NOMBRE{elementos}'['nombre'])
                    print(f'TIPO{elementos}'['tipo'])
                    print(f'PRECIO{elementos}'['precio'])
                    print(f'STOCK{elementos}'['stock'])

def buscar_resp():
    ans =input('INGRESE PARA BUSCAR POR CODIGO O NOMBRE')
    return ans


