from datetime import datetime, timedelta
from odoo import models, fields, api


class ProductWarranty(models.Model):
    _name = "warranty.request"
    _description = "Warranty Request"

    invoice_id = fields.Many2one('account.move', string="Invoice")
    customer_id = fields.Many2one(string="Customer Name", related='invoice_id.partner_id')
    # product_id = fields.Many2one('product.product', string="Product Name", domain="[('id', '=', invoice_id.invoice_line_ids.product_id)]")
    product_id = fields.Many2one('product.product', string="Product Name",
                                 related='invoice_id.invoice_line_ids.product_id')
    # product_id = fields.Many2one('product.product', string="Product Name")
    lot_id = fields.Many2one(string="Lot Number", related='product_id.stock_move_ids.move_line_ids.lot_id')
    invoice_date = fields.Date(string="Invoice Date", related='invoice_id.invoice_date')
    request_date = fields.Date(string="Date")

    state = fields.Selection([('draft', 'Draft'), ('to approve', 'To approve'), ('approved', 'Approved'),
                              ('product received', 'Product Received'), ('done', 'Done'),
                              ('cancel', 'Cancel')],
                             default='draft', string="Status")

    name = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')

    warranty_expiry = fields.Date(string="Warranty Expiry", compute='_compute_warranty_expiry')

    move_id = fields.Many2one("stock.move")

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

    def action_submit(self):
        self.state = 'to approve'

    def action_approve(self):
        self.state = 'approved'
        # if self.state == 'approved':
        #     action_return_product()


    @api.model
    def action_return_product(self):
        # stock_location = self.env.ref('stock.stock_location_stock')
        stock_location = self.env.ref('stock.location_mylocation')
        customer_location = self.env.ref('stock.stock_location_customer')
        # uom_unit = self.env.ref('uom.product_uom_unit')
        # uom_dozen = self.env.ref('uom.product_uom_dozen')
        product = self.env.ref('invoice_id.invoice_line_ids.product_id')
        move = self.env['stock.move'].create({
            'name': 'Use on MyLocation',
            'location_id': customer_location.id,
            'location_dest_id': stock_location.id,
            'product_id': product.id,
            'product_uom': product.uom_id.id,
            'product_uom_qty': 1,
        })
        move._action_confirm()
        move._action_assign()
        move.move_line_ids.write({'qty_done': 1})
        move._action_done()


    def action_product_moves(self):
        # pass
        return {
            'name': 'Form',
            'res_model': 'stock.move',
            'res_id': self.move_id.id,
            'view_type': 'form',
            'view_mode': 'form',
            'type': 'ir.actions.act_window'
        }

    def action_return(self):
        pass
# self.state = 'product received'
