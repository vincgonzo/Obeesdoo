# -*- coding: utf-8 -*-

from openerp import models, fields

class beesdoo_intranet(models.Model):
    _name = 'beesdoo.intranet'

    def _get_default_partner(self):
        return self.env.uid #context['active_id']

    partner_id = fields.Many2one('res.partner', default=_get_default_partner)
    
    text = fields.Char("Hello")