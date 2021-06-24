from odoo import models, fields, api

class ProductWarrantyWizard(models.TransientModel):
    _name = "warranty.report.wizard"

    product_name = fields.Many2one()