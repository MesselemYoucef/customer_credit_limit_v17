from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Float(String="Credit Limit")
    total_receivable = fields.Float(String="Credit", compute="_calculate_total_credit")
    total_payable = fields.Float(String="Debit", compute="_calculate_total_debit")
    balance = fields.Float(String="Balance", compute="_calculate_balance")
    amount_available = fields.Float(String="Amount Available", compute="_calculate_amount_available")

    def _calculate_total_credit(self):
        self.total_receivable = self.credit

    def _calculate_total_debit(self):
        self.total_payable = self.debit

    def _calculate_balance(self):
        self.balance = self.total_receivable - self.total_payable

    def _calculate_amount_available(self):
        self.amount_available = self.credit_limit - self.balance
