
{
    'name': 'Point of Sale Discounts Price',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Simple Discounts in the Point of Sale ',
    'description': """

This module allows the cashier to quickly give percentage-based
discount to a customer.

""",
    'depends': ['base', 'point_of_sale', 'product'],
    'data': [

        'views/pos_confi_inherit.xml',
        'views/pos_product_discount.xml',
        'views/template.xml',
    ],
    'qweb': [

        'static/src/xml/discount_receipt.xml',
        'static/src/xml/discount_price_tag.xml',
        'static/src/xml/action_button.xml',
    ],
    'installable': True,
}
