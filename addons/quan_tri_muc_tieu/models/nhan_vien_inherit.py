# -*- coding: utf-8 -*-

from odoo import api, fields, models


class NhanVien(models.Model):
    _inherit = "nhan_vien"

    muc_tieu_ids = fields.One2many("muc_tieu", "nhan_vien_id", string="Mục tiêu")
    so_muc_tieu = fields.Integer(string="Số mục tiêu", compute="_compute_so_muc_tieu")

    so_cong_viec = fields.Integer(string="Số công việc", compute="_compute_stats_cong_viec")
    tien_do_trung_binh = fields.Float(string="Tiến độ TB (%)", compute="_compute_stats_cong_viec")

    def _compute_so_muc_tieu(self):
        for rec in self:
            rec.so_muc_tieu = len(rec.muc_tieu_ids)

    @api.depends()
    def _compute_stats_cong_viec(self):
        CongViec = self.env["cong_viec"]
        CongViecCon = self.env["cong_viec_con"]
        for rec in self:
            cvs = CongViec.search([("nhan_vien_id", "=", rec.id)])
            cvcs = CongViecCon.search([("nhan_vien_id", "=", rec.id)])
            rec.so_cong_viec = len(cvs) + len(cvcs)
            progresses = (cvs.mapped("tien_do") or []) + (cvcs.mapped("tien_do") or [])
            progresses = [p for p in progresses if p is not None]
            rec.tien_do_trung_binh = (sum(progresses) / len(progresses)) if progresses else 0.0

    def action_view_muc_tieu(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Mục tiêu",
            "res_model": "muc_tieu",
            "view_mode": "tree,form",
            "domain": [("nhan_vien_id", "=", self.id)],
            "context": {"default_nhan_vien_id": self.id},
        }

