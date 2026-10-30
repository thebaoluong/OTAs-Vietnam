import pandas as pd
from datetime import datetime

# Sample empirical dataset for Master's thesis / OTA management
data = [
    {
        "Mã Đơn Hàng": "VJ10294",
        "Thời Gian Đặt": "2026-10-30 08:30:15",
        "Họ và Tên Khách Hàng": "Nguyễn Văn An",
        "Số Điện Thoại": "0912345678",
        "Email Nhận Vé": "an.nguyen@gmail.com",
        "Tên Tour Đã Đặt": "Khám Phá Sa Pa - Đỉnh Fansipan - Bản Cát Cát 3N2Đ",
        "Vùng Miền": "Miền Bắc",
        "Đơn Vị Điều Hành (Operator)": "Sa Pa Eco-Tours Vietnam",
        "Ngày Khởi Hành": "2026-11-05",
        "Số Khách": 2,
        "Đơn Giá (VNĐ)": 2850000,
        "Tổng Tiền (VNĐ)": 5700000,
        "Phương Thức Thanh Toán": "Chuyển khoản VietQR Napas 24/7",
        "Ngân Hàng": "MB Bank - STK 0988888888",
        "Trạng Thái Thanh Toán": "Đã thanh toán (Confirmed)",
        "Trạng Thái Vé": "Đã gửi E-Voucher tự động",
        "Ghi Chú Yêu Cầu": "Ăn chay 1 người, phòng tầng cao có ban công"
    },
    {
        "Mã Đơn Hàng": "VJ10295",
        "Thời Gian Đặt": "2026-10-30 09:15:20",
        "Họ và Tên Khách Hàng": "Trần Thị Mai Hương",
        "Số Điện Thoại": "0987654321",
        "Email Nhận Vé": "huong.tran@gmail.com",
        "Tên Tour Đã Đặt": "Du Thuyền Vịnh Hạ Long 5 Sao - Đảo Ti Tốp - Hang Sửng Sốt 2N1Đ",
        "Vùng Miền": "Miền Bắc",
        "Đơn Vị Điều Hành (Operator)": "Halong Luxury Cruises",
        "Ngày Khởi Hành": "2026-11-12",
        "Số Khách": 4,
        "Đơn Giá (VNĐ)": 3200000,
        "Tổng Tiền (VNĐ)": 12800000,
        "Phương Thức Thanh Toán": "Chuyển khoản VietQR Napas 24/7",
        "Ngân Hàng": "MB Bank - STK 0988888888",
        "Trạng Thái Thanh Toán": "Đã thanh toán (Confirmed)",
        "Trạng Thái Vé": "Đã gửi E-Voucher tự động",
        "Ghi Chú Yêu Cầu": "Đoàn có 2 trẻ em, cần hướng dẫn viên chu đáo"
    },
    {
        "Mã Đơn Hàng": "VJ10296",
        "Thời Gian Đặt": "2026-10-30 09:45:00",
        "Họ và Tên Khách Hàng": "Lê Hoàng Long",
        "Số Điện Thoại": "0903123456",
        "Email Nhận Vé": "long.le@vlu.edu.vn",
        "Tên Tour Đã Đặt": "Hành Trình Di Sản Miền Trung: Đà Nẵng - Bà Nà Hills - Phố Cổ Hội An 4N3Đ",
        "Vùng Miền": "Miền Trung",
        "Đơn Vị Điều Hành (Operator)": "Danang Heritage Travel",
        "Ngày Khởi Hành": "2026-11-20",
        "Số Khách": 3,
        "Đơn Giá (VNĐ)": 4500000,
        "Tổng Tiền (VNĐ)": 13500000,
        "Phương Thức Thanh Toán": "Chuyển khoản VietQR Napas 24/7",
        "Ngân Hàng": "MB Bank - STK 0988888888",
        "Trạng Thái Thanh Toán": "Đã thanh toán (Confirmed)",
        "Trạng Thái Vé": "Đã gửi E-Voucher tự động",
        "Ghi Chú Yêu Cầu": "Học viên cao học du lịch trải nghiệm dịch vụ lữ hành thực tế"
    },
    {
        "Mã Đơn Hàng": "VJ10297",
        "Thời Gian Đặt": "2026-10-30 10:10:30",
        "Họ và Tên Khách Hàng": "Phạm Quốc Tuấn",
        "Số Điện Thoại": "0934567890",
        "Email Nhận Vé": "tuan.pham@outlook.com",
        "Tên Tour Đã Đặt": "Đại Ngàn Tây Nguyên: Buôn Ma Thuột - Hồ Lắk - Thác Dray Nur 3N2Đ",
        "Vùng Miền": "Tây Nguyên",
        "Đơn Vị Điều Hành (Operator)": "Tay Nguyen Discovery Tours",
        "Ngày Khởi Hành": "2026-11-15",
        "Số Khách": 2,
        "Đơn Giá (VNĐ)": 2950000,
        "Tổng Tiền (VNĐ)": 5900000,
        "Phương Thức Thanh Toán": "Chuyển khoản VietQR Napas 24/7",
        "Ngân Hàng": "MB Bank - STK 0988888888",
        "Trạng Thái Thanh Toán": "Đã thanh toán (Confirmed)",
        "Trạng Thái Vé": "Đã gửi E-Voucher tự động",
        "Ghi Chú Yêu Cầu": "Trải nghiệm cà phê Robusta và cồng chiêng bản địa"
    }
]

df = pd.DataFrame(data)

# Export to Excel
excel_path = "data/Danh_Sach_Dat_Tour_OTAs_Vietnam.xlsx"
df.to_excel(excel_path, index=False, engine='openpyxl')

# Export to CSV (with UTF-8 BOM so Excel opens with proper Vietnamese accents)
csv_path = "data/Danh_Sach_Dat_Tour_OTAs_Vietnam.csv"
df.to_csv(csv_path, index=False, encoding='utf-8-sig')

print(f"Excel file created at: {excel_path}")
print(f"CSV file created at: {csv_path}")
