
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.portal.controllers.web import Home
from odoo.http import request
from ast import literal_eval

from odoo import models, api, fields, http



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
        # var = res.qcontext.get('res')
        # print(res)
        return res


        # var = request.env['website'].sudo.search[('user_ids.id')]
        # var = fields.Char("User ID", default=lambda self: self.env.user.name)

        # current_user = fields.Many2one('res.users', 'current user', default=lambda self: self.env.user.id)
        # approved_by = fields.Many2one('res.users', 'approved by', default=lambda self: self.env.user)
        # console.log('approved_by')



    # @http.route(['/shop/product/<model("res.partner"):website_available_product_ids>'], type='http', auth="user", website=True,
    #             sitemap=False)
    # def old_product(self, product, category='', search='', **kwargs):
    #     # Compatibility pre-v14
    #     return request.redirect(_build_url_w_params("/shop/%s" % slug(product), request.params), code=301)

    # @api.onchange('user')
    # def _onchange_products(self, category, **post):
    #     res = super(RelatedUserLogin, self)._onchange_products(categry='res.partner.product_visibility', **post)
    #     return res


    @api.onchange('user')
    def _onchange_user(self):
        search_ids = self.search(cr, [('create_uid', '=', uid)])
        for id in search_ids:
            self.write(cr,uid,[id],{'current':'true'})

