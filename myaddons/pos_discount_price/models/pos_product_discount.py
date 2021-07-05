from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'product.template'

    discount = fields.Selection(
        [
           ("invalid", "Invalid"),
           ("discount", "Discount"),
        ],
        string="Discount",
        default="discount",
    )



