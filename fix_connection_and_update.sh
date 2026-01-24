#!/bin/bash
# Script để kiểm tra và sửa lỗi kết nối database + cập nhật module

echo "=== KIỂM TRA VÀ SỬA LỖI ODOO ==="
echo ""

# 1. Kiểm tra PostgreSQL có chạy không
echo "1. Kiểm tra PostgreSQL service..."
if systemctl is-active --quiet postgresql || service postgresql status > /dev/null 2>&1; then
    echo "   ✓ PostgreSQL đang chạy"
else
    echo "   ✗ PostgreSQL chưa chạy. Đang khởi động..."
    sudo systemctl start postgresql || sudo service postgresql start
    sleep 2
fi

# 2. Kiểm tra database
echo ""
echo "2. Kiểm tra database 'odoo'..."
DB_EXISTS=$(sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -w odoo | wc -l)

if [ "$DB_EXISTS" -eq "0" ]; then
    echo "   ✗ Database 'odoo' chưa tồn tại"
    echo "   Đang tạo database..."
    sudo -u postgres createdb -O odoo odoo
    echo "   ✓ Đã tạo database 'odoo'"
else
    echo "   ✓ Database 'odoo' đã tồn tại"
fi

# 3. Dừng Odoo nếu đang chạy
echo ""
echo "3. Kiểm tra Odoo đang chạy..."
PID=$(lsof -ti:8069 2>/dev/null || fuser 8069/tcp 2>/dev/null | awk '{print $2}')
if [ ! -z "$PID" ]; then
    echo "   Đang dừng Odoo (PID: $PID)..."
    kill -9 $PID 2>/dev/null
    sleep 2
    echo "   ✓ Đã dừng Odoo"
else
    echo "   ✓ Odoo chưa chạy"
fi

# 4. Cập nhật module
echo ""
echo "4. Đang cập nhật module quan_ly_du_an và quan_ly_cong_viec..."
python3 odoo-bin.py -c odoo.conf -d odoo -u quan_ly_du_an,quan_ly_cong_viec --stop-after-init

if [ $? -eq 0 ]; then
    echo "   ✓ Cập nhật module thành công!"
else
    echo "   ✗ Có lỗi khi cập nhật module. Kiểm tra log ở trên."
    exit 1
fi

echo ""
echo "=== HOÀN TẤT ==="
echo ""
echo "Bây giờ bạn có thể chạy lại Odoo:"
echo "  python3 odoo-bin.py -c odoo.conf -d odoo"
echo ""
echo "Hoặc nếu muốn chạy ở chế độ nền:"
echo "  nohup python3 odoo-bin.py -c odoo.conf -d odoo > odoo.log 2>&1 &"

