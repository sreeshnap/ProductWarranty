
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.portal.controllers.web import Home
from odoo.http import request

from odoo import fields, http



class RelatedUserLogin(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="user", website=True)
    def shop(self, page=0, category='', search='', ppg=False, **post):
        res = super(RelatedUserLogin, self).shop(page=0, category='', search='', ppg=False, **post)
        # var = res.qcontext.get('products')
        # for rec in var:
        #     if rec.id == 9:
        #         rec.name = 'Normal Desk'
        return res

    @http.route(['/shop/product/<model("res.partner"):website_available_product_ids>'], type='http', auth="user", website=True,
                sitemap=False)
    def old_product(self, product, category='', search='', **kwargs):
        # Compatibility pre-v14
        return request.redirect(_build_url_w_params("/shop/%s" % slug(product), request.params), code=301)

    # @api.onchange('user')
    # def _onchange_products(self, category, **post):
    #     res = super(RelatedUserLogin, self)._onchange_products(categry='res.partner.product_visibility', **post)
    #     return res


