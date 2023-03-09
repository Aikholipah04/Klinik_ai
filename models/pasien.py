from odoo import models, fields, api

class Pasien(models.Model):
    _name ='klinik_ai.pasien'
    _description ='New Description'

    name = fields.Char(string='Nama Pasien')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    jenis_kelamin = fields.Char(string='Jenis Kelamin')
    umur = fields.Char(string='Umur Pasien')
    dokter_id = fields.Many2one(string='pasien dari', comodel_name='klinik_ai.dokter')