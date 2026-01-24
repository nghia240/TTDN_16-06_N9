# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DanhGiaCongViec(models.Model):
    _name = 'danh_gia_cong_viec'
    _description = 'Quản lý đánh giá công việc'
    
    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên phụ trách")
    cong_viec_id = fields.Many2one("cong_viec", string="Công việc", required=True)
    kpi = fields.Float("KPI", required=True, default=0.0)
    nhan_xet = fields.Text("Nhận xét", required=True)

    @api.constrains('kpi')
    def _check_kpi(self):
        """Kiểm tra KPI phải lớn hơn hoặc bằng 0"""
        for rec in self:
            if rec.kpi < 0:
                raise ValidationError("KPI phải lớn hơn hoặc bằng 0!")       
