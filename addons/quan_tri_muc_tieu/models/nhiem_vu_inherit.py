# -*- coding: utf-8 -*-

from odoo import api, fields, models


class NhiemVu(models.Model):
    _inherit = "nhiem_vu"

    # % tiến độ dùng chung cho mục tiêu/KPI
    tien_do_pct = fields.Float(string="Tiến độ (%)", compute="_compute_tien_do_pct", store=True)

    @api.depends("trang_thai", "cong_viec_ids.tien_do", "cong_viec_con_ids.tien_do")
    def _compute_tien_do_pct(self):
        for rec in self:
            if rec.trang_thai == "hoan_thanh":
                rec.tien_do_pct = 100.0
                continue
            # ưu tiên tính từ công việc liên quan (nếu có)
            progresses = []
            if hasattr(rec, "cong_viec_ids"):
                progresses += rec.cong_viec_ids.mapped("tien_do")
            if hasattr(rec, "cong_viec_con_ids"):
                progresses += rec.cong_viec_con_ids.mapped("tien_do")

            progresses = [p for p in progresses if p is not None]
            rec.tien_do_pct = (sum(progresses) / len(progresses)) if progresses else 0.0

