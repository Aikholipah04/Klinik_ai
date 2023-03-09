from odoo import models, fields, api


class Dokter(models.Model):
      _name = 'klinik_ai.dokter'
      _description = 'New Description'

      name = fields.Char(string='Nama Dokter')
      jenis_kelamin = fields.Char('Jenis Kelamin')
      spesialis  = fields.Char(string='Spesialis')
      pasien_ids = fields.One2many(string='daftar pasien',
                                   comodel_name='klinik_ai.pasien',
                                   inverse_name='dokter_id')
 
