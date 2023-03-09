# -*- coding: utf-8 -*-
# from odoo import http


# class KlinikAi(http.Controller):
#     @http.route('/klinik_ai/klinik_ai/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/klinik_ai/klinik_ai/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('klinik_ai.listing', {
#             'root': '/klinik_ai/klinik_ai',
#             'objects': http.request.env['klinik_ai.klinik_ai'].search([]),
#         })

#     @http.route('/klinik_ai/klinik_ai/objects/<model("klinik_ai.klinik_ai"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('klinik_ai.object', {
#             'object': obj
#         })
