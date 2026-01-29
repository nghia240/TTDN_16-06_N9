# 🚀 Hệ thống Quản lý Dự án, Công việc và Nhân sự trên Odoo 15

[![Odoo Version](https://img.shields.io/badge/Odoo-15.0-blue)](https://www.odoo.com/)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success)](https://github.com)

> Hệ thống quản lý dự án, công việc và nhân sự tích hợp trên nền tảng Odoo 15, hỗ trợ quản trị mục tiêu và theo dõi hiệu quả cá nhân.

---

## 📋 Mục lục

* [Giới thiệu](#-giới-thiệu)
* [Tính năng chính](#-tính-năng-chính)
* [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
* [Cài đặt](#-cài-đặt)
* [Cấu trúc dự án](#-cấu-trúc-dự-án)
* [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
* [Screenshots](#-screenshots)
* [Modules](#-modules)
* [Đóng góp](#-đóng-góp)
* [Tác giả](#-tác-giả)
* [Tài liệu tham khảo](#-tài-liệu-tham-khảo)
* [License](#-license)

---

## 🎯 Giới thiệu

Hệ thống được xây dựng nhằm giải quyết các thách thức trong quản lý dự án và nhân sự tại doanh nghiệp:

* **Quản trị mục tiêu**: Chia nhỏ dự án thành các tác vụ để theo dõi tiến độ
* **Theo dõi hiệu quả**: Đánh giá hiệu suất thông qua KPI và thời gian làm việc
* **Tích hợp thống nhất**: Các module liên kết chặt chẽ, đảm bảo dữ liệu nhất quán

### 🌟 Đặc điểm nổi bật

#### ✨ Tự động hóa thông minh

* Tự động tính tiến độ dự án
* Cảnh báo nhiệm vụ trễ hạn
* Tự động điền dữ liệu

#### 📊 Dashboard trực quan

* Biểu đồ trạng thái dự án
* Biểu đồ mức độ ưu tiên
* Thanh tiến độ (Progress Bar)

#### 🔗 Tích hợp chặt chẽ

* Liên kết qua inheritance & dependencies
* Chia sẻ dữ liệu, hạn chế trùng lặp

---

## ✨ Tính năng chính

### 👥 Module Quản lý Nhân sự

* ✅ Quản lý thông tin nhân viên
* ✅ Quản lý phòng ban, chức vụ
* ✅ Lịch sử công tác
* ✅ Validation dữ liệu

### 📁 Module Quản lý Dự án

* ✅ Quản lý dự án (ngân sách, thời gian, ưu tiên)
* ✅ Quản lý nhiệm vụ
* ✅ Tính tiến độ tự động
* ✅ Quản lý rủi ro
* ✅ Cảnh báo trễ hạn
* ✅ Dashboard thống kê

### 📝 Module Quản lý Công việc

* ✅ Quản lý công việc & công việc con
* ✅ Ghi nhận thời gian
* ✅ Đánh giá KPI
* ✅ Tích hợp dự án
* ✅ Tính tiến độ tự động

---

## 💻 Yêu cầu hệ thống

* **Python**: ≥ 3.8
* **PostgreSQL**: ≥ 12
* **Odoo**: 15.0 Community
* **Hệ điều hành**: Linux / macOS / Windows (WSL)

### Dependencies

* Core: `base`, `mail`, `web`, `board`
* Python: Theo `requirements.txt` của Odoo

---

## 🚀 Cài đặt

### Bước 1: Clone repository

```bash
git clone https://github.com/your-username/odoo15-project-management.git
cd odoo15-project-management
```

### Bước 2: Cài đặt Odoo 15

Tham khảo tài liệu chính thức của Odoo.

### Bước 3: Cấu hình Odoo

File `odoo.conf`:

```ini
[options]
addons_path = /path/to/odoo/addons,/path/to/odoo15-project-management/addons
```

### Bước 4: Khởi động Odoo

```bash
./odoo-bin -c odoo.conf
```

### Bước 5: Cài đặt module

1. Truy cập: `http://localhost:8069`
2. Đăng nhập Admin
3. Vào **Apps → Update Apps List**
4. Cài theo thứ tự:

   * `nhan_su`
   * `quan_ly_du_an`
   * `quan_ly_cong_viec`

> ⚠️ Cần cài đúng thứ tự để tránh lỗi dependencies.

### Bước 6: Upgrade module

```bash
./odoo-bin -c odoo.conf -u nhan_su,quan_ly_du_an,quan_ly_cong_viec -d database_name
```

---

## 📁 Cấu trúc dự án

```
odoo15-project-management/
├── addons/
│   ├── nhan_su/
│   ├── quan_ly_du_an/
│   └── quan_ly_cong_viec/
├── README.md
└── LICENSE
```

---

## 📖 Hướng dẫn sử dụng

### Quy trình quản lý dự án

#### 1. Tạo dự án

* Quản lý dự án → Dự án → Create
* Nhập thông tin cơ bản

#### 2. Tạo nhiệm vụ

* Tab **Nhiệm vụ** → Add a line
* Gán người phụ trách

#### 3. Tạo công việc

* Quản lý công việc → Công việc → Create
* Liên kết dự án

#### 4. Ghi nhận thời gian

* Theo dõi → Ghi nhận thời gian
* Nhập số giờ làm việc

#### 5. Đánh giá KPI

* Theo dõi → Đánh giá công việc
* Nhập KPI, nhận xét

### Xem thống kê

* Quản lý dự án → Dashboard
* Xem biểu đồ tổng hợp

### Quản lý trễ hạn

* Quản lý dự án → Quản lý trễ hạn
* Theo dõi và xử lý kịp thời

---

## 📸 Screenshots

```
screenshots/
├── dashboard.png
├── danh_sach_du_an.png
├── form_du_an.png
├── danh_sach_nhiem_vu.png
├── form_nhiem_vu.png
├── danh_sach_cong_viec.png
├── ghi_nhan_thoi_gian.png
├── danh_sach_nhan_vien.png
├── lich_su_cong_tac.png
```

![Dashboard hệ thống](Screenshots/GiaoDienQuanLyNhanVien.png)
*Giao diện Quản lý nhân viên*


---

## 📦 Modules

### 🧩 nhan_su

**Chức năng:** Quản lý nhân viên

**Models:**

* nhan_vien
* phong_ban
* chuc_vu
* lich_su_cong_tac

**Dependencies:** `base`

---

### 🧩 quan_ly_du_an

**Chức năng:** Quản lý dự án, nhiệm vụ

**Models:**

* du_an
* nhiem_vu
* tien_do
* rui_ro
* tre_han

**Dependencies:** `base`, `mail`, `web`, `board`, `nhan_su`

---

### 🧩 quan_ly_cong_viec

**Chức năng:** Quản lý công việc, KPI

**Models:**

* cong_viec
* cong_viec_con
* ghi_nhan_thoi_gian
* danh_gia_cong_viec

**Dependencies:** `base`, `nhan_su`, `quan_ly_du_an`

---

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp:

1. Fork project
2. Tạo branch mới
3. Commit thay đổi
4. Push lên GitHub
5. Tạo Pull Request


## 📚 Tài liệu tham khảo

1. Odoo Documentation (15.0)
2. Python Documentation
3. PostgreSQL Documentation
4. Git & GitHub Docs
5. Stack Overflow (Odoo)

---

## 📄 License

Dự án được phát hành theo giấy phép **MIT License**.

Xem file `LICENSE` để biết thêm chi tiết.
