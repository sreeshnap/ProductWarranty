{
    'name': "Warranty Calculation",
    'version': '14.0.1.0.0',
    'summary': """Module deals with product warranty""",
    'description': """Product Warranty""",
    'live_test_url': 'https://youtu.be/5GwbWciCJDw',
    'category': 'Uncategorized',
    'website': "https://www.openhrms.com",
    'depends': ['base', 'sale', 'account', 'purchase_stock', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'view/view.xml',
        'data/sequence.xml',
        'view/produ.xml',
        'security/security.xml',
        'data/warranty_location_data.xml',
        'view/invo.xml',
        # 'view/sale_addmenu.xml',
        # 'view/stock_move.xml',
        'wizard/warranty_report_wizard_view.xml',
        'reports/report_pdf.xml',
        'reports/report_template.xml',

    ],
    'demo': [],
    'license': "AGPL-3",

}
