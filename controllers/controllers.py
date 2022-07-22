# -*- coding: utf-8 -*-
# from odoo import http


# class MunDic(http.Controller):
#     @http.route('/mun_dic/mun_dic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mun_dic/mun_dic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mun_dic.listing', {
#             'root': '/mun_dic/mun_dic',
#             'objects': http.request.env['mun_dic.mun_dic'].search([]),
#         })

#     @http.route('/mun_dic/mun_dic/objects/<model("mun_dic.mun_dic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mun_dic.object', {
#             'object': obj
#         })
