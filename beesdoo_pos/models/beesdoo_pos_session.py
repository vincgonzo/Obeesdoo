from openerp import models, fields, api, _
from openerp.exceptions import UserError

class BeesdooPOSSession(models.Model):
    _inherit = 'pos.session'
    
    def wkf_action_open(self, cr, uid, ids, context=None):
        try:
            for record in self.browse(cr, uid, ids, context=context):
                if record.cash_register_balance_start == 0:
                    raise UserError(_('Please set opening balance.'))
        except UserError:
            return super(pos_session, self).wkf_action_open(cr, uid, ids, context=context)