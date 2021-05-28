import datetime
from odoo import models, fields,api


class WarrantyProblem(models.Model):
    _name = "warranty.request"
    _description = "Warranty Request"

    invoice_ids = fields.Many2one('account.move', string="Invoice")
    customer_name = fields.Char(string="Customer Name", related='invoice_ids.partner_id.name')
    product = fields.Many2one(string="Product Name", related='invoice_ids.invoice_line_ids.product_id')
    lot_number = fields.Integer(string="Lot Number")
    purchase_date = fields.Date(string="Invoice Date", compute="get_purchase_date")
    date_order = fields.Datetime(string="Date", default=fields.Datetime.now)

    # @api.depends('invoice_ids')
    # def get_product(self):
    #  self.product = self.invoice_ids.product_id
    # return self.invoice_ids.product_id

    @api.depends('invoice_ids')
    def get_purchase_date(self):
        self.purchase_date = self.invoice_ids.invoice_date
        return self.invoice_ids.invoice_date

    name = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'warranty.service') or 'New'
        result = super(WarrantyProblem, self).create(vals)
        return result


    warranty_updation = fields.Integer(string="Warranty Duration")
    warranty_method = fields.Selection(
        [
            ("service", "Service"),
            ("Replacement", "Replacement"),
        ],
        string="Warranty Method",
    )

    warranty_type = fields.Selection(
        [
            ("day", "Day(s)"),
            ("week", "Week(s)"),
            ("month", "Month(s)"),
            ("year", "Year(s)"),
        ],
        string="Warranty Type",
        required=True,
        default="day",
    )