from odoo import models, fields, api

class Suplier(models.Model):
    _name ='klinik_ai.supplier'
    _description ='New Description'

    name = fields.Char(string='Nama Supplier')
    alamat = fields.Char(string='Alamat Supplier')
    no_hp = fields.Char(string='Nomor Handphone')
    obat_id = fields.Many2one(string='obatnya', 
                              comodel_name='klinik_ai.obat', 
                              inverse_name='supplier_id')
    