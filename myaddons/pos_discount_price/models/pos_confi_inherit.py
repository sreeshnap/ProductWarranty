from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_percentage = fields.Boolean(string="Discount Percentage", default=False)
    percentage = fields.Integer(string="Percentage")
    discount_product_id = fields.Many2one('product.product', string='Discount Product', domain="[('sale_ok', '=', True)]")





