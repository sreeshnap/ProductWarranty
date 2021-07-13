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
                await self.apply_discount(val);
            }
       }
         async apply_discount(pc) {
            var order    = this.env.pos.get_order();
            var lines    = order.get_orderlines();
//            var product  = this.env.pos.db.get_product_by_id(this.env.pos.config.discount_product_id[0]);
            var product  = this.env.pos.db.get_product_by_id;
                console.log(product)
                console.log(order)
                console.log(lines)
                return;

            }
//        price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
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
