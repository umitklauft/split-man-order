# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2019 EquickERP
#
##############################################################################
{
    'name': "Split Manufacturing Order",
    'category': "Manufacturing",
    'version': "13.0.1.0",
    'author': 'Equick ERP',
    'description': """
        This allows you to split manufacturing order.
        * Whoever user have access rights they can split manufacturing order.
        * User have different split options as like below.
         > Number of Split: It will divide quantity into selected number of split.
         > Number of Quantity: Each split MO quantity as selected number of quantity.
         > Manual Split: User have to enter the quantity for each split.
    """,
    'summary': """split mo split mrp order split manufacturing order by number of quantity split manufacturing order by number of split manufacturing order split production order split manufacturing splitting split by number of order mrp split by number of order""",
    'depends': ['base', 'mrp'],
    'price': 20,
    'currency': 'EUR',
    'license': 'OPL-1',
    'website': "",
    'data': [
        'security/security.xml',
        'views/wizard_split_mo_view.xml',
    ],
    'live_test_url': 'https://www.youtube.com/watch?v=RT7QJZ6aXUM',
    'demo': [],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: