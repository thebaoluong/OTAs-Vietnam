# HỆ THỐNG NỀN TẢNG OTA DU LỊCH & ĐIỀU PHỐI BOOKING BẰNG AI CHATBOT (RAG)
**Đơn vị phát triển:** VietJourneys OTA Marketplace (`vietjourneys.vn`)

Dự án này mô phỏng một **Nền tảng OTA (Online Travel Agency) thông minh** kết nối hơn **1.000 chương trình tour** từ **150+ nhà điều hành lữ hành địa phương (Travel Operators)** khắp 63 tỉnh thành Việt Nam.

---

## 1. MÔ HÌNH VẬN HÀNH OTA & TRAVEL OPERATORS
Khác với công ty du lịch truyền thống, VietJourneys đóng vai trò là **Sàn giao dịch số (Marketplace / OTA)**:
1. **Khách hàng:** Tìm kiếm trong kho 1.000+ tour theo vùng miền, điểm đến, ngân sách và sở thích.
2. **AI Chatbot Agentic:** Tương tác, bóc tách nhu cầu và tự động so sánh giá, đề xuất tour tối ưu.
3. **Điều phối tới Travel Operators (Booking Dispatcher):** Khi khách bấm "Đặt qua OTA", AI tự động chuyển giao thông tin booking sang đơn vị lữ hành phụ trách địa phương đó (Hanoi Heritage, Sapa Trails, Halong Cruises, Mekong Riverways...) để giữ chỗ và phục vụ thực tế.

---

## 2. CẤU TRÚC DỮ LIỆU (`/data`)
* `1000_tours_vietnam.json`: Cơ sở dữ liệu chuẩn gồm **1.000 tour** với đầy đủ thông tin: Mã tour, Tên tour, Vùng miền, Điểm đến, Thời lượng, Phương tiện, Điểm khởi hành, Giá niêm yết OTA, **Tên Travel Operator phụ trách**, Đánh giá (Rating & Reviews), Điểm nhấn và Lịch trình.
* `tours/`: Dữ liệu phân vùng theo Markdown phục vụ Knowledge Base của Chatbot AI (RAG).
* `services/dich_vu_du_lich_khac.md`: Khách sạn/Resort, Thuê xe, Vé máy bay, E-visa, MICE, Bảo hiểm.
* `faqs_chinh_sach/chinh_sach_va_faqs.md`: Chính sách trẻ em, dời hủy tour, điều phối OTA.

---

## 3. CÁCH CHẠY WEBSITE THỬ NGHIỆM
Website được phục vụ trên local server:
* URL: `http://localhost:49681` (hoặc chạy lệnh: `python3 -m http.server 49681`).
