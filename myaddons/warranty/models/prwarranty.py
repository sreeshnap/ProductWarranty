from datetime import datetime, timedelta
from odoo import models, fields, api


class WarrantyProblem(models.Model):
    _name = "warranty.request"
    _description = "Warranty Request"

    invoice_ids = fields.Many2one('account.move', string="Invoice")
    customer_name = fields.Char(string="Customer Name", related='invoice_ids.partner_id.name')
    product = fields.Many2one(string="Product Name", related='invoice_ids.invoice_line_ids.product_id')
    lot_number = fields.Many2one(string="Lot Number", related='product.stock_move_ids.move_line_ids.lot_id')
    purchase_date = fields.Date(string="Invoice Date", related='invoice_ids.invoice_date')
    date_order = fields.Date(string="Date")

    state = fields.Selection([('draft', 'Draft'), ('to approve', 'To approve'), ('approved', 'Approved'),
                              ('cancel', 'Cancel')],
                             default='draft', string="Status")

    name = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'warranty.service') or 'New'
        result = super(WarrantyProblem, self).create(vals)
        return result

    warranty_updation = fields.Date(string="Warranty Expiry", compute='_compute_warranty_end')

    @api.depends('invoice_ids')
    def _compute_warranty_end(self):
        start_date = self.purchase_date
        end_date = self.product.warranty_updated
        date_warranty = start_date
        if self.product.has_warranty:
            date_warranty = start_date + timedelta(days=end_date)
        self.warranty_updation = date_warranty


    is_warranty_product = fields.Boolean(string="Warranty Product", default=False)

    @api.onchange('warranty_updation')
    def warranty_updation_check(self):
        if self.warranty_updation:
            self.is_warranty_product = False
        else:
            self.is_warranty_product = True

