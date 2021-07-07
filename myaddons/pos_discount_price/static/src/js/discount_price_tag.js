odoo.define('pos_discount_price.discount', function(require) {
"use strict";

var models = require('point_of_sale.ProductsWidget');
//console.log("models", models)
models.load_fields('product.template','discount');
//
//var _super_products_widget = models.ProductsWidget.prototype;
//models.ProductsWidget = models.ProductsWidget.extend({
//    export_for_printing: function() {
//        var line = _super_products_widget.export_for_printing.apply(this,arguments);
//        line.discount= this.get_product().discount;
//        return line;
//    },
//});
//

});