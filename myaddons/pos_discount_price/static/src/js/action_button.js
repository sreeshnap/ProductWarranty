odoo.define('pos_custom_buttons.DiscountButton', function(require) {
'use strict';
   const { Gui } = require('point_of_sale.Gui');
   const PosComponent = require('point_of_sale.PosComponent');
   const ProductScreen = require('point_of_sale.ProductScreen');
   const { useListener } = require('web.custom_hooks');
   const Registries = require('point_of_sale.Registries');

   class CustomDiscountButtons extends ProductScreen {
       constructor() {
           super(...arguments);
           useListener('click', this.onClick);
       }
       is_available() {
           const order = this.env.pos.get_order();
           return order
       }
       async onClick() {
                var self = this;
            const { confirmed, payload } = await this.showPopup('TextInputPopup',{
                title: this.env._t('Discount Percentage'),
                startingValue: this.env.pos.config.percentage,
            });
             if (confirmed) {
                const val = Math.round(Math.max(0,Math.min(100,parseFloat(payload))));
                console.log(val)
                await self.apply_discount(val);
            }
       }
         async apply_discount(val) {
            var order    = this.env.pos.get_order();
            var lines    = order.get_orderlines();
            var product  = this.env.pos.db.get_product_by_id(this.env.pos.config.discount_product_id);
            var price = order.get_total_with_tax();
//                console.log(order.get_total_with_tax())
            var discount = - val / 100.0 * price;
                console.log(discount)

            if( discount < 0 ){
                var total_with_tax = order.get_total_with_tax()+discount;
                console.log(total_with_tax)
            }
                return;
                }


//            var i = 0;
//            while ( i < lines.length ) {
//                if (lines[i].get_product() === product) {
//                    order.remove_orderline(lines[i]);
//                } else {
//                    i++;
//                }
//            }
//            var price_to_discount = order.get_total_without_tax();
//            if (product.taxes_id.length){
//                var first_tax = this.env.pos.taxes_by_id[product.taxes_id[0]];
//                if (first_tax.price_include) {
//                    price_to_discount = order.get_total_with_tax();
//                }
//            }


//
//          if( discount < 0 ){
//                order.add_product(product, {
//                    price: discount,
//                    lst_price: discount,
//                    extras: {
//                        price_manually_set: true,
//                    },
//                });
//            }
//        }
   }
   CustomDiscountButtons.template = 'CustomDiscountButtons';
   ProductScreen.addControlButton({
       component: CustomDiscountButtons,
       condition: function() {
           return this.env.pos;
       },
   });
   Registries.Component.add(CustomDiscountButtons);
   return CustomDiscountButtons;
});
