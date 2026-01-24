# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TienDo(models.Model):
    _name = "tien_do"
    _description = "Tiến độ công việc"
    _order = "ngay_cap_nhat desc"

    # ===== LIÊN KẾT CHÍNH =====
    nhiem_vu_id = fields.Many2one(
        'nhiem_vu',
        string="Nhiệm vụ",
        required=True,
        ondelete='cascade'
    )

    du_an_id = fields.Many2one(
        related='nhiem_vu_id.du_an_id',
        string="Dự án",
        store=True,
        readonly=True
    )

    # ===== THÔNG TIN TIẾN ĐỘ =====
    ghi_chu = fields.Text(string="Ghi chú")
    ngay_cap_nhat = fields.Datetime(
        string="Ngày cập nhật",
        default=fields.Datetime.now,
        required=True
    )

    nguoi_cap_nhat_id = fields.Many2one(
        'res.users',
        string="Người cập nhật",
        default=lambda self: self.env.user,
        readonly=True
    )

    # ===== THÔNG TIN TỔNG HỢP (READONLY) =====
    phan_tram_hoan_thanh = fields.Float(
        string="Phần trăm hoàn thành (%)",
        compute="_compute_phan_tram_hoan_thanh",
        store=False
    )

    trang_thai_du_an = fields.Selection(
        related='du_an_id.trang_thai',
        string="Trạng thái dự án",
        readonly=True,
        store=False
    )

    # ===== COMPUTE =====
    def _compute_phan_tram_hoan_thanh(self):
        """Tính phần trăm hoàn thành của dự án"""
        for rec in self:
            rec.phan_tram_hoan_thanh = (
                round(rec.du_an_id.tien_do_du_an, 2)
                if rec.du_an_id else 0.0
            )
