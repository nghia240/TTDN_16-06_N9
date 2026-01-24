# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MucTieuDong(models.Model):
    _name = "muc_tieu_dong"
    _description = "Dòng mục tiêu (liên kết nhiệm vụ/công việc)"

    muc_tieu_id = fields.Many2one("muc_tieu", required=True, ondelete="cascade")
    name = fields.Char(string="Nội dung", required=True)

    # Liên kết “chia nhỏ” theo 3 tầng: nhiệm vụ / công việc / công việc con
    nhiem_vu_id = fields.Many2one("nhiem_vu", string="Nhiệm vụ")
    cong_viec_id = fields.Many2one("cong_viec", string="Công việc")
    cong_viec_con_id = fields.Many2one("cong_viec_con", string="Công việc con")

    nhan_vien_id = fields.Many2one("nhan_vien", string="Nhân viên (tuỳ chọn)")

    trong_so = fields.Float(string="Trọng số", default=1.0)
    tien_do_thuc_te = fields.Float(string="Tiến độ thực tế (%)", compute="_compute_tien_do_thuc_te", store=True)

    ghi_chu = fields.Text(string="Ghi chú")

    @api.constrains("nhiem_vu_id", "cong_viec_id", "cong_viec_con_id")
    def _check_only_one_link(self):
        for rec in self:
            links = [bool(rec.nhiem_vu_id), bool(rec.cong_viec_id), bool(rec.cong_viec_con_id)]
            if sum(1 for x in links if x) > 1:
                raise models.ValidationError("Mỗi dòng mục tiêu chỉ được liên kết 1 trong 3: Nhiệm vụ/Công việc/Công việc con.")

    @api.depends(
        "nhiem_vu_id.tien_do_pct",
        "nhiem_vu_id.trang_thai",
        "cong_viec_id.tien_do",
        "cong_viec_con_id.tien_do",
    )
    def _compute_tien_do_thuc_te(self):
        for rec in self:
            if rec.cong_viec_con_id:
                rec.tien_do_thuc_te = rec.cong_viec_con_id.tien_do or 0.0
            elif rec.cong_viec_id:
                rec.tien_do_thuc_te = rec.cong_viec_id.tien_do or 0.0
            elif rec.nhiem_vu_id:
                # ưu tiên % tính được, fallback theo trạng thái
                if hasattr(rec.nhiem_vu_id, "tien_do_pct"):
                    rec.tien_do_thuc_te = rec.nhiem_vu_id.tien_do_pct or 0.0
                else:
                    rec.tien_do_thuc_te = 100.0 if rec.nhiem_vu_id.trang_thai == "hoan_thanh" else 0.0
            else:
                rec.tien_do_thuc_te = 0.0

