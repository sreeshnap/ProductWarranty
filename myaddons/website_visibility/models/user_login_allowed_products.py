from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale


class RelatedUserLogin(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="user", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(RelatedUserLogin, self).shop(page=0, category=None, search='', ppg=False, **post)
        return res
