from odoo import models, fields, api


class ProductWarrantyWizard(models.TransientModel):
    _name = "warranty.report.wizard"

    product_name_id = fields.Many2one('product.product', string="Product Name")
    date = fields.Date(string="Date")

    def print_report(self):
        # pass
        data = {
            'model': 'warranty.report.wizard',
            'form': self.read()[0]
        }
        print("Data", data)
        return self.env.ref('warranty.print_reports_pdf').report_action(self, data=data)
