# -*- coding: utf-8 -*-
{
    'name': "Quản lý nhân sự",
    'summary': "Hệ thống quản lý nhân viên, phòng ban, chức vụ và lịch sử công tác",
    'description': """
        Module quản lý nhân sự bao gồm:
        - Quản lý thông tin nhân viên
        - Quản lý phòng ban
        - Quản lý chức vụ
        - Lịch sử công tác của nhân viên
    """,
    'author': "phuccthuan",
    'website': "http://www.yourcompany.com",
    'category': 'Human Resources',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/lich_su_cong_tac.xml',
        'views/nhan_vien.xml',
        'views/phong_ban.xml',
        'views/chuc_vu.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
