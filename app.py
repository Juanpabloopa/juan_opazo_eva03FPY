from modules.crear import mapa_resp,mapa
from modules.data import menup,rutaj,rutac
from  modules.buscar import slt_buscar,buscar_resp
from modules.agregar import agregar
from modules.eliminar import eliminar, resp_eliminar
from modules.exportar import exportar
import os


while True:
    mapa(menup)
    ans = mapa_resp()
    if ans == '1':
        pass
    elif ans=='2':
        slt_buscar(buscar_resp(rutaj))
    elif ans== '3':
        agregar(menup)
    elif ans == '4':
        eliminar(resp_eliminar(rutaj))
    elif ans == '5':
        exportar(rutac)
    elif ans == '6':
        exit('ADIOHH')
    else:
        print('ERROR, opcion no valida, vuelve a intentarlo')
