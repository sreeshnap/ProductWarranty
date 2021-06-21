{
    'name': "Warranty Calculation",
    'version': '14.0.1.0.0',
    'summary': """Module deals with product warranty""",
    'description': """Product Warranty""",
    'live_test_url': 'https://youtu.be/5GwbWciCJDw',
    'category': 'Uncategorized',
    'website': "https://www.openhrms.com",
    'depends': ['base', 'sale', 'account', 'purchase_stock'],
    'data': [
        'security/ir.model.access.csv',
        'view/view.xml',
        'data/sequence.xml',
        'view/produ.xml',
        'security/security.xml',
        # 'data/warranty_data.xml',
        # 'view/invo.xml',
    ],
    'demo': [],
    'license': "AGPL-3",

}
