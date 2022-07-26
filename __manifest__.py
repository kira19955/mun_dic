# -*- coding: utf-8 -*-
{
    'name': "mun_dic",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Luis Antonio Cruz Gutierrez",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'directorio_municipal'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/secuencias.xml',
        'views/views.xml',
        'views/templates.xml',
        #'views/catalogos.xml',
        'views/menus.xml',
        'report/recepcion_de_equipo.xml',
        'report/centro_de_servicios.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'true',
}
