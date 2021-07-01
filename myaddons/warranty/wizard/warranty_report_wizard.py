from odoo import models, fields, api


class ProductWarrantyWizard(models.TransientModel):
    _name = "warranty.report.wizard"

    product_id = fields.Many2one('product.product', string="Product Name")
    date = fields.Date(string="Date")

    def print_report(self):
        # print("kkk-->", self.read()[0])
        # pass
        data = {
            'model': self._name,
            'ids': self.ids,
            'product_id': self.product_id.id,
            'date' : self.date
            # 'form': self.read()[0],
        }
        return self.env.ref("warranty.report_warranty_request").report_action(self, data=data)
