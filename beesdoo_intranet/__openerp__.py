# -*- coding: utf-8 -*-
{
    'name': "Beesdoo Intranet Module",

    'summary': """
        Intranet for the members so they can see their balance,
        list of purchases, ... """,

    'description': """
        
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['beesdoo_base', 'beesdoo_product' ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/intranet.xml'
    ],
}