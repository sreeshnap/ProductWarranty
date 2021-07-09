from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_percentage = fields.Boolean(string="Discount Percentage", default=False)
    discount_enable = fields.Boolean(string="Discount Enable")

    @api.onchange('discount_percentage')
    def _default_product_discount(self):
        if self.discount_percentage:
            self.discount_enable = True
        else:
            self.discount_enable = False
