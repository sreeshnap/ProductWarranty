from odoo import models, fields, api

class InvoiceDetails(models.Model):
    _inherit = 'account.move'

    warranty_info = fields(string="Warranty Info")