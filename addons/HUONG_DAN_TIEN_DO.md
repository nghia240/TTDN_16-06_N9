# Hướng dẫn về Tiến độ trong hệ thống

## 📊 Các loại Tiến độ

### 1. **Tiến độ Công việc** (`tien_do`) - ✅ CÓ THỂ CHỈNH SỬA

**Vị trí**: Form Công việc → Field "Tiến độ %"

**Cách chỉnh sửa**:
1. Vào **Quản lý công việc** → **Công việc**
2. Mở công việc cần cập nhật
3. Click vào field **"Tiến độ %"**
4. Nhập giá trị từ 0 đến 100 (ví dụ: 50 = 50%)
5. Click **Lưu**

**Lưu ý**: 
- Field này là **nhập tay**, bạn tự cập nhật
- Giá trị từ 0 đến 100 (%)

---

### 2. **Tiến độ Công việc con** (`tien_do`) - ✅ CÓ THỂ CHỈNH SỬA

**Vị trí**: Form Công việc con → Field "Tiến độ %"

**Cách chỉnh sửa**:
1. Vào **Quản lý công việc** → **Công việc con**
2. Mở công việc con cần cập nhật
3. Click vào field **"Tiến độ %"**
4. Nhập giá trị từ 0 đến 100
5. Click **Lưu**

---

### 3. **Tiến độ tự động từ Công việc con** (`tien_do_tu_dong`) - ⚠️ CHỈ ĐỌC

**Vị trí**: Form Công việc → Field "Tiến độ tự động (%)"

**Giải thích**:
- Field này **tự động tính** từ tiến độ của các công việc con
- Công thức: Trung bình tiến độ của tất cả công việc con
- **Không thể chỉnh sửa** (readonly)
- Chỉ hiển thị khi công việc có công việc con

**Ví dụ**:
- Công việc con 1: 30%
- Công việc con 2: 50%
- Công việc con 3: 70%
- → Tiến độ tự động = (30 + 50 + 70) / 3 = **50%**

---

### 4. **Tiến độ Dự án** (`tien_do_du_an`) - ⚠️ CHỈ ĐỌC (Computed)

**Vị trí**: Form Dự án → Field "Tiến độ (%)" (có widget progressbar)

**Giải thích**:
- Field này **tự động tính** từ trạng thái của các nhiệm vụ
- Công thức: (Số nhiệm vụ hoàn thành / Tổng số nhiệm vụ) × 100
- **Không thể chỉnh sửa** (readonly)
- Hiển thị dưới dạng progressbar (thanh tiến độ)

**Cách cập nhật gián tiếp**:
1. Vào **Quản lý dự án** → **Quản lý nhiệm vụ**
2. Thay đổi trạng thái nhiệm vụ thành **"Hoàn thành"**
3. Tiến độ dự án sẽ tự động cập nhật

---

## 🔧 Cách sử dụng Tiến độ hiệu quả

### **Tùy chọn 1: Nhập tay tiến độ**
- Chỉnh sửa trực tiếp field **"Tiến độ %"** trong form Công việc/Công việc con
- Phù hợp khi bạn muốn kiểm soát chính xác giá trị

### **Tùy chọn 2: Sử dụng tiến độ tự động**
1. Tạo các công việc con
2. Cập nhật tiến độ cho từng công việc con
3. Xem **"Tiến độ tự động"** để tham khảo
4. Có thể copy giá trị này vào **"Tiến độ %"** nếu muốn đồng bộ

### **Tùy chọn 3: Đồng bộ tiến độ**
- Nếu muốn tiến độ công việc tự động = tiến độ tự động:
  1. Xem giá trị **"Tiến độ tự động"**
  2. Copy giá trị đó
  3. Paste vào field **"Tiến độ %"**
  4. Lưu

---

## ❓ Câu hỏi thường gặp

### Q: Tại sao không thể chỉnh sửa tiến độ Dự án?
**A**: Tiến độ Dự án được tính tự động từ nhiệm vụ để đảm bảo tính chính xác. Bạn cần hoàn thành nhiệm vụ để tăng tiến độ.

### Q: Tiến độ tự động có cập nhật real-time không?
**A**: Có, mỗi khi bạn thay đổi tiến độ công việc con, tiến độ tự động sẽ tự động cập nhật.

### Q: Có thể làm cho tiến độ công việc tự động = tiến độ tự động không?
**A**: Hiện tại bạn cần copy thủ công. Nếu muốn tự động, có thể yêu cầu thêm tính năng này.

---

## 💡 Mẹo sử dụng

1. **Sử dụng tiến độ tự động làm tham chiếu**: Xem tiến độ tự động để biết trung bình, sau đó quyết định có cập nhật tiến độ chính không.

2. **Cập nhật thường xuyên**: Để có báo cáo chính xác, nên cập nhật tiến độ công việc con thường xuyên.

3. **Kiểm tra tiến độ dự án**: Tiến độ dự án phản ánh tổng thể, nên kiểm tra định kỳ để đảm bảo dự án đúng tiến độ.

