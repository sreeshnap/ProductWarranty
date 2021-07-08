from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'


    discount_percentage = fields.Boolean(string="Discount Percentage", default=False)