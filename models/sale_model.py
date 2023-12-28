from odoo import api, fields, models
from odoo.exceptions import UserError

class SaleModel (models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    credit_limit = fields.Float(related="partner_id.credit_limit", String="Credit Limit")
    total_receivable = fields.Float(related="partner_id.total_receivable", String="Credit")
    total_payable = fields.Float(related="partner_id.total_payable", String="Debit")
    balance = fields.Float(related="partner_id.balance", String="Balance")
    amount_available = fields.Float(related="partner_id.amount_available", String="Amount_available")
    
    
    def action_confirm(self):
        for order in self:
            if order.amount_available < order.amount_total:
                raise UserError("Over Credit Limit")
        return super(SaleModel, self).action_confirm()


    # def action_confirm(self):
    #     print("action has been confirmed")
    #     view_id = self.env.ref('customer_credit_limit_v17.view_warning_wizard_form')
    #     context = dict(self.env.context or {})
    #     context['message'] = "Over Credit Limit"
    #     context['default_sale_id'] = self.id
    #     if self.amount_available < self.amount_total:
    #         print("There should be an error here")
    #         return {
    #             'name': 'Warning',
    #             'type': 'ir.actions.act_window',
    #             'view_mode': 'form',
    #             'res_model': 'warning.wizard',
    #             'view_id': view_id.id,
    #             'target': 'new',
    #             'context': context,
    #         }
    # 
    #     res = super(SaleModel, self).action_confirm()
    #     return res
