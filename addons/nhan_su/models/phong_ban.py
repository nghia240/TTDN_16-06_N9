# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Bảng chứa thông tin phòng ban'

    ma_phong_ban = fields.Char("Mã phòng ban", required=True)
    ten_phong_ban = fields.Char("Tên phòng ban", required=True)
    lich_su_cong_tac_ids = fields.One2many(
        "lich_su_cong_tac",
        inverse_name="phong_ban_id",
        string="Lịch sử công tác"
    )

    _sql_constraints = [
        ('ma_phong_ban_unique', 'UNIQUE(ma_phong_ban)', 'Mã phòng ban đã tồn tại!'),
    ]

    def name_get(self):
        """Hiển thị mã và tên phòng ban"""
        result = []
        for record in self:
            name = f"{record.ma_phong_ban} - {record.ten_phong_ban}"
            result.append((record.id, name))
        return result
