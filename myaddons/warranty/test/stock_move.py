from odoo.exceptions import UserError
from odoo.tests import Form

from odoo.tests.common import SavepointCase

class StockMove(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(StockMove, cls).setUpClass()
        cls.stock_location = cls.env.ref('stock.location_mylocation')
        cls.supplier_location = cls.env.ref('stock.stock_location_suppliers')
        cls.uom_unit = cls.env.ref('uom.product_uom_unit')
        cls.uom_dozen = cls.env.ref('uom.product_uom_dozen')
        cls.product = cls.env['product.product'].create({
            'name': 'Product A',
            'type': 'product',
            # 'categ_id': cls.env.ref('product.product_category_all').id,
            'categ_id': cls.env.ref('invoice_id.invoice_line_ids.product_id').id,
        })
        # cls.product = cls.env.ref('invoice_id.invoice_line_ids.product_id')

    def gather_relevant(self, product_id, location_id, lot_id=None, strict=False):
        quants = self.env['stock.quant']._gather(product_id, location_id, lot_id=lot_id,  strict=strict)
        return quants.filtered(lambda q: not (q.quantity == 0 and q.reserved_quantity == 0))

    def test_in_1(self):
        """ Receive products from a customer/supplier. Check that a move line is created and that the
        reception correctly increase a single quant in stock.
        """
        # creation
        move1 = self.env['stock.move'].create({
            'name': 'test_in_1',
            'location_id': self.supplier_location.id,
            'location_dest_id': self.stock_location.id,
            'product_id': self.product.id,
            'product_uom': self.uom_unit.id,
            'product_uom_qty': 100.0,
        })
        self.assertEqual(move1.state, 'draft')

        # confirmation
        move1._action_confirm()
        self.assertEqual(move1.state, 'assigned')
        self.assertEqual(len(move1.move_line_ids), 1)

        # fill the move line
        move_line = move1.move_line_ids[0]
        self.assertEqual(move_line.product_qty, 100.0)
        self.assertEqual(move_line.qty_done, 0.0)
        move_line.qty_done = 100.0

        # validation
        move1._action_done()
        self.assertEqual(move1.state, 'done')
        # no quants are created in the supplier location
        self.assertEqual(self.env['stock.quant']._get_available_quantity(self.product, self.supplier_location), 0.0)
        self.assertEqual(self.env['stock.quant']._get_available_quantity(self.product, self.supplier_location, allow_negative=True), -100.0)
        self.assertEqual(self.env['stock.quant']._get_available_quantity(self.product, self.stock_location), 100.0)
        self.assertEqual(len(self.gather_relevant(self.product, self.supplier_location)), 1.0)
        self.assertEqual(len(self.gather_relevant(self.product, self.stock_location)), 1.0)


