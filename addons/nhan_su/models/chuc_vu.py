# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Bảng chứa thông tin chức vụ'

    ma_chuc_vu = fields.Char("Mã chức vụ", required=True)
    ten_chuc_vu = fields.Char("Tên chức vụ", required=True)
    lich_su_cong_tac_ids = fields.One2many(
        "lich_su_cong_tac",
        inverse_name="chuc_vu_id",
        string="Lịch sử công tác"
    )

    _sql_constraints = [
        ('ma_chuc_vu_unique', 'UNIQUE(ma_chuc_vu)', 'Mã chức vụ đã tồn tại!'),
    ]

    def name_get(self):
        """Hiển thị mã và tên chức vụ"""
        result = []
        for record in self:
            name = f"{record.ma_chuc_vu} - {record.ten_chuc_vu}"
            result.append((record.id, name))
        return result