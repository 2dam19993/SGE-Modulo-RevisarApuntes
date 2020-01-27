# -*- coding: utf-8 -*-
{
    'name': "VerificacionesDeProductos",

    'summary': """
        Gestiona las revisiones de los apuntes guardando los comentarios y
        los profesionales que lo hayan revisado.""",

    'description': """
        Se guarda la información de todos los apuntes y todas la revisiones que
        contengan cada uno de estos. Cada revisión consta de un comentario correspondiente
        de un profesional especificado en una materia y un nivel. Además, cada revisión
        guarda una fecha, ya que un mismo profesional puede repetir la revisión de
        un mismo apunte.
    """,

    'author': "2DAM2CURIOUS",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/apunte.xml',
        'views/profesional.xml',
        'views/apunte_report.xml',
        'views/nivel.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/nivel.xml'
    ],
}
