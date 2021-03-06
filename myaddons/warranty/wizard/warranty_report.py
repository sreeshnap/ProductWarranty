from datetime import datetime
import  time

from odoo import models, fields, api


class SampleReportPrint(models.AbstractModel):
    _name = 'report.warranty.print_reports_pdf'

    @api.model
    def _get_report_values(self, docids, data=None):
        # active_model = self.env.context.get('active_model')
        # docs = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))
        # print(self.env['product.product'].search([('id', '=', 26)]).name)
        # print(self.env['warranty.request'].search([('product_id.id', '=', 26)]).product_id.name)
        if data['date']:
            date = time.mktime(datetime.strptime(data['date'], "%Y-%m-%d").timetuple())

        query = """
                  SELECT row_number() over(ORDER BY warranty.invoice_id) as sl_no,
                  template.name as product_id,lot.name as lot_id,customer.name as customer_id,template.list_price as price_id 
                  from warranty_request as warranty LEFT JOIN product_product as product 
                  on product.id = warranty.product_id  LEFT JOIN res_partner as customer 
                  on customer.id = warranty.customer_id LEFT JOIN stock_production_lot as lot
                  on lot.id = warranty.lot_id LEFT JOIN product_template as template on product.product_tmpl_id = template.id;
                """

        if data['product_id'] and data['date']:
            query = """
                              SELECT row_number() over(ORDER BY warranty.invoice_id) as sl_no,
                              template.name as product_id,lot.name as lot_id,warranty.invoice_date as date,
                              customer.name as customer_id,template.list_price as price_id
                              from warranty_request as warranty LEFT JOIN product_product as product 
                              on product.id = warranty.product_id LEFT JOIN res_partner as customer 
                              on customer.id = warranty.customer_id LEFT JOIN stock_production_lot as lot
                              on lot.id = warranty.lot_id LEFT JOIN product_template as template on 
                              product.product_tmpl_id = template.id WHERE warranty.product_id=""" + str(data['product_id']) + """ 
                              and warranty.invoice_date<=to_timestamp(""" + str(date) + """)"""


        elif data['product_id']:
            query = """
                              SELECT row_number() over(ORDER BY warranty.invoice_id) as sl_no,
                              template.name as product_id,lot.name as lot_id,customer.name as customer_id,
                              template.list_price as price_id from warranty_request as warranty 
                              LEFT JOIN product_product as product on product.id = warranty.product_id 
                              LEFT JOIN res_partner as customer on customer.id = warranty.customer_id 
                              LEFT JOIN stock_production_lot as lot
                              on lot.id = warranty.lot_id LEFT JOIN product_template as template on 
                              product.product_tmpl_id = template.id
                              WHERE warranty.product_id=""" + str(data['product_id']) + """"""

        elif data['date']:
            query = """
                              SELECT row_number() over(ORDER BY warranty.invoice_id) as sl_no,
                              template.name as product_id,lot.name as lot_id,warranty.invoice_date as date,
                              customer.name as customer_id,template.list_price as price_id
                              from warranty_request as warranty LEFT JOIN product_product as product 
                              on product.id = warranty.product_id LEFT JOIN res_partner as customer 
                              on customer.id = warranty.customer_id LEFT JOIN stock_production_lot as lot
                              on lot.id = warranty.lot_id LEFT JOIN product_template as template on 
                              product.product_tmpl_id = template.id
                              WHERE warranty.invoice_date<=to_timestamp(""" + str(date) + """)"""

        cr = self._cr
        cr.execute(query)
        fetched_data = cr.dictfetchall()
        return {
            'product_id': data['product_id'],
            'doc_ids': self.ids,
            # 'doc_model': active_model,
            # 'docs': docs,
            'fetched_data': fetched_data
        }
