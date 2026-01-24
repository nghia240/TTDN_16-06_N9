#!/bin/bash
# Script để cập nhật module quan_ly_du_an và quan_ly_cong_viec

echo "Đang cập nhật module quan_ly_du_an và quan_ly_cong_viec..."
echo ""

# Dừng Odoo nếu đang chạy
echo "Kiểm tra Odoo đang chạy..."
PID=$(lsof -ti:8069 2>/dev/null || fuser 8069/tcp 2>/dev/null | awk '{print $2}')
if [ ! -z "$PID" ]; then
    echo "Đang dừng Odoo (PID: $PID)..."
    kill -9 $PID 2>/dev/null
    sleep 2
fi

# Cập nhật module
echo "Đang cập nhật module..."
python3 odoo-bin.py -c odoo.conf -d odoo -u quan_ly_du_an,quan_ly_cong_viec --stop-after-init

echo ""
echo "Cập nhật hoàn tất!"
echo "Bây giờ bạn có thể chạy lại Odoo:"
echo "python3 odoo-bin.py -c odoo.conf -d odoo"

