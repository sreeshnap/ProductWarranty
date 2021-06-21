from datetime import datetime, timedelta
from odoo import models, fields, api


class ProductWarranty(models.Model):
    _name = "warranty.request"
    _description = "Warranty Request"

    invoice_id = fields.Many2one('account.move', string="Invoice")
    customer_id = fields.Many2one(string="Customer Name", related='invoice_id.partner_id')
    #product_id = fields.Many2one('product.product', string="Product Name", domain="[('id', '=', invoice_id.invoice_line_ids.product_id)]")
    product_id = fields.Many2one(string="Product Name", related='invoice_id.invoice_line_ids.product_id')
    lot_id = fields.Many2one(string="Lot Number", related='product_id.stock_move_ids.move_line_ids.lot_id')
    invoice_date = fields.Date(string="Invoice Date", related='invoice_id.invoice_date')
    request_date = fields.Date(string="Date")

    state = fields.Selection([('draft', 'Draft'), ('to approve', 'To approve'), ('approved', 'Approved'),
                              ('cancel', 'Cancel')],
                             default='draft', string="Status")

    name = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')

    warranty_expiry = fields.Date(string="Warranty Expiry", compute='_compute_warranty_expiry')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'warranty.service') or 'New'
        result = super(ProductWarranty, self).create(vals)
        return result


    @api.depends('invoice_id')
    def _compute_warranty_expiry(self):
        start_date = self.invoice_date
        end_date = self.product_id.warranty_duration
        warranty_date = start_date
        if self.product_id.has_warranty:
            warranty_date = start_date + timedelta(days=end_date)
        self.warranty_expiry = warranty_date

    def action_approve(self):
        self.state = 'approved'

    def action_submit(self):
        self.state = 'to approve'

    def action_moves(self):
         # pass
        return {
            'name': 'Form',
            'res_id': self.product_id.stock.view_move_form,
            'view_type': 'form',
            'res_model': 'stock.move',
            'view_mode': 'form',
            'type': 'ir.actions.act_window'
        }



