odoo.define('pos_discount_price.discount_receipt', function (require) {
"use strict";

var models = require('point_of_sale.models');

models.load_fields('product.product','product_discount');

var _super_order_line = models.Orderline.prototype;
models.Orderline = models.Orderline.extend({
    export_for_printing: function(){
        var line = _super_order_line.export_for_printing.apply(this,arguments)
        line.product_discount = this.get_product().product_discount;
        console.log(line.product_discount)
        return line;

    },
});
});