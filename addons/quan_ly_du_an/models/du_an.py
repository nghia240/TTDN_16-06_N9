# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DuAn(models.Model):
    _name = 'du_an'
    _description = 'Quản lý dự án'

    ten_du_an = fields.Char(required=True, string="Tên dự án")
    ngan_sach = fields.Float(required=True, string="Ngân sách")
    ngay_bat_dau = fields.Date(required=True, string="Ngày bắt đầu")
    ngay_ket_thuc = fields.Date(required=True, string="Ngày kết thúc")
    mo_ta = fields.Text(string="Mô tả")

    nhan_vien_ids = fields.Many2many('nhan_vien', string="Nhân viên")

    nhiem_vu_ids = fields.One2many('nhiem_vu', 'du_an_id', string="Nhiệm vụ")

    trang_thai = fields.Selection([
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy_bo', 'Hủy bỏ')
    ], compute='_compute_trang_thai', store=True)

    tien_do_du_an = fields.Float(
        string="Tiến độ (%)",
        compute="_compute_tien_do",
        store=True
    )
    
    muc_uu_tien = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung bình'),
        ('cao', 'Cao'),
        ('rat_cao', 'Rất cao')
    ], string="Mức ưu tiên", default='trung_binh')
    
    so_luong_nhiem_vu = fields.Integer(
        string="Số lượng nhiệm vụ",
        compute="_compute_so_luong_nhiem_vu",
        store=True
    )
    
    so_luong_nhan_vien = fields.Integer(
        string="Số lượng nhân viên",
        compute="_compute_so_luong_nhan_vien",
        store=True
    )

    @api.depends('nhiem_vu_ids.trang_thai')
    def _compute_trang_thai(self):
        """Tính trạng thái dự án dựa trên trạng thái các nhiệm vụ"""
        for rec in self:
            if not rec.nhiem_vu_ids:
                rec.trang_thai = 'dang_thuc_hien'
            elif all(nv.trang_thai == 'hoan_thanh' for nv in rec.nhiem_vu_ids):
                rec.trang_thai = 'hoan_thanh'
            elif all(nv.trang_thai == 'huy_bo' for nv in rec.nhiem_vu_ids):
                rec.trang_thai = 'huy_bo'
            else:
                rec.trang_thai = 'dang_thuc_hien'

    @api.depends('nhiem_vu_ids.trang_thai')
    def _compute_tien_do(self):
        """Tính tiến độ dự án dựa trên tỷ lệ nhiệm vụ hoàn thành"""
        for rec in self:
            total = len(rec.nhiem_vu_ids)
            done = len(rec.nhiem_vu_ids.filtered(lambda x: x.trang_thai == 'hoan_thanh'))
            rec.tien_do_du_an = (done / total * 100) if total else 0
    
    @api.depends('nhiem_vu_ids')
    def _compute_so_luong_nhiem_vu(self):
        """Tính số lượng nhiệm vụ trong dự án"""
        for rec in self:
            rec.so_luong_nhiem_vu = len(rec.nhiem_vu_ids)
    
    @api.depends('nhan_vien_ids')
    def _compute_so_luong_nhan_vien(self):
        """Tính số lượng nhân viên tham gia dự án"""
        for rec in self:
            rec.so_luong_nhan_vien = len(rec.nhan_vien_ids)

    @api.constrains('ngay_bat_dau', 'ngay_ket_thuc')
    def _check_ngay_thang(self):
        """Kiểm tra ngày kết thúc phải sau ngày bắt đầu"""
        for rec in self:
            if rec.ngay_ket_thuc and rec.ngay_bat_dau:
                if rec.ngay_ket_thuc < rec.ngay_bat_dau:
                    raise ValidationError("Ngày kết thúc phải sau ngày bắt đầu!")

    @api.constrains('ngan_sach')
    def _check_ngan_sach(self):
        """Kiểm tra ngân sách phải lớn hơn 0"""
        for rec in self:
            if rec.ngan_sach < 0:
                raise ValidationError("Ngân sách phải lớn hơn hoặc bằng 0!")

    def name_get(self):
        """Hiển thị tên dự án"""
        return [(rec.id, rec.ten_du_an) for rec in self]
