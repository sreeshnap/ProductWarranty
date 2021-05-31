from odoo import models, fields, api


class ProductDetails(models.Model):
    _inherit = 'product.template'
    has_warranty = fields.Boolean(string="Has Warranty", default=False)
    is_show_warranty = fields.Boolean(string="is_show_warranty")

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
    warranty_types = fields.Selection(
        [
            ("service", "Service"),
            ("replacement", "Replacement"),
        ],
        string="Warranty Types",
    )

    @api.onchange('has_warranty')
    def warranty_checked(self):
        if self.has_warranty:
            self.is_show_warranty = True
        else:
            self.is_show_warranty = False
