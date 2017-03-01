from openerp import fields, models

class BeesAccountCashboxLine(models.Model):
    _inherit = 'account.cashbox.line'
    # Put 0 as default value to have the subtotal directly computed, so the total is also displayed
    number = fields.Integer(default=0) 