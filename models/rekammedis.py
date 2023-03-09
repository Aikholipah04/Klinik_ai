from odoo import models, fields, api


class Rekammedis(models.Model):
    _name ='klinik_ai.rekammedis'
    _description ='New Description'

    name = fields.Char(string='Kode')
    pasien_id = fields.Many2one(string='Nama Pasien', comodel_name='klinik_ai.pasien')
    tanggal_daftar = fields.Datetime(string='Tanggal Daftar',default=fields.Datetime.now())
    penyakit = fields.Char(string='Penyakit')
    obat = fields.Char(string='Obat')
    
