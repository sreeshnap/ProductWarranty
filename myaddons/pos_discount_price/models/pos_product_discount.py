from odoo import api, fields, models


class PosDiscount(models.Model):
    _inherit = 'product.template'

    discount = fields.Integer(string="Discount")



