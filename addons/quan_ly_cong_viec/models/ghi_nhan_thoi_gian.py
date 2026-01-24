# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GhiNhanThoiGian(models.Model):
    _name = 'ghi_nhan_thoi_gian'
    _description = 'Quản lý ghi nhận thời gian làm việc'
    
    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên phụ trách")
    cong_viec_id = fields.Many2one("cong_viec", string="Công việc", required=True)
    so_gio_lam_viec = fields.Float("Số giờ làm việc", required=True, default=0.0)
    ngay_ghi_nhan = fields.Date("Ngày ghi nhận", required=True, default=fields.Date.today)

    @api.constrains('so_gio_lam_viec')
    def _check_so_gio(self):
        """Kiểm tra số giờ làm việc phải lớn hơn 0"""
        for rec in self:
            if rec.so_gio_lam_viec <= 0:
                raise ValidationError("Số giờ làm việc phải lớn hơn 0!")

    @api.constrains('ngay_ghi_nhan', 'cong_viec_id')
    def _check_ngay_ghi_nhan(self):
        """Kiểm tra ngày ghi nhận phải trong khoảng thời gian của công việc"""
        for rec in self:
            if rec.cong_viec_id and rec.cong_viec_id.ngay_bat_dau and rec.cong_viec_id.ngay_ket_thuc:
                if rec.ngay_ghi_nhan < rec.cong_viec_id.ngay_bat_dau:
                    raise ValidationError("Ngày ghi nhận không được trước ngày bắt đầu công việc!")
                if rec.ngay_ghi_nhan > rec.cong_viec_id.ngay_ket_thuc:
                    raise ValidationError("Ngày ghi nhận không được sau ngày kết thúc công việc!")       
