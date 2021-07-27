from odoo import api, fields, models

class AllowedProductInherit(models.Model):
    _inherit = 'res.partner'
    # _name = 'allowed.product'

    filter_mode = fields.Selection([('null', 'No Filter'), ('product_only', 'Product Wise'),
                                    ('categ_only', 'Category Wise')], string='Filter Mode', default='null')
    website_available_product_ids = fields.Many2many('product.template', string='Available Product',
                                                     domain="[('is_published', '=', True)]")
    website_available_cat_ids = fields.Many2many('product.public.category', string='Available Product Categories')

    @api.onchange("filter_mode")
    def onchange_filter_mod(self):
        if self.filter_mode == 'null':
            self.website_available_cat_ids = None
            self.website_available_product_ids = None



