# 📊 Phân Tích Nghiệp Vụ & Kế Hoạch Phát Triển 3 Module

## 🎯 Yêu Cầu Chính: "Quản Trị Mục Tiêu"

**Mục tiêu**: Chia nhỏ dự án thành các tác vụ nhỏ để theo dõi sát sao tiến độ và hiệu quả của từng cá nhân.

---

## 📋 Phân Tích Nghiệp Vụ

### 1. Nghiệp Vụ "Quản Trị Mục Tiêu"

#### 1.1. Chia Nhỏ Dự Án Thành Tác Vụ
**Quy trình**:
```
DỰ ÁN
  └── NHIỆM VỤ (Nhiệm vụ lớn)
      └── CÔNG VIỆC (Công việc cụ thể)
          └── CÔNG VIỆC CON (Tác vụ nhỏ nhất - Task)
              └── GHI NHẬN THỜI GIAN (Theo dõi từng cá nhân)
```

**Yêu cầu**:
- Dự án → Nhiệm vụ → Công việc → Công việc con (đã có)
- Mỗi công việc con phải gán cho **1 nhân viên cụ thể**
- Theo dõi tiến độ từng công việc con
- Tổng hợp tiến độ lên công việc → nhiệm vụ → dự án

#### 1.2. Theo Dõi Tiến Độ Từng Cá Nhân
**Yêu cầu**:
- Xem tất cả công việc con của 1 nhân viên
- Xem tiến độ hoàn thành của nhân viên
- Xem số giờ làm việc của nhân viên trên từng công việc
- Đánh giá hiệu quả làm việc của nhân viên

#### 1.3. Đánh Giá Hiệu Quả Từng Cá Nhân
**Yêu cầu**:
- Tính KPI từ công việc hoàn thành
- So sánh tiến độ thực tế vs kế hoạch
- Đánh giá chất lượng công việc
- Báo cáo hiệu suất theo nhân viên

---

## 🔄 Nghiệp Vụ Kết Hợp Giữa Các Module

### 2.1. Module Nhân Sự ↔ Module Dự Án

**Luồng nghiệp vụ**:
1. **Phân công nhân viên vào dự án**:
   - Dự án có danh sách nhân viên tham gia (Many2many)
   - Mỗi nhiệm vụ có người phụ trách và người thực hiện
   - Mỗi công việc có nhân viên phụ trách

2. **Theo dõi công việc của nhân viên**:
   - Xem tất cả dự án nhân viên đang tham gia
   - Xem tất cả nhiệm vụ nhân viên đang thực hiện
   - Xem tất cả công việc nhân viên đang làm

3. **Đánh giá hiệu quả nhân viên**:
   - Tính số công việc hoàn thành
   - Tính số giờ làm việc trên dự án
   - Tính KPI từ tiến độ công việc

### 2.2. Module Nhân Sự ↔ Module Công Việc

**Luồng nghiệp vụ**:
1. **Phân công công việc**:
   - Mỗi công việc gán cho 1 nhân viên phụ trách
   - Mỗi công việc con gán cho 1 nhân viên cụ thể
   - Ghi nhận thời gian làm việc của nhân viên

2. **Theo dõi tiến độ**:
   - Xem tất cả công việc của nhân viên
   - Xem tiến độ từng công việc
   - Xem số giờ làm việc trên từng công việc

3. **Đánh giá công việc**:
   - Đánh giá công việc của nhân viên
   - Tính điểm KPI từ đánh giá
   - Lưu vào hồ sơ nhân viên

### 2.3. Module Dự Án ↔ Module Công Việc

**Luồng nghiệp vụ**:
1. **Liên kết dự án với công việc**:
   - Công việc có thể liên kết với dự án
   - Công việc có thể liên kết với nhiệm vụ
   - Tổng hợp tiến độ công việc lên nhiệm vụ/dự án

2. **Số hóa hồ sơ**:
   - Tài liệu dự án (hợp đồng, báo giá, pháp lý)
   - Tài liệu công việc (báo cáo, tài liệu liên quan)

---

## 🎯 Kế Hoạch Phát Triển Chi Tiết

### **GIAI ĐOẠN 1: Hoàn Thiện Module Nhân Sự** (Tuần 1-2)

#### 1.1. Mở Rộng Model Nhân Viên
**File**: `nhan_su/models/nhan_vien.py`

**Cần thêm**:
```python
# Thông tin cơ bản
phong_ban_id = fields.Many2one('phong_ban', string="Phòng ban")
chuc_vu_id = fields.Many2one('chuc_vu', string="Chức vụ")
ngay_vao_lam = fields.Date(string="Ngày vào làm")
ngay_nghi_viec = fields.Date(string="Ngày nghỉ việc")
muc_luong_co_ban = fields.Float(string="Mức lương cơ bản")
trang_thai = fields.Selection([
    ('dang_lam_viec', 'Đang làm việc'),
    ('thu_viec', 'Thử việc'),
    ('nghi_viec', 'Nghỉ việc'),
], default='dang_lam_viec')

# Liên kết với dự án và công việc (One2many ngược)
du_an_ids = fields.Many2many('du_an', string="Dự án tham gia")
cong_viec_ids = fields.Many2many('cong_viec', string="Công việc đang làm")
cong_viec_con_ids = fields.Many2many('cong_viec_con', string="Công việc con đang làm")

# Thống kê hiệu quả
tong_cong_viec_hoan_thanh = fields.Integer(
    string="Tổng công việc hoàn thành",
    compute="_compute_tong_cong_viec_hoan_thanh",
    store=True
)
tong_so_gio_lam_viec = fields.Float(
    string="Tổng số giờ làm việc",
    compute="_compute_tong_so_gio_lam_viec",
    store=True
)
diem_kpi_trung_binh = fields.Float(
    string="Điểm KPI trung bình",
    compute="_compute_diem_kpi_trung_binh",
    store=True
)
```

#### 1.2. Tạo Model Hợp Đồng Lao Động (Số Hóa)
**File**: `nhan_su/models/hop_dong_lao_dong.py` (MỚI)

```python
class HopDongLaoDong(models.Model):
    _name = 'hop_dong_lao_dong'
    _description = 'Hợp đồng Lao động'
    
    nhan_vien_id = fields.Many2one('nhan_vien', required=True)
    so_hop_dong = fields.Char(required=True)
    loai_hop_dong = fields.Selection([
        ('chinh_thuc', 'Chính thức'),
        ('thu_viec', 'Thử việc'),
        ('hop_tac', 'Hợp tác'),
    ])
    ngay_ky = fields.Date(required=True)
    ngay_het_han = fields.Date(required=True)
    muc_luong = fields.Float(string="Mức lương")
    
    # Số hóa hồ sơ
    file_hop_dong = fields.Binary(string="File hợp đồng", attachment=True)
    ten_file = fields.Char(string="Tên file")
    
    trang_thai = fields.Selection([
        ('dang_hieu_luc', 'Đang hiệu lực'),
        ('het_han', 'Hết hạn'),
        ('huy_bo', 'Hủy bỏ'),
    ], compute='_compute_trang_thai', store=True)
```

#### 1.3. Tạo Model Đánh Giá Hiệu Suất (KPI)
**File**: `nhan_su/models/danh_gia_hieu_suat.py` (MỚI)

```python
class DanhGiaHieuSuat(models.Model):
    _name = 'danh_gia_hieu_suat'
    _description = 'Đánh giá Hiệu suất (KPI)'
    
    nhan_vien_id = fields.Many2one('nhan_vien', required=True)
    thang = fields.Selection([...])
    nam = fields.Integer(required=True)
    
    # Tính từ công việc
    so_cong_viec_hoan_thanh = fields.Integer(
        compute='_compute_so_cong_viec_hoan_thanh',
        store=True
    )
    so_cong_viec_tong = fields.Integer(
        compute='_compute_so_cong_viec_tong',
        store=True
    )
    ti_le_hoan_thanh = fields.Float(
        string="Tỷ lệ hoàn thành (%)",
        compute='_compute_ti_le_hoan_thanh',
        store=True
    )
    
    # Tính từ đánh giá công việc
    diem_trung_binh = fields.Float(
        string="Điểm trung bình",
        compute='_compute_diem_trung_binh',
        store=True
    )
    
    # Tính từ thời gian làm việc
    tong_so_gio_lam_viec = fields.Float(
        compute='_compute_tong_so_gio',
        store=True
    )
    
    # Điểm KPI tổng hợp
    diem_kpi = fields.Float(
        string="Điểm KPI",
        compute='_compute_diem_kpi',
        store=True
    )
```

