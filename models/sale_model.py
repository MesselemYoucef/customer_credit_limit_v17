from odoo import api, fields, models
from odoo.exceptions import ValidationError

class SaleModel (models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one("res.partner")
    credit_limit = fields.Float(related="partner_id.credit_limit", String="Credit Limit")
    total_receivable = fields.Float(related="partner_id.total_receivable", String="Credit")
    total_payable = fields.Float(related="partner_id.total_payable", String="Debit")
    balance = fields.Float(related="partner_id.balance", String="Balance")
    amount_available = fields.Float(related="partner_id.amount_available", String="Amount_available")




    # @api.constrains("amount_total")
    # def _check_amount_available(self):
    #     for record in self:
    #         if record.amount_available < record.amount_total:
    #             raise ValidationError("Please check the Credit Limit.")
    #     #All records passed the test don't return anything

    # @api.onchange("total_amount")
    # def onchange_amount(self):
    #     res = {}
    #     res['warning'] = {'title': ("Warning"), 'message': ('Over Credit Limit'), }
    #     return res

    # @api.depends("amount_total")
    # def _check_user_cost_privilege(self):
    #     res = {}
    #     for record in self:
    #         if record.amount_available < record.amount_total:
    #             res['warning'] = {'title': ("Warning"), 'message': ('Over Credit Limit'), }
    #             return res

    # def compute_amounts(self):
    #     res = super(SaleModel, self).compute_amounts()
    #     res['warning'] = {'title': ("Warning"), 'message': ('Over Credit Limit'), }
    #     return res