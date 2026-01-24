# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NhiemVu(models.Model):
    _inherit = 'nhiem_vu'
    
    # Liên kết với module quan_ly_cong_viec
    # Các field này được thêm vào từ module quan_ly_cong_viec để tránh lỗi KeyError khi load module quan_ly_du_an
    cong_viec_ids = fields.One2many('cong_viec', 'nhiem_vu_id', string="Công việc liên quan")
    cong_viec_con_ids = fields.One2many('cong_viec_con', 'nhiem_vu_id', string="Công việc con liên quan")
    
    so_luong_cong_viec = fields.Integer(
        string="Số lượng công việc",
        compute="_compute_so_luong_cong_viec",
        store=True
    )
    
    @api.depends('cong_viec_ids', 'cong_viec_con_ids')
    def _compute_so_luong_cong_viec(self):
        """Tính tổng số lượng công việc và công việc con liên quan đến nhiệm vụ"""
        for rec in self:
            rec.so_luong_cong_viec = len(rec.cong_viec_ids) + len(rec.cong_viec_con_ids)