#### 1.4. Tạo Model Chấm Công
**File**: `nhan_su/models/cham_cong.py` (MỚI)

```python
class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm công'
    
    nhan_vien_id = fields.Many2one('nhan_vien', required=True)
    ngay_cham_cong = fields.Date(required=True, default=fields.Date.today)
    gio_vao = fields.Datetime(string="Giờ vào")
    gio_ra = fields.Datetime(string="Giờ ra")
    so_gio_lam_viec = fields.Float(
        string="Số giờ làm việc",
        compute='_compute_so_gio_lam_viec',
        store=True
    )
    cong_viec_ids = fields.Many2many(
        'cong_viec',
        string="Công việc đã làm"
    )
```

---

### **GIAI ĐOẠN 2: Mở Rộng Module Dự Án - Quản Trị Mục Tiêu** (Tuần 3-4)

#### 2.1. Cải Thiện Phân Công Nhân Viên
**File**: `quan_ly_du_an/models/nhiem_vu.py` (CẬP NHẬT)

**Cần cải thiện**:
- Đảm bảo mỗi nhiệm vụ có người phụ trách rõ ràng
- Thêm field: `nguoi_phu_trach_chinh_id` (Many2one - 1 người chính)
- Thêm field: `phan_cong_chi_tiet_ids` (One2many) để phân công chi tiết từng phần

#### 2.2. Tạo Model Phân Công Chi Tiết (Mới)
**File**: `quan_ly_du_an/models/phan_cong_chi_tiet.py` (MỚI)

```python
class PhanCongChiTiet(models.Model):
    _name = 'phan_cong_chi_tiet'
    _description = 'Phân công chi tiết nhiệm vụ'
    
    nhiem_vu_id = fields.Many2one('nhiem_vu', required=True)
    nhan_vien_id = fields.Many2one('nhan_vien', required=True)
    phan_cong = fields.Text(string="Phần công việc được giao")
    trong_so = fields.Float(string="Trọng số (%)", default=100.0)
    tien_do = fields.Float(string="Tiến độ (%)", default=0.0)
    ngay_bat_dau = fields.Date()
    ngay_ket_thuc = fields.Date()
    trang_thai = fields.Selection([
        ('chua_bat_dau', 'Chưa bắt đầu'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
    ], default='chua_bat_dau')
```

#### 2.3. Tạo Model Tài Liệu Dự Án (Số Hóa Hồ Sơ)
**File**: `quan_ly_du_an/models/tai_lieu_du_an.py` (MỚI)

```python
class TaiLieuDuAn(models.Model):
    _name = 'tai_lieu_du_an'
    _description = 'Tài liệu Dự án'
    
    du_an_id = fields.Many2one('du_an', required=True)
    ten_tai_lieu = fields.Char(required=True)
    loai_tai_lieu = fields.Selection([
        ('hop_dong', 'Hợp đồng dự án'),
        ('bao_gia', 'Báo giá dự án'),
        ('tai_lieu_phap_ly', 'Tài liệu pháp lý'),
        ('bao_cao', 'Báo cáo'),
        ('khac', 'Khác'),
    ], required=True)
    
    # Số hóa hồ sơ
    file_tai_lieu = fields.Binary(required=True, attachment=True)
    ten_file = fields.Char()
    ngay_upload = fields.Date(default=fields.Date.today)
    nguoi_upload_id = fields.Many2one('res.users', default=lambda self: self.env.user)
```

