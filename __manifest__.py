{
    "name": "Gastos personales",
    "version": "1.0",
    "sequence": -1,
    "depends": ["base", "sale"],
    "author": "AMS",
    "category": "Service",
    "application": True,
    "license": "LGPL-3",
    "description": """
    Módulo para llevar el control de mis gastos así como mis ingresos
    """,

    "data": [
        "security/ir.model.access.csv",
        # "views/groups.xml",
        "views/control_gastos.xml",
        "views/menus.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # "tablero_laboratorio/static/src/components/*/*.js",
            # "tablero_laboratorio/static/src/components/*/*.xml",
            # "tablero_laboratorio/static/src/components/*/*.scss",
            
        ]
    }
}