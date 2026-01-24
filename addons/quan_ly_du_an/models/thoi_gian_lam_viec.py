# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ThoiGianLamViec(models.Model):
    _name = "thoi_gian_lam_viec"
    _description = "Thời gian làm việc"

    nhiem_vu_id = fields.Many2one('nhiem_vu', string="Nhiệm vụ", ondelete='cascade', required=True)
    nhan_vien_id = fields.Many2many(
        'nhan_vien',
        'thoi_gian_lam_viec_nhan_vien_rel',
        'thoi_gian_lam_viec_id',
        'nhan_vien_id',
        string="Nhân viên",
        required=True
    )
    so_gio = fields.Float(string="Số giờ", required=True, default=0.0)
    ngay_lam_viec = fields.Datetime(string="Ngày làm việc", default=fields.Datetime.now)

    so_luong_nhan_vien = fields.Integer(string="Số lượng nhân viên", compute="_compute_so_luong_nhan_vien", store=True)

    @api.depends('nhan_vien_id')
    def _compute_so_luong_nhan_vien(self):
        """Tính số lượng nhân viên tham gia"""
        for record in self:
            record.so_luong_nhan_vien = len(record.nhan_vien_id)
    
    @api.onchange('nhiem_vu_id')
    def _onchange_nhiem_vu_id(self):
        """Tự động điền nhân viên từ nhiệm vụ"""
        if self.nhiem_vu_id and self.nhiem_vu_id.nguoi_thuc_hien_id:
            self.nhan_vien_id = [(6, 0, self.nhiem_vu_id.nguoi_thuc_hien_id.ids)]
        else:
            self.nhan_vien_id = [(5, 0, 0)]

    @api.constrains('so_gio')
    def _check_so_gio(self):
        """Kiểm tra số giờ làm việc phải lớn hơn 0"""
        for rec in self:
            if rec.so_gio <= 0:
                raise ValidationError("Số giờ làm việc phải lớn hơn 0!")
