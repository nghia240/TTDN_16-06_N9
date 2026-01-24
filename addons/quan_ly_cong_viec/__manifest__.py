# -*- coding: utf-8 -*-
{
    'name': "Quản lý công việc",
    'summary': "Hệ thống quản lý công việc, công việc con, ghi nhận thời gian và đánh giá",
    'description': """
        Module quản lý công việc bao gồm:
        - Quản lý công việc và công việc con
        - Ghi nhận thời gian làm việc
        - Đánh giá công việc (KPI)
        - Liên kết với dự án và nhiệm vụ
    """,
    'author': "phuccthuan",
    'website': "http://www.yourcompany.com",
    'category': 'Project',
    'version': '0.1',
    'depends': ['base', 'nhan_su', 'quan_ly_du_an'],
    'data': [
        'security/ir.model.access.csv',
        'views/cong_viec.xml',
        'views/cong_viec_con.xml',
        'views/ghi_nhan_thoi_gian.xml',
        'views/danh_gia_cong_viec.xml',
        'views/du_an_inherit.xml',
        'views/nhiem_vu_inherit.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
