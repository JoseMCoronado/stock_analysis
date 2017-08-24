# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Analysis Report',
    'category': 'Inventory',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Stock Analysis report
        """,
    'depends': ['base','stock','product'],
    'data': [
        'data/ir_models.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_views.xml',
        'data/ir_actions_act_window.xml',
        'data/ir_ui_menu.xml',
        'data/ir_actions_server.xml'
    ],
    'installable': True,
    'application': True,
}
