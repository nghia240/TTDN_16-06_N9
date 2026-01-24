#!/bin/bash
# Script để kill process Odoo đang chạy trên port 8069

echo "Đang tìm process Odoo trên port 8069..."

# Tìm PID của process đang sử dụng port 8069
PID=$(lsof -ti:8069 2>/dev/null || fuser 8069/tcp 2>/dev/null | awk '{print $2}')

if [ -z "$PID" ]; then
    echo "Không tìm thấy process nào đang sử dụng port 8069"
    echo "Đang tìm process odoo-bin..."
    PID=$(ps aux | grep odoo-bin | grep -v grep | awk '{print $2}' | head -1)
fi

if [ -z "$PID" ]; then
    echo "Không tìm thấy process Odoo nào đang chạy"
    exit 0
fi

echo "Tìm thấy process với PID: $PID"
echo "Đang kill process..."

kill -9 $PID 2>/dev/null

sleep 2

# Kiểm tra lại
if ps -p $PID > /dev/null 2>&1; then
    echo "Không thể kill process $PID"
    exit 1
else
    echo "Đã kill thành công process $PID"
    echo "Bây giờ bạn có thể chạy lại Odoo"
fi

