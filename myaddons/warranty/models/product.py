from odoo import models, fields, api


class ProductDetails(models.Model):
    _inherit = 'product.template'
    has_warranty = fields.Boolean(string="Has Warranty", default=False)

    warranty_period = fields.Selection(
        [
            ("day", "Day(s)"),
            ("week", "Week(s)"),
            ("month", "Month(s)"),
            ("year", "Year(s)"),
        ],
        string="Warranty Period",
        default="day",
    )
    warranty_updated = fields.Integer(string="Warranty Duration")
    warranty_Types = fields.Selection(
        [
            ("service", "Service"),
            ("Replacement", "Replacement"),
        ],
        string="Warranty Types",
    )
