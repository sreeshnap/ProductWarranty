odoo.define('pos_discount_price.discount_price_tag', function(require) {
"use strict";

var models = require('point_of_sale.models');
//console.log("models", models)
models.load_fields('product.product','product_discount');

//var _super_products_widget = models.ProductsWidget.prototype;
//models.ProductsWidget = models.ProductsWidget.extend({
//    export_for_printing: function() {
//        var line = _super_products_widget.export_for_printing.apply(this,arguments);
//        line.product_discount= this.get_product().product_discount;
//        console.log(line.product_discount)
//        return line;
//    },
//});

});