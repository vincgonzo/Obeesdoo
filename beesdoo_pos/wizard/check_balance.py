# -*- coding: utf-8 -*-
from openerp import models, fields, api

class OpeningBalanceWizard(models.TransientModel):
    
    _name = 'opening.balance.new.wizard'
    
    def _get_opening_balance(self):
        print "_get_opening_balance", self.env['pos.session'].cash_register_id.balance_start
        return self.env['pos.session'].cash_register_id.balance_start
    
    balance = fields.Float('Opening Balance', default=_get_opening_balance)
       
    @api.one
    def open_session(self):
        #self.env['pos.session'].open_session_cb
       self.env['pos.session'].states="opened"
       self.env['pos.session'].wkf_action_open