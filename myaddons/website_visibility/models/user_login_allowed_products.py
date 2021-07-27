from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import fields, models, api
from ast import literal_eval


class RelatedUserLogin(WebsiteSale):
    _inherit = 'res.partner'

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="user", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(RelatedUserLogin, self).shop(page=0, category=None, search='', ppg=False, **post)
        return res

    @api.model
    def set_values(self):
        res = super(RelatedUserLogin, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('user', self.user)
        self.env['ir.config_parameter'].sudo().set_param('filter_mode', self.filter_mode)
        if not self.user:
            self.website_available_cat_ids = None
            self.website_available_product_ids = None
            self.env['ir.config_parameter'].sudo().set_param('filter_mode', 'product_only')
        if self.filter_mode == 'product_only':
            self.website_available_cat_ids = None
        elif self.filter_mode == 'categ_only':
            self.website_available_product_ids = None

        self.env['ir.config_parameter'].sudo().set_param('website_product_visibility.website_available_product_ids',
                                                         self.website_available_product_ids.ids)
        self.env['ir.config_parameter'].sudo().set_param('website_product_visibility.website_available_cat_ids',
                                                         self.website_available_cat_ids.ids)
        return res

    @api.model
    def get_values(self):
        res = super(RelatedUserLogin, self).get_values()
        product_ids = literal_eval(
            self.env['ir.config_parameter'].sudo().get_param('website_product_visibility.website_available_product_ids',
                                                             'False'))
        cat_ids = literal_eval(
            self.env['ir.config_parameter'].sudo().get_param('website_product_visibility.website_available_cat_ids', 'False'))
        mod = self.env['ir.config_parameter'].sudo().get_param('filter_mode')
        res.update(
            user=self.env['ir.config_parameter'].sudo().get_param(
                'user'),
            filter_mode=mod if mod else 'product_only',
            website_available_product_ids=[(6, 0, product_ids)],
            website_available_cat_ids=[(6, 0, cat_ids)],
        )
        return res


