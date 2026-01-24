# -*- coding: utf-8 -*-

{
    'name': 'quan_ly_du_an',
    'summary': 'Quản lý dự án, nhiệm vụ và tiến độ',
    'description': 'Hệ thống quản lý dự án đơn giản',
    'author': 'phuccthuan',
    'website': 'http://www.yourcompany.com',
    'category': 'Project',
    'version': '0.1',

    'depends': [
        'base',
        'mail',
        'web',
        'board',
        'nhan_su',
    ],

    'data': [
        # ===== SECURITY =====
        'security/ir.model.access.csv',

        # ===== VIEWS + ACTIONS =====
        'views/du_an.xml',
        'views/nhiem_vu.xml',
        'views/thoi_gian_lam_viec.xml',
        'views/tien_do.xml',
        'views/rui_ro.xml',
        'views/tre_han.xml',
        'views/dashboard.xml',

        # ===== MENUS (LUÔN CUỐI) =====
        'views/menu.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
