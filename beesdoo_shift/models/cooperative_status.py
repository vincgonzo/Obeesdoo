# -*- coding: utf-8 -*-
from openerp import models, fields

class CooperativeStatus(models.Model):
    _name = 'cooperative.status'
    _rec_name = 'cooperator_id'

    cooperator_id = fields.Many2one('res.partner')
    super = fields.Boolean("Super Cooperative")
    sr = fields.Integer("Compteur shift regulier")
    sc = fields.Integer("Compteur shift de compensation")
    time_holiday = fields.Integer("Holidays Days NB", default=0)
    time_extension = fields.Integer("Extension Days NB", default=0) #Durée initial par défault sur ir_config_parameter
    holiday_start_time = fields.Date("Holidays Start Day")
    alert_start_time = fields.Date("Alert Start Day")
    extension_start_time = fields.Date("Extension Start Day")
    #Champ compute
    status = fields.Selection([('ok',  'Up to Date'), ('holiday', 'Holidays'), ('alert', 'Alerte'), ('unsubscribed', 'Unsubscribed')], compute="_compute_status", string="Cooperative Status")
    working_mode = fields.Selection(
        [
            ('regular', 'Regular worker'),
            ('irregular', 'Irregular worker'),
            ('exempt', 'Exempted'),
        ],
        string="Working mode",
    )
    
    def _compute_status(self):
        for rec in self:
            rec.status = 'ok'
 
class ResPartner(models.Model):
    _inherit = 'res.partner'

    super = fields.Boolean(related='cooperative_status_ids.super', string="Super Cooperative", readonly=True)
    cooperative_status_ids = fields.One2many('cooperative.status', 'cooperator_id', readonly=True)
    working_mode = fields.Selection(related='user_ids.working_mode', readonly=True)
