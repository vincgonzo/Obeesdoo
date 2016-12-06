


from openerp import models, fields, api, _

class BeesdooPOSSession(models.Model):
    _inherit = 'pos.session'

    def wkf_action_open(self, cr, uid, ids, context=None):
        print "test"
        #if self.cash_control:
        #    if not self.cash_register_balance_start:
        #        raise UserError(_('Please set opening balance.'))
        return super(pos_session, self).wkf_action_open(cr, uid, ids, context)
            