#### 2.4. Thêm Dashboard Theo Dõi Nhân Viên
**File**: `quan_ly_du_an/models/du_an.py` (CẬP NHẬT)

**Thêm các field thống kê**:
```python
# Thống kê theo nhân viên
nhan_vien_tien_do_ids = fields.One2many(
    'nhan_vien_tien_do',
    'du_an_id',
    string="Tiến độ theo nhân viên"
)

# Compute tiến độ từng nhân viên
def _compute_tien_do_nhan_vien(self):
    for rec in self:
        # Tính tiến độ từng nhân viên trong dự án
        ...
```

---

### **GIAI ĐOẠN 3: Mở Rộng Module Công Việc - Theo Dõi Cá Nhân** (Tuần 5-6)

#### 3.1. Cải Thiện Phân Công Công Việc Con
**File**: `quan_ly_cong_viec/models/cong_viec_con.py` (CẬP NHẬT)

**Cần cải thiện**:
- Đảm bảo mỗi công việc con có 1 nhân viên cụ thể (required=True)
- Thêm field: `ngay_bat_dau_thuc_te`, `ngay_ket_thuc_thuc_te`
- Thêm field: `so_gio_du_kien`, `so_gio_thuc_te`
- Tính hiệu quả: so sánh thời gian thực tế vs dự kiến

#### 3.2. Mở Rộng Model Ghi Nhận Thời Gian
**File**: `quan_ly_cong_viec/models/ghi_nhan_thoi_gian.py` (CẬP NHẬT)

**Cần thêm**:
```python
cong_viec_con_id = fields.Many2one(
    'cong_viec_con',
    string="Công việc con",
    help="Ghi nhận thời gian cho công việc con cụ thể"
)
# Đã có: cong_viec_id, nhan_vien_id, so_gio_lam_viec, ngay_ghi_nhan
```

#### 3.3. Tạo Model Tài Liệu Công Việc (Số Hóa Hồ Sơ)
**File**: `quan_ly_cong_viec/models/tai_lieu_cong_viec.py` (MỚI)

```python
class TaiLieuCongViec(models.Model):
    _name = 'tai_lieu_cong_viec'
    _description = 'Tài liệu Công việc'
    
    cong_viec_id = fields.Many2one('cong_viec', required=True)
    ten_tai_lieu = fields.Char(required=True)
    loai_tai_lieu = fields.Selection([
        ('bao_cao', 'Báo cáo công việc'),
        ('tai_lieu_lien_quan', 'Tài liệu liên quan'),
        ('tai_lieu_phap_ly', 'Tài liệu pháp lý'),
        ('khac', 'Khác'),
    ], required=True)
    
    # Số hóa hồ sơ
    file_tai_lieu = fields.Binary(required=True, attachment=True)
    ten_file = fields.Char()
    ngay_upload = fields.Date(default=fields.Date.today)
    nguoi_upload_id = fields.Many2one('res.users', default=lambda self: self.env.user)
```

#### 3.4. Mở Rộng Đánh Giá Công Việc
**File**: `quan_ly_cong_viec/models/danh_gia_cong_viec.py` (CẬP NHẬT)

**Cần thêm**:
```python
diem_so = fields.Float(string="Điểm số (1-10)", required=True)
nhan_xet_chi_tiet = fields.Text(string="Nhận xét chi tiết")
file_danh_gia = fields.Binary(string="File đánh giá", attachment=True)
nguoi_danh_gia_id = fields.Many2one('nhan_vien', string="Người đánh giá")
```

---

### **GIAI ĐOẠN 4: Dashboard & Báo Cáo Theo Dõi Cá Nhân** (Tuần 7-8)

#### 4.1. Dashboard Nhân Viên
**File**: `nhan_su/views/dashboard_nhan_vien.xml` (MỚI)

**Hiển thị**:
- Tổng số công việc đang làm
- Tiến độ trung bình
- Số giờ làm việc trong tháng
- Điểm KPI hiện tại
- Danh sách công việc sắp đến hạn

#### 4.2. Báo Cáo Hiệu Quả Nhân Viên
**File**: `nhan_su/views/bao_cao_hieu_qua.xml` (MỚI)

