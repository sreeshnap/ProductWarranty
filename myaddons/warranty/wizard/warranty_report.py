from odoo import models, fields, api

class SampleReportPrint(models.AbstractModel):
    _name = 'report.warranty.request.print_sample_report'

    @api.model
    def _get_report_values(self, docids, data):
        """in this function can access the data returned from the button
        click function"""
        model_id = data['sale.order']
        value = [1]
        query = """SELECT *
                        FROM sale_order as so
                        JOIN sale_order_line AS Sl No ON so.id = sl.sale_order_id
                        WHERE Sl No.id = %s"""
        value.append(model_id)
        self._cr.execute(query, value)
        record = self._cr.dictfetchall()
        return {
            'docs': record,
        }
        # query = """
        #             SELECT row_number() over(ORDER BY ) as Sl No,
        #             Product Name as product_id,Lot as lot_id,Customer Name as customer_id,
        #
        #         """