# -*- coding: utf-8 -*-
{
    "name": "quan_tri_muc_tieu",
    "summary": "Quản trị mục tiêu & KPI theo nhân viên, bám sát dự án/nhiệm vụ/công việc",
    "description": """
Quản trị mục tiêu:
- Chia nhỏ dự án -> nhiệm vụ -> công việc/công việc con
- Theo dõi tiến độ và hiệu quả theo từng nhân viên
Tích hợp chặt với: nhan_su, quan_ly_du_an, quan_ly_cong_viec
""",
    "author": "TTDN-15-04",
    "website": "http://www.yourcompany.com",
    "category": "Project",
    "version": "15.0.1.0.0",
    "depends": [
        "base",
        "mail",
        "nhan_su",
        "quan_ly_du_an",
        "quan_ly_cong_viec",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/muc_tieu.xml",
        "views/menu.xml",
        "views/nhan_vien_inherit.xml",
        "views/nhiem_vu_inherit.xml",
    ],
    "installable": True,
    "application": True,
}

