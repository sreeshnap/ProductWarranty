from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'product.template'

    discount = fields.Integer(string="Discount")



