odoo.define('pos_discount_price.discount', function(require) {
"use strict";

var models = require('point_of_sale.models');
models.load_fields('product.template', 'discount_price');

var _super_order_line = models.Orderline.prototype;
models.Orderline = models.Orderline.extend({
    export_for_printing: function(){
        var line = _super_order_line.export_for_printing.apply(this,arguments)
        line.discount_price = this.get_product().discount_price;
        return line;

    },
});
});