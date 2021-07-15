from odoo import api, fields, models


class AllowedProductInherit(models.Model):
    _inherit = 'res.partner'

    allowed_products_id = fields.Many2one(string="Allowed Products")