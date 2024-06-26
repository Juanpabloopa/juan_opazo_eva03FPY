import json

def eliminar(jsonf,dato):
    if not jsonf.exits():
        print('no existe este archivo')
    if jsonf.stat().st_size==0:
        print('El archivo esta vacio')
    else:
        with open(jsonf,mode='r') as stream:
            json_file= json.load(stream)
            for elementos in json_file:
                if elementos['codigo'] and elementos['nombre']:
                    elementos.remove
            with open(jsonf,mode='w') as cffile:
                json_file= json.dumps(cffile)
            print('elemento borrado con exito')


def resp_eliminar():
    ans=input('escriba codigo o nombre de la persona a eliminar')
    return ans

