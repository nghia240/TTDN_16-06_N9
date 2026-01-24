# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CongViecCon(models.Model):
    _name = 'cong_viec_con'
    _description = 'Quản lý Công Việc Con'
    
    cong_viec_id = fields.Many2one("cong_viec", string="Công việc", required=True)
    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên phụ trách")
    
    # Liên kết với module quan_ly_du_an
    nhiem_vu_id = fields.Many2one('nhiem_vu', string="Nhiệm vụ", help="Liên kết công việc con với nhiệm vụ")
    ten_cong_viec_con = fields.Char("Tên công việc con", required=True)
    han_hoan_thanh = fields.Date("Hạn hoàn thành", required=True)
    tien_do = fields.Float("Tiến độ %", required=True, default=0.0)
    
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

    @api.constrains('han_hoan_thanh')
    def _check_han_hoan_thanh(self):
        """Kiểm tra hạn hoàn thành phải hợp lệ"""
        for rec in self:
            if rec.cong_viec_id and rec.cong_viec_id.ngay_bat_dau:
                if rec.han_hoan_thanh < rec.cong_viec_id.ngay_bat_dau:
                    raise ValidationError("Hạn hoàn thành công việc con phải sau ngày bắt đầu công việc chính!")

    @api.constrains('tien_do')
    def _check_tien_do(self):
        """Kiểm tra tiến độ phải trong khoảng 0-100%"""
        for rec in self:
            if rec.tien_do < 0 or rec.tien_do > 100:
                raise ValidationError("Tiến độ phải trong khoảng 0-100%!")
    