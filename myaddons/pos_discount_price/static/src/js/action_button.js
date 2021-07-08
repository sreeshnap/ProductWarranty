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
       onClick() {
                Gui.showPopup("ErrorPopup", {
                       title: this.env._t('Discount Button clicked'),
                       body: this.env._t('Discount'),
                   });
       }
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
