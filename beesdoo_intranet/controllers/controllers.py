# -*- coding: utf-8 -*-
from openerp import http

# class BeesdooIntranet(http.Controller):
#     @http.route('/beesdoo_intranet/beesdoo_intranet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/beesdoo_intranet/beesdoo_intranet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('beesdoo_intranet.listing', {
#             'root': '/beesdoo_intranet/beesdoo_intranet',
#             'objects': http.request.env['beesdoo_intranet.beesdoo_intranet'].search([]),
#         })

#     @http.route('/beesdoo_intranet/beesdoo_intranet/objects/<model("beesdoo_intranet.beesdoo_intranet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('beesdoo_intranet.object', {
#             'object': obj
#         })