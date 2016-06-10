# -*- coding: utf-8 -*-

from openerp import models, fields, api

class beesdoo_intranet(models.Model):
    _name = 'beesdoo_intranet'

    text = fields.Char("Hello")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
