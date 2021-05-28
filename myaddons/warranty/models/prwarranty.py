import datetime
from odoo import models, fields, api


class WarrantyProblem(models.Model):
    _name = "warranty.request"
    _description = "Warranty Request"

    invoice_ids = fields.Many2one('account.move', string="Invoice")
    customer_name = fields.Char(string="Customer Name", related='invoice_ids.partner_id.name')
    product = fields.Many2one(string="Product Name", related='invoice_ids.invoice_line_ids.product_id')
    lot_number = fields.Many2one(string="Lot Number", related='product.stock_move_ids.move_line_ids.lot_id')
    purchase_date = fields.Date(string="Invoice Date", compute="get_purchase_date")
    date_order = fields.Datetime(string="Date", default=fields.Datetime.now)

    state = fields.Selection([('draft', 'Draft'), ('to approve', 'To approve'), ('approved', 'Approved'),
                              ('cancel', 'Cancel')],
                             default='draft', string="Status")

    #@api.depends('invoice_ids')
    #def get_lot_number(self):
    #        self.lot_number = self.invoice_ids.invoice_line_ids.product_id.purchase_order_line_ids.lot_id

    @api.depends('invoice_ids')
    def get_purchase_date(self):
        self.purchase_date = self.invoice_ids.invoice_date


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
