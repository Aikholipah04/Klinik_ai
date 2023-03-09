from odoo import models, fields, api

class Penjualan(models.Model):
    _name ='klinik_ai.penjualan'
    _description ='New Description'

    name = fields.Char(string='Kode')
    pasien_id = fields.Many2one(string='Nama Pasien', comodel_name='klinik_ai.pasien')
    total_bayar= fields.Integer(compute='_compute_total_bayar', string='Total Bayar', store=True)
    tanggal_transaksi = fields.Datetime(string='Tanggal Transaksi', default=fields.Datetime.now())
    penjualandetail_ids = fields.One2many(string='Daftar Penjualan',
                                          comodel_name='klinik_ai.penjualandetail',
                                          inverse_name='penjualan_id')
    
    @api.depends('penjualandetail_ids')
    def _compute_total_bayar(self):
        for record in self:
            total= sum(self.env['klinik_ai.penjualandetail'].search([('penjualan_id','=',record.id)]).mapped('harga'))
            record.total_bayar =total
    
    


class Penjualandetail(models.Model):
    _name ='klinik_ai.penjualandetail'
    _description ='New Description'
    _rec_name ='obat_id'

    obat_id = fields.Many2one(string='Obat', comodel_name='klinik_ai.obat')
    penjualan_id = fields.Many2one(string='Penjualan', comodel_name='klinik_ai.penjualan')
    harga = fields.Integer(compute='_compute_harga', string='harga')
    satuan = fields.Integer(compute='_compute_satuan', string='satuan')
    qty = fields.Integer(string='quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='subtotal')

    

    @api.depends('harga','qty')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.harga * record.qty

    
    @api.depends('obat_id')
    def _compute_satuan(self):
        for record in self:
            record.satuan = record.obat_id.satuan

    
    @api.depends('obat_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.obat_id.harga_jual
    
    
    
    
    

    





