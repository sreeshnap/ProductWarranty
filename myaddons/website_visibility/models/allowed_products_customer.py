from odoo import api, fields, models


class AllowedProductInherit(models.Model):
    _inherit = 'res.partner'

    allowed_products_ids = fields.One2many('product.product', 'product_tmpl_id')

    # @api.onchange('partner_id')
    # def _onchange_product_id(self):
    #     self.product_tmpl_id.write({
    #         'allowed_products_ids': [(1, 0, {
    #             'product_tmpl_id': self.product_templ_id,
    #         })]
    #     })

