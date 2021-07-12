odoo.define('pos_custom_buttons.DiscountButton', function(require) {
'use strict';
   const { Gui } = require('point_of_sale.Gui');
   const PosComponent = require('point_of_sale.PosComponent');
   const ProductScreen = require('point_of_sale.ProductScreen');
   const { useListener } = require('web.custom_hooks');
   const Registries = require('point_of_sale.Registries');

   class CustomDiscountButtons extends PosComponent {
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
            });
             if (confirmed) {
                const val = Math.round(Math.max(0,Math.min(100,parseFloat(payload))));
                await self.apply_discount(val);
            }
       }
         async apply_discount(pc) {
            var order    = this.env.pos.get_order();
            var lines    = order.get_orderlines();
            var product  = this.env.pos.db.get_product_by_id(this.env.pos.config.product_discount[0]);
//            if (product === undefined) {
//                await this.showPopup('ErrorPopup', {
//                    title : this.env._t("No discount product found"),
//                    body  : this.env._t("No"),
//                });
                return;

            }
//            var base_to_discount = order.get_total_without_tax();
//            if (product.taxes_id.length){
//                var first_tax = this.env.pos.taxes_by_id[product.taxes_id[0]];
//                if (first_tax.price_include) {
//                    base_to_discount = order.get_total_with_tax();
//                }
//            }
//            var discount = - pc / 100.0 * base_to_discount;


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
