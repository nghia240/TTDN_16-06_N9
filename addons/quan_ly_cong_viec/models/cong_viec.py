# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công Việc'

    ten_cong_viec = fields.Char("Tên công việc", required=True)
    han_hoan_thanh = fields.Date("Hạn hoàn thành", required=True)
    tien_do = fields.Float("Tiến độ %", required=True, default=0.0)
    ngay_bat_dau = fields.Date("Ngày bắt đầu", required=True)
    ngay_ket_thuc = fields.Date("Ngày kết thúc", required=True)
    mo_ta = fields.Text("Mô tả công việc", required=True)
    trang_thai = fields.Selection(
        [
            ('moi', 'Mới'),
            ('dang_thuc_hien', 'Đang thực hiện'),
            ('dang_cho', 'Đang chờ '),
            ('tam_hoan', 'Tạm hoãn'),
            ('hoan_thanh', 'Hoàn thành'),
            ('da_huy', 'Đã hủy'),
            ('qua_han', 'Quá hạn'),
            ('da_duyet', 'Đã duyệt'),
            ('can_sua_doi', 'Cần sửa đổi'),
            
        ],
        string= "Trạng thái", default="moi"
    )
    cong_viec_con_ids = fields.One2many ("cong_viec_con", inverse_name="cong_viec_id", string="Công việc con")
    nhan_vien_id = fields.Many2one('nhan_vien',string="Nhân viên phụ trách")
    ghi_nhan_thoi_gian_ids = fields.One2many ("ghi_nhan_thoi_gian", inverse_name="cong_viec_id", string="Ghi nhận thời gian")
    danh_gia_cong_viec_ids = fields.One2many ("danh_gia_cong_viec", inverse_name="cong_viec_id", string="Đánh giá công việc")
    
    # Liên kết với module quan_ly_du_an
    du_an_id = fields.Many2one('du_an', string="Dự án", help="Liên kết công việc với dự án")
    nhiem_vu_id = fields.Many2one('nhiem_vu', string="Nhiệm vụ", help="Liên kết công việc với nhiệm vụ")
    
    # Tính tiến độ tự động từ công việc con (tùy chọn)
    tien_do_tu_dong = fields.Float(
        string="Tiến độ tự động (%)",
        compute="_compute_tien_do_tu_dong",
        store=False,
        help="Tiến độ tự động tính từ công việc con (chỉ đọc)"
    )
    
    @api.depends('cong_viec_con_ids.tien_do')
    def _compute_tien_do_tu_dong(self):
        """Tự động tính tiến độ từ công việc con"""
        for rec in self:
            if rec.cong_viec_con_ids:
                total_tien_do = sum(rec.cong_viec_con_ids.mapped('tien_do'))
                rec.tien_do_tu_dong = total_tien_do / len(rec.cong_viec_con_ids)
            else:
                rec.tien_do_tu_dong = 0.0

    @api.constrains('ngay_bat_dau', 'ngay_ket_thuc', 'han_hoan_thanh')
    def _check_ngay_thang(self):
        """Kiểm tra tính hợp lệ của ngày tháng"""
        for rec in self:
            if rec.ngay_ket_thuc and rec.ngay_bat_dau:
                if rec.ngay_ket_thuc < rec.ngay_bat_dau:
                    raise ValidationError("Ngày kết thúc phải sau ngày bắt đầu!")
            if rec.han_hoan_thanh and rec.ngay_bat_dau:
                if rec.han_hoan_thanh < rec.ngay_bat_dau:
                    raise ValidationError("Hạn hoàn thành phải sau ngày bắt đầu!")

    @api.constrains('tien_do')
    def _check_tien_do(self):
        """Kiểm tra tiến độ phải trong khoảng 0-100%"""
        for rec in self:
            if rec.tien_do < 0 or rec.tien_do > 100:
                raise ValidationError("Tiến độ phải trong khoảng 0-100%!")
    