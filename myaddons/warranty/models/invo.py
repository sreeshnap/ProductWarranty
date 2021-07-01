from odoo import models, fields, api


class ProductWarranty(models.Model):

    _inherit = "account.move"

    invoice_request = fields.One2many('warranty.request', 'invoice_id')


