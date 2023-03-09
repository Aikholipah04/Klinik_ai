from odoo import models, fields, api

class Obat(models.Model):
      _name = 'klinik_ai.obat'
      _description = 'New Description'

      name = fields.Char(string='Nama Obat')
      harga = fields.Integer(string='Harga')
      harga_jual = fields.Integer(string='Harga Jual')
      satuan = fields.Char(string='Satuan')
      stok = fields.Char(string='Stok')
      supplier_id = fields.Many2one(string='suppliernya', comodel_name='klinik_ai.supplier')
      img = fields.Binary(string='Image')
     
      
      