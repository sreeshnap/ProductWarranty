from odoo import api, fields, models


class PosDiscount(models.Model):
    _inherit = 'product.template'

    product_discount = fields.Integer(string="Discount")
