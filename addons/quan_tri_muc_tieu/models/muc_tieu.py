# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MucTieu(models.Model):
    _name = "muc_tieu"
    _description = "Mục tiêu theo nhân viên"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Tên mục tiêu", required=True, tracking=True)
    nhan_vien_id = fields.Many2one("nhan_vien", string="Nhân viên", required=True, tracking=True)

    ngay_bat_dau = fields.Date(string="Từ ngày", required=True, tracking=True)
    ngay_ket_thuc = fields.Date(string="Đến ngày", required=True, tracking=True)

    du_an_id = fields.Many2one("du_an", string="Dự án (tuỳ chọn)", tracking=True)
    mo_ta = fields.Text(string="Mô tả")

    trang_thai = fields.Selection(
        [
            ("nhap", "Nháp"),
            ("dang_thuc_hien", "Đang thực hiện"),
            ("hoan_thanh", "Hoàn thành"),
            ("huy", "Hủy"),
        ],
        default="nhap",
        string="Trạng thái",
        tracking=True,
    )

    dong_ids = fields.One2many("muc_tieu_dong", "muc_tieu_id", string="Chi tiết mục tiêu")

    tong_trong_so = fields.Float(string="Tổng trọng số", compute="_compute_tong_trong_so", store=True)
    tien_do = fields.Float(string="Tiến độ (%)", compute="_compute_tien_do", store=True)

    @api.depends("dong_ids.trong_so")
    def _compute_tong_trong_so(self):
        for rec in self:
            rec.tong_trong_so = sum(rec.dong_ids.mapped("trong_so")) if rec.dong_ids else 0.0

    @api.depends("dong_ids.tien_do_thuc_te", "dong_ids.trong_so")
    def _compute_tien_do(self):
        for rec in self:
            if not rec.dong_ids:
                rec.tien_do = 0.0
                continue
            tong_trong_so = sum(rec.dong_ids.mapped("trong_so")) or 0.0
            if tong_trong_so <= 0:
                # fallback: trung bình
                rec.tien_do = sum(rec.dong_ids.mapped("tien_do_thuc_te")) / len(rec.dong_ids)
            else:
                rec.tien_do = sum((l.trong_so * l.tien_do_thuc_te) for l in rec.dong_ids) / tong_trong_so

    def action_start(self):
        self.write({"trang_thai": "dang_thuc_hien"})

    def action_done(self):
        self.write({"trang_thai": "hoan_thanh"})

    def action_cancel(self):
        self.write({"trang_thai": "huy"})

    def action_draft(self):
        self.write({"trang_thai": "nhap"})