**Báo cáo**:
- Số công việc hoàn thành vs tổng số
- Tỷ lệ hoàn thành đúng hạn
- Điểm KPI theo tháng/quý
- So sánh với nhân viên khác

#### 4.3. Dashboard Dự Án - Theo Dõi Nhân Viên
**File**: `quan_ly_du_an/views/dashboard_du_an.xml` (MỚI)

**Hiển thị**:
- Tiến độ từng nhân viên trong dự án
- Số giờ làm việc của từng nhân viên
- Công việc đang làm của từng nhân viên
- Cảnh báo công việc trễ hạn

---

## 📋 Checklist Phát Triển

### Module Nhân Sự (`nhan_su`)
- [ ] Mở rộng model `nhan_vien` (phòng ban, chức vụ, thống kê)
- [ ] Model `hop_dong_lao_dong` (hợp đồng + upload file)
- [ ] Model `danh_gia_hieu_suat` (KPI từ công việc)
- [ ] Model `cham_cong` (chấm công)
- [ ] Dashboard nhân viên
- [ ] Báo cáo hiệu quả nhân viên
- [ ] Views và menu

### Module Dự Án (`quan_ly_du_an`)
- [ ] Model `phan_cong_chi_tiet` (phân công chi tiết nhiệm vụ)
- [ ] Model `tai_lieu_du_an` (tài liệu + upload file) ⭐
- [ ] Cải thiện phân công nhân viên trong nhiệm vụ
- [ ] Dashboard theo dõi nhân viên trong dự án
- [ ] View hiển thị tài liệu trong form dự án
- [ ] Báo cáo tiến độ theo nhân viên

### Module Công Việc (`quan_ly_cong_viec`)
- [ ] Cải thiện model `cong_viec_con` (theo dõi thời gian thực tế)
- [ ] Model `tai_lieu_cong_viec` (tài liệu + upload file) ⭐
- [ ] Mở rộng `ghi_nhan_thoi_gian` (liên kết với công việc con)
- [ ] Mở rộng `danh_gia_cong_viec` (điểm số, file đánh giá)
- [ ] View hiển thị tài liệu trong form công việc
- [ ] Báo cáo công việc theo nhân viên

---

## 🎯 Kết Quả Mong Đợi

Sau khi hoàn thành:

1. ✅ **Quản trị mục tiêu hoàn chỉnh**:
   - Dự án → Nhiệm vụ → Công việc → Công việc con (tác vụ nhỏ)
   - Mỗi tác vụ gán cho 1 nhân viên cụ thể
   - Theo dõi tiến độ từng tác vụ

2. ✅ **Theo dõi sát sao từng cá nhân**:
   - Xem tất cả công việc của nhân viên
   - Xem tiến độ từng công việc
   - Xem số giờ làm việc
   - Đánh giá hiệu quả

3. ✅ **Số hóa hồ sơ**:
   - Tài liệu dự án (hợp đồng, báo giá, pháp lý)
   - Tài liệu công việc (báo cáo, tài liệu liên quan)
   - Hợp đồng lao động

4. ✅ **Module Nhân sự hoàn chỉnh**:
   - Quản lý đầy đủ thông tin nhân viên
   - Hợp đồng lao động (số hóa)
   - Đánh giá hiệu suất (KPI)
   - Chấm công

5. ✅ **Dashboard & Báo cáo**:
   - Dashboard nhân viên
   - Dashboard dự án
   - Báo cáo hiệu quả theo nhân viên

---

## 🚀 Bắt Đầu Phát Triển

### Bước 1: Hoàn thiện Module Nhân Sự
Bắt đầu với việc mở rộng model `nhan_vien` và tạo các model mới.

### Bước 2: Cải thiện Phân Công & Theo Dõi
Thêm phân công chi tiết và theo dõi tiến độ từng cá nhân.

### Bước 3: Số hóa Hồ sơ
Tạo model tài liệu cho dự án và công việc.

### Bước 4: Dashboard & Báo cáo
Tạo dashboard và báo cáo để theo dõi hiệu quả.

