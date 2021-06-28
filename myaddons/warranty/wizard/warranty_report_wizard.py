from odoo import models, fields, api


class ProductWarrantyWizard(models.TransientModel):
    _name = "warranty.report.wizard"

    product_name_id = fields.Many2one('product.product', string="Product Name")
    date = fields.Date(string="Date")

    def print_report(self):
        print("kkk-->", self.read()[0])
        # pass
        data = {
            'model': 'warranty.report.wizard',
            'form': self.read()[0],
        }
        print("Data", data)
        selected_product = data['form']['product_name_id'][0]
        selected_product_name = self.env['warranty.request'].search([('product_id', '=', selected_product)])
        selected_product_name_list = []
        for app in selected_product_name:
            vals ={
                'Product_Name': app.name
            }
        data['docs'] = selected_product_name
        return self.env.ref("warranty.report_warranty_request").report_action(self, data=data)
