from openerp import models, fields, api, _
from openerp.exceptions import UserError

class BeesdooPOSSession(models.Model):
    _inherit = 'pos.session'
    
    def wkf_action_open(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.cash_register_balance_start == 0:
                raise UserError(_('Please set opening balance.'))
        return super(BeesdooPOSSession, self).wkf_action_open(cr, uid, ids, context=context)
    
    def wkf_action_close(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.cash_register_balance_end_real == 0:
                raise UserError(_('Please set closing balance.'))
        return super(BeesdooPOSSession, self).wkf_action_close(cr, uid, ids, context=context)