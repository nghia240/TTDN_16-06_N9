# Hướng dẫn Test Tích Hợp 2 Module

## Tổng quan tích hợp

Hai module `quan_ly_cong_viec` và `quan_ly_du_an` đã được tích hợp với các liên kết sau:

### 1. Liên kết Công việc ↔ Dự án/Nhiệm vụ
- **Công việc** (`cong_viec`) có thể liên kết với:
  - **Dự án** (`du_an`) - field `du_an_id`
  - **Nhiệm vụ** (`nhiem_vu`) - field `nhiem_vu_id`

- **Công việc con** (`cong_viec_con`) có thể liên kết với:
  - **Nhiệm vụ** (`nhiem_vu`) - field `nhiem_vu_id`

### 2. Liên kết ngược lại
- **Dự án** có thể xem tất cả công việc liên quan qua tab "Công việc liên quan"
- **Nhiệm vụ** có thể xem tất cả công việc và công việc con liên quan qua tab "Công việc liên quan"

## Các bước test

### Bước 1: Cập nhật module
```bash
# Cập nhật cả 2 module
python3 odoo-bin -c odoo.conf -d ten_database -u quan_ly_cong_viec,quan_ly_du_an --stop-after-init
```

### Bước 2: Tạo dữ liệu test

#### 2.1. Tạo Dự án
1. Vào **Quản lý dự án** → **Dự án** → **Danh sách dự án**
2. Tạo mới một dự án:
   - Tên dự án: "Dự án Test Tích Hợp"
   - Ngân sách: 1000000
   - Ngày bắt đầu: Hôm nay
   - Ngày kết thúc: 30 ngày sau
   - Mức ưu tiên: Cao

#### 2.2. Tạo Nhiệm vụ
1. Vào **Quản lý dự án** → **Dự án** → **Quản lý nhiệm vụ**
2. Tạo mới một nhiệm vụ:
   - Tên nhiệm vụ: "Nhiệm vụ Test"
   - Dự án: Chọn dự án vừa tạo
   - Ngày bắt đầu: Hôm nay
   - Hạn chót: 15 ngày sau
   - Mức ưu tiên: Cao

#### 2.3. Tạo Công việc liên kết với Dự án
1. Vào **Quản lý công việc** → **Công việc**
2. Tạo mới một công việc:
   - Tên công việc: "Công việc Test - Liên kết Dự án"
   - **Dự án**: Chọn dự án vừa tạo ← **KIỂM TRA LIÊN KẾT**
   - Nhân viên phụ trách: Chọn một nhân viên
   - Trạng thái: Mới
   - Hạn hoàn thành: 20 ngày sau
   - Tiến độ: 0%
   - Ngày bắt đầu: Hôm nay
   - Ngày kết thúc: 20 ngày sau

#### 2.4. Tạo Công việc liên kết với Nhiệm vụ
1. Tạo mới một công việc khác:
   - Tên công việc: "Công việc Test - Liên kết Nhiệm vụ"
   - **Nhiệm vụ**: Chọn nhiệm vụ vừa tạo ← **KIỂM TRA LIÊN KẾT**
   - Nhân viên phụ trách: Chọn một nhân viên
   - Trạng thái: Đang thực hiện
   - Hạn hoàn thành: 10 ngày sau
   - Tiến độ: 30%

#### 2.5. Tạo Công việc con liên kết với Nhiệm vụ
1. Vào **Quản lý công việc** → **Công việc con**
2. Tạo mới một công việc con:
   - Công việc: Chọn một công việc
   - **Nhiệm vụ**: Chọn nhiệm vụ vừa tạo ← **KIỂM TRA LIÊN KẾT**
   - Tên công việc con: "Công việc con Test"
   - Nhân viên phụ trách: Chọn một nhân viên
   - Trạng thái: Mới
   - Hạn hoàn thành: 5 ngày sau
   - Tiến độ: 0%

### Bước 3: Kiểm tra liên kết ngược

#### 3.1. Kiểm tra từ Dự án
1. Vào **Quản lý dự án** → **Dự án** → **Danh sách dự án**
2. Mở dự án "Dự án Test Tích Hợp"
3. Kiểm tra tab **"Công việc liên quan"**:
   - Phải thấy công việc "Công việc Test - Liên kết Dự án"
   - Kiểm tra số lượng công việc hiển thị đúng

#### 3.2. Kiểm tra từ Nhiệm vụ
1. Vào **Quản lý dự án** → **Dự án** → **Quản lý nhiệm vụ**
2. Mở nhiệm vụ "Nhiệm vụ Test"
3. Kiểm tra tab **"Công việc liên quan"**:
   - Phải thấy công việc "Công việc Test - Liên kết Nhiệm vụ"
   - Phải thấy công việc con "Công việc con Test"
   - Kiểm tra số lượng công việc hiển thị đúng

### Bước 4: Kiểm tra tìm kiếm và lọc

#### 4.1. Tìm kiếm Công việc theo Dự án
1. Vào **Quản lý công việc** → **Công việc**
2. Trong ô tìm kiếm, nhập tên dự án
3. Kiểm tra kết quả hiển thị đúng

#### 4.2. Tìm kiếm Công việc theo Nhiệm vụ
1. Trong danh sách công việc
2. Trong ô tìm kiếm, nhập tên nhiệm vụ
3. Kiểm tra kết quả hiển thị đúng

#### 4.3. Tìm kiếm Công việc con theo Nhiệm vụ
1. Vào **Quản lý công việc** → **Công việc con**
2. Trong ô tìm kiếm, nhập tên nhiệm vụ
3. Kiểm tra kết quả hiển thị đúng

### Bước 5: Kiểm tra tính toán tự động

#### 5.1. Kiểm tra số lượng công việc trong Dự án
1. Mở dự án
2. Kiểm tra field **"Số lượng công việc"** phải hiển thị đúng số lượng

#### 5.2. Kiểm tra số lượng công việc trong Nhiệm vụ
1. Mở nhiệm vụ
2. Kiểm tra field **"Số lượng công việc"** phải hiển thị đúng số lượng (bao gồm cả công việc và công việc con)

## Checklist Test

- [ ] Tạo được công việc liên kết với dự án
- [ ] Tạo được công việc liên kết với nhiệm vụ
- [ ] Tạo được công việc con liên kết với nhiệm vụ
- [ ] Xem được công việc từ dự án (tab "Công việc liên quan")
- [ ] Xem được công việc từ nhiệm vụ (tab "Công việc liên quan")
- [ ] Tìm kiếm công việc theo dự án hoạt động đúng
- [ ] Tìm kiếm công việc theo nhiệm vụ hoạt động đúng
- [ ] Số lượng công việc hiển thị đúng trong dự án
- [ ] Số lượng công việc hiển thị đúng trong nhiệm vụ
- [ ] Không có lỗi khi lưu/xóa các bản ghi liên kết

## Lưu ý

1. **Dependency**: Module `quan_ly_cong_viec` phụ thuộc vào `quan_ly_du_an`, nên cần cài đặt `quan_ly_du_an` trước
2. **Module nhan_su**: Cả 2 module đều cần module `nhan_su` để sử dụng model `nhan_vien`
3. **Cập nhật module**: Sau khi sửa code, nhớ cập nhật module để áp dụng thay đổi

## Troubleshooting

### Lỗi: "Model không tồn tại"
- Kiểm tra đã cài đặt đầy đủ các module: `nhan_su`, `quan_ly_du_an`, `quan_ly_cong_viec`
- Cập nhật lại module: `-u quan_ly_cong_viec,quan_ly_du_an`

### Lỗi: "Field không tồn tại"
- Kiểm tra đã cập nhật module sau khi thêm field
- Xóa cache và cập nhật lại module

### Không thấy tab "Công việc liên quan"
- Kiểm tra đã cập nhật module
- Kiểm tra view XML đã được load đúng

