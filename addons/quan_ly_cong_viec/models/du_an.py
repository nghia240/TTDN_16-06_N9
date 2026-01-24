# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DuAn(models.Model):
    _inherit = 'du_an'
    
    # Liên kết với module quan_ly_cong_viec
    # Field này được thêm vào từ module quan_ly_cong_viec để tránh lỗi KeyError khi load module quan_ly_du_an
    cong_viec_ids = fields.One2many('cong_viec', 'du_an_id', string="Công việc liên quan")
    
    so_luong_cong_viec = fields.Integer(
        string="Số lượng công việc",
        compute="_compute_so_luong_cong_viec",
        store=True
    )
    
    @api.depends('cong_viec_ids')
    def _compute_so_luong_cong_viec(self):
        """Tính số lượng công việc liên quan đến dự án"""
        for rec in self:
            rec.so_luong_cong_viec = len(rec.cong_viec_ids)

