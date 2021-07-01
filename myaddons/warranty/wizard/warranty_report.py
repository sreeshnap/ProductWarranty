from odoo import models, fields, api


class SampleReportPrint(models.AbstractModel):
    _name = 'report.warranty.print_reports_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        active_model = self.env.context.get('active_model')
        docs = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))

        query = """
                  SELECT row_number() over(ORDER BY warranty_data.invoice_id) as sl_no,
                  product.name as product_id,lot.name as lot_id,customer.name as customer_id
                  from warranty_request as warranty_data LEFT JOIN product_template as product 
                  on product.id = warranty_data.product_id LEFT JOIN res_partner as customer 
                  on customer.id = warranty_data.customer_id LEFT JOIN stock_production_lot as lot
                  on lot.id = warranty_data.lot_id;
                """
        if data['product_id'] and data['date']:
            query = """
                              SELECT row_number() over(ORDER BY warranty_data.invoice_id) as sl_no,
                              product.name as product_id,lot.name as lot_id,customer.name as customer_id
                              from warranty_request as warranty_data LEFT JOIN product_template as product 
                              on product.id = warranty_data.product_id LEFT JOIN res_partner as customer 
                              on customer.id = warranty_data.customer_id LEFT JOIN stock_production_lot as lot
                              on lot.id = warranty_data.lot_id
                              WHERE warranty_data.product_id=""" + str(data['product_id']) + """"""

        cr = self._cr
        cr.execute(query)
        fetched_data = cr.dictfetchall()
        return {
            'product_id': data['product_id'],
            'doc_ids': self.ids,
            'doc_model': active_model,
            'docs': docs,
            'fetched_data': fetched_data
        }
