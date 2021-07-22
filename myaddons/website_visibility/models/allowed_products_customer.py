from odoo import api, fields, models

class AllowedProductInherit(models.Model):
    _inherit = 'res.partner'

    allowed_products_ids = fields.One2many('customer.product', 'product_id', 'same_vat_partner_id')


class AllowedProduct(models.Model):
    _name = 'customer.product'

    product_id = fields.Many2one('product.product')
    same_vat_partner_id = fields.Many2one('res.partner')


    # @api.depends('same_vat_partner_id')
    # def _compute_product_id(self):
    #     self.allowed_products.write({
    #         'allowed_products_ids': [(1, 0, {
    #             'product_id': self.product_id,
    #         })]
    #     })

