{
    'name': 'Website Visibility',
    'version': '1.0',
    'category': 'Website/Website',
    'sequence': 6,
    'summary': 'Product Visibility In Website ',
    'description': """

This module allows the cashier to quickly give percentage-based
discount to a customer.

""",
    'depends': ['base', 'website_sale', 'product', 'contacts'],
    'data': [
        'views/allowed_products_customer.xml',
        'views/buy_now_button.xml',
        # 'views/user_login_allowed_products.xml',
    ],
    'qweb': [

    ],
    'installable': True,
}