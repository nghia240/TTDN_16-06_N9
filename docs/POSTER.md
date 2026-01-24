## Poster – Hệ thống Quản trị mục tiêu (Odoo 15)

### Vấn đề cần giải quyết
- Chia nhỏ dự án thành các tác vụ nhỏ để theo dõi sát tiến độ
- Đo hiệu quả theo từng cá nhân dựa trên tiến độ + ghi nhận thời gian + KPI

### 3 module chính
- **`nhan_su`**: quản lý nhân viên, phòng ban, chức vụ, lịch sử công tác
- **`quan_ly_du_an`**: quản lý dự án (`du_an`) và nhiệm vụ (`nhiem_vu`)
- **`quan_ly_cong_viec`**: quản lý công việc (`cong_viec`) và công việc con (`cong_viec_con`), ghi nhận thời gian, đánh giá KPI

### Module tích hợp mới
- **`quan_tri_muc_tieu`**:
  - `muc_tieu`: mục tiêu theo nhân viên, theo giai đoạn
  - `muc_tieu_dong`: dòng mục tiêu liên kết trực tiếp **1 trong 3**: `nhiem_vu` / `cong_viec` / `cong_viec_con`
  - Tiến độ mục tiêu tự động tính từ tiến độ thực tế của task đã liên kết

### Luồng nghiệp vụ (end-to-end)
1. Tạo **Nhân viên** (nhan_su)
2. Tạo **Dự án** + thêm nhân viên tham gia (quan_ly_du_an)
3. Tạo **Nhiệm vụ** thuộc dự án (quan_ly_du_an)
4. Chia nhỏ nhiệm vụ thành **Công việc/Công việc con** và gán nhân viên (quan_ly_cong_viec)
5. Tạo **Mục tiêu** cho từng nhân viên, liên kết tới nhiệm vụ/công việc/công việc con (quan_tri_muc_tieu)
6. Theo dõi **tiến độ mục tiêu** và **tiến độ theo cá nhân** trực tiếp trên hồ sơ nhân viên

### Chỉ số theo dõi nhanh
- Tiến độ dự án: dựa trên trạng thái nhiệm vụ
- Tiến độ nhiệm vụ: `tien_do_pct` tính từ các công việc liên quan
- Tiến độ mục tiêu: trung bình có trọng số từ các dòng mục tiêu

### Gợi ý thiết kế Poster (A3/A2)
- Cột trái: bài toán + mục tiêu hệ thống
- Cột giữa: sơ đồ dữ liệu (du_an → nhiem_vu → cong_viec → cong_viec_con; nhan_vien liên kết)
- Cột phải: demo màn hình (Dự án / Nhiệm vụ / Công việc / Mục tiêu / Nhân viên)

