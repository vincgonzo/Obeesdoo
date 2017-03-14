# -*- coding: utf-8 -*-
from openerp import models, fields, api

class OpeningBalanceWizard(models.TransientModel):
    
    _name = 'opening.balance.new.wizard'
    
    def _get_opening_balance(self):
        return self.env['pos.session'].browse(self._context['active_id']).cash_register_id.balance_start
    
    opening_balance = fields.Float('Opening Balance', default=_get_opening_balance, readonly = True)
    
    @api.one
    def open_session(self):
        print 'open_session'
        print '#########################'
        
        return self.env['pos.session'].browse(self._context['active_id']).open_session