# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date


class NhiemVu(models.Model):
    _name = 'nhiem_vu'
    _description = 'Nhiệm vụ'

    ten_nhiem_vu = fields.Char(required=True, string="Tên nhiệm vụ")
    mo_ta = fields.Text(string="Mô tả")

    du_an_id = fields.Many2one(
        'du_an',
        string="Dự án",
        required=True,
        ondelete='cascade'
    )

    trang_thai = fields.Selection([
        ('chua_bat_dau', 'Chưa bắt đầu'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy_bo', 'Hủy bỏ')
    ], string="Trạng thái", default='chua_bat_dau')

    ngay_bat_dau = fields.Date(string="Ngày bắt đầu")
    han_chot = fields.Date(string="Hạn chót")
    
    muc_uu_tien = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung bình'),
        ('cao', 'Cao'),
        ('rat_cao', 'Rất cao')
    ], string="Mức ưu tiên", default='trung_binh')
    
    nguoi_phu_trach_id = fields.Many2many(
        'nhan_vien',
        'nhiem_vu_nguoi_phu_trach_rel',
        'nhiem_vu_id',
        'nhan_vien_id',
        string="Người phụ trách"
    )
    
    nguoi_thuc_hien_id = fields.Many2many(
        'nhan_vien',
        'nhiem_vu_nguoi_thuc_hien_rel',
        'nhiem_vu_id',
        'nhan_vien_id',
        string="Người thực hiện"
    )
    
    so_luong_nguoi_phu_trach = fields.Integer(
        string="Số lượng người phụ trách",
        compute="_compute_so_luong_nguoi_phu_trach",
        store=True
    )
    
    so_luong_nguoi_thuc_hien = fields.Integer(
        string="Số lượng người thực hiện",
        compute="_compute_so_luong_nguoi_thuc_hien",
        store=True
    )
    
    so_ngay_thuc_hien = fields.Integer(
        string="Số ngày thực hiện",
        compute="_compute_so_ngay_thuc_hien",
        store=True
    )

    tien_do_ids = fields.One2many(
        'tien_do',
        'nhiem_vu_id',
        string="Tiến độ"
    )

    @api.depends('nguoi_phu_trach_id')
    def _compute_so_luong_nguoi_phu_trach(self):
        """Tính số lượng người phụ trách"""
        for rec in self:
            rec.so_luong_nguoi_phu_trach = len(rec.nguoi_phu_trach_id)
    
    @api.depends('nguoi_thuc_hien_id')
    def _compute_so_luong_nguoi_thuc_hien(self):
        """Tính số lượng người thực hiện"""
        for rec in self:
            rec.so_luong_nguoi_thuc_hien = len(rec.nguoi_thuc_hien_id)
    
    @api.depends('ngay_bat_dau', 'han_chot')
    def _compute_so_ngay_thuc_hien(self):
        """Tính số ngày thực hiện nhiệm vụ"""
        for rec in self:
            if rec.ngay_bat_dau and rec.han_chot:
                delta = rec.han_chot - rec.ngay_bat_dau
                rec.so_ngay_thuc_hien = delta.days if delta.days > 0 else 0
            else:
                rec.so_ngay_thuc_hien = 0

    @api.constrains('ngay_bat_dau', 'han_chot')
    def _check_ngay_thang(self):
        """Kiểm tra hạn chót phải sau ngày bắt đầu"""
        for rec in self:
            if rec.han_chot and rec.ngay_bat_dau:
                if rec.han_chot < rec.ngay_bat_dau:
                    raise ValidationError("Hạn chót phải sau ngày bắt đầu!")

    def name_get(self):
        """Hiển thị tên nhiệm vụ"""
        return [(rec.id, rec.ten_nhiem_vu) for rec in self]
