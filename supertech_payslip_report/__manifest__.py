# -*- coding: utf-8 -*-
{
    'name': "Payslip Report",

    'summary': """ Payslip Report Design For SuperTech
        """,

    'description': """
        
    """,

    'author': "Odoo India",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll'],

    # always loaded
    'data': [
        'report/report_payslip_templates.xml',
        'report/hr_payroll_report.xml',
    ],
}
