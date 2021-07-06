from datetime import datetime, timedelta
from odoo import models, fields, api


class ProductWarranty(models.Model):
    _name = "warranty.request"
    _description = "Warranty Request"

    invoice_id = fields.Many2one('account.move', string="Invoice")
    customer_id = fields.Many2one(string="Customer Name", related='invoice_id.partner_id', store=True)
    # product_id = fields.Many2one('product.product', string="Product Name", domain="[('id', '=', invoice_id.invoice_line_ids.product_id)]")
    # product_id = fields.Many2one('product.product', string="Product Name",
    #                              related='invoice_id.invoice_line_ids.product_id', store=True)
    product_id = fields.Many2one('product.product', string="Product Name")
    # lot_id = fields.Many2one('stock.production.lot', string="Lot Number")
    lot_id = fields.Many2one('stock.production.lot', string="Lot Number", related='product_id.stock_move_ids.move_line_ids.lot_id', store=True)

    invoice_date = fields.Date(string="Invoice Date", related='invoice_id.invoice_date', store=True)
    request_date = fields.Date(string="Date")

    state = fields.Selection([('draft', 'Draft'), ('to approve', 'To approve'), ('approved', 'Approved'),
                              ('product received', 'Product Received'), ('done', 'Done'),
                              ('cancel', 'Cancel')],
                             default='draft', string="Status")

    name = fields.Char(string="Service Number", readonly=True, required=True, copy=False, default='New')

    warranty_expiry = fields.Date(string="Warranty Expiry", compute='_compute_warranty_expiry')
    move_id = fields.Many2one("stock.move")
    # product_tmpl_id = fields.Many2one('product.product', store=True)

    @api.onchange('invoice_id')
    def _onchange_invoice_id(self):
        domain = []
        self.product_id = False
        for line in self.invoice_id.invoice_line_ids:
            domain.append(line.product_id.id)
        return {'domain': {
            'product_id': [('id', 'in', domain)]
        }}

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
        self.invoice_id.write({
            'invoice_request_ids': [(1, 0, {
                'invoice_id': self.invoice_id,
                'customer_id': self.customer_id,
                'product_id': self.product_id,
                'lot_id': self.lot_id,
                'state': self.state
            })]
        })

    def action_approve(self):
        self.state = 'approved'

        if self.state == 'approved':
            if self.product_id.warranty_types == 'service':
                self.action_approve_warranty()
                self.state = 'product received'
            elif self.product_id.warranty_types == 'replacement':
                self.action_approve_warranty()
                self.state = 'product received'

    @api.model
    def action_approve_warranty(self):
        stock_location = self.env.ref('warranty.location_mylocation')
        customer_location = self.env.ref('stock.stock_location_customers')
        product = self.product_id
        # lot_id = self.lot_id
        qty = 1
        # print(lot_id)
        # print(lot_id.id)
        self.move_id = self.env['stock.move'].create({
            'name': 'MyLocation',
            'location_id': customer_location.id,
            'location_dest_id': stock_location.id,
            'product_id': product.id,
            # 'lot_ids': lot_id.id,
            'product_uom': product.uom_id.id,
            'product_uom_qty': qty,
        })
        print("Data", self.move_id)
        self.move_id._action_confirm()

        self.move_id.move_line_ids.write({'qty_done': qty})
        # self.move_id._action_done()
        self.move_id._action_assign()

    def action_product_moves(self):
        # pass
        return {
            'name': 'Form',
            'domain': [('product_id', '=', self.product_id.id)],
            'res_model': 'stock.move',
            'res_id': self.move_id.id,
            'view_type': 'form',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }

    def action_return(self):
        # pass
        self.state = 'done'
        self.action_return_product()

    @api.model
    def action_return_product(self):
        if self.product_id.warranty_types == 'service':
            stock_location = self.env.ref('warranty.location_mylocation')
            customer_location = self.env.ref('stock.stock_location_customers')
            product = self.product_id
            lot_id = self.lot_id
            qty = 1
            self.move_id = self.env['stock.move'].create({
                'name': 'MyLocation',
                'location_id': stock_location.id,
                'location_dest_id': customer_location.id,
                # 'lot_ids': lot_id.id,
                'product_id': product.id,
                'product_uom': product.uom_id.id,
                'product_uom_qty': qty,
            })
            print("Data", self.move_id)
            self.move_id._action_confirm()
            self.move_id.move_line_ids.write({'qty_done': qty})
            # self.move_id._action_done()
            self.move_id._action_assign()

        elif self.product_id.warranty_types == 'replacement':
            stock_location = self.env.ref('stock.stock_location_stock')
            customer_location = self.env.ref('stock.stock_location_customers')
            product = self.product_id
            lot_id = self.lot_id
            qty = 1
            self.move_id = self.env['stock.move'].create({
                'name': 'WH/Stock',
                'location_id': stock_location.id,
                'location_dest_id': customer_location.id,
                # 'lot_ids': lot_id.id,
                'product_id': product.id,
                'product_uom': product.uom_id.id,
                'product_uom_qty': qty,
            })
            print("Data", self.move_id)
            self.move_id._action_confirm()
            self.move_id.move_line_ids.write({'qty_done': qty})
            # self.move_id._action_done()
            self.move_id._action_assign()

