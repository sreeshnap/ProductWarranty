from odoo import api, fields, models

class AllowedProductInherit(models.Model):
    _inherit = 'res.partner'


    allowed_products_ids = fields.Many2many('product.template', domain="[('is_published', '=', True)]")


    # website_available_product_ids = fields.Many2many('product.template', string='Available Product',
    #                                                  domain="[('is_published', '=', True)]")
    # website_available_cat_ids = fields.Many2many('product.public.category', string='Available Product Categories')


class WebsiteGuestVisibility(models.TransientModel):
    _inherit = 'res.config.settings'

    available_product_ids = fields.Many2many('product.template', string='Available Product',
                                             domain="[('is_published', '=', True)]")

