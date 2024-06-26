from pathlib import Path
home=Path(__file__).parent.parent
rutaj=Path(home/'base.json')
rutac=Path(home/'exportar.csv')



menup=['VER LISTADO',
        'BUSCAR PINTURA',
        'AGREGAR PNTURA',
        'ELIMINAR PINTURA',
        'EXPORTAR PITURA',
        'SALIR']