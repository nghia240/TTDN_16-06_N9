# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    lich_su_cong_tac_ids = fields.One2many(
        "lich_su_cong_tac",
        inverse_name="nhan_vien_id",
        string="Lịch sử công tác"
    )
    ho_ten_dem = fields.Char("Họ tên đệm", required=True)
    ten = fields.Char("Tên", required=True)
    ho_va_ten = fields.Char("Họ và tên", compute='_tinh_ho_va_ten', store=True)
    
    @api.depends("ho_ten_dem", "ten")
    def _tinh_ho_va_ten(self):
        """Tính họ và tên từ họ tên đệm và tên"""
        for record in self:
            if record.ho_ten_dem and record.ten:
                record.ho_va_ten = record.ho_ten_dem + ' ' + record.ten
            else:
                record.ho_va_ten = ''
                
    def name_get(self):
        """Hiển thị mã định danh và họ tên"""
        result = []
        for record in self:
            name = f"{record.ma_dinh_danh} - {record.ho_va_ten}"
            result.append((record.id, name))
        return result

    _sql_constraints = [
        ('ma_dinh_danh_unique', 'UNIQUE(ma_dinh_danh)', 'Mã định danh đã tồn tại!'),
    ]

    @api.constrains('email')
    def _check_email(self):
        """Kiểm tra định dạng email"""
        for rec in self:
            if rec.email and '@' not in rec.email:
                raise ValidationError("Email không hợp lệ!")