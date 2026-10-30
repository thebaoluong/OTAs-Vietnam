# GIÁO TRÌNH HƯỚNG DẪN: TÍCH HỢP HỆ THỐNG TRỢ LÝ AI CHATBOT VÀO NỀN TẢNG DU LỊCH TRỰC TUYẾN (OTA)
**Chuyên đề Ứng dụng Trí tuệ Nhân tạo & Chuyển đổi số trong Quản trị Du lịch - Lữ hành**  
*Tài liệu giảng dạy dành cho Học viên Cao học Du lịch (Masters in Tourism)*

---

## 🎯 MỤC TIÊU ĐÀO TẠO & NĂNG LỰC ĐẦU RA (LEARNING OUTCOMES)
1. **Về tư duy quản trị du lịch số:** Hiểu rõ vai trò của AI Chatbot và công nghệ sinh nội dung (GenAI) trong việc tối ưu hóa quy trình tư vấn tour 24/7, cá nhân hóa trải nghiệm khách hàng và giải bài toán quá tải chăm sóc khách hàng mùa cao điểm.
2. **Về hiểu biết công nghệ:**
   - Nắm vững nguyên lý **RAG (Retrieval-Augmented Generation)**: Kỹ thuật "dạy" AI nắm chắc dữ liệu tour của doanh nghiệp để tư vấn chính xác 100%, không bị ảo giác bịa đặt giá cả hay lịch trình.
   - So sánh thực nghiệm được 2 trường phái tích hợp AI:
     - **Trường phái 1 (No-Code/Low-Code):** Sử dụng nền tảng trực quan **Dify.ai** (Dành cho nhà quản trị kinh doanh, không cần viết mã).
     - **Trường phái 2 (Native API Integration):** Kết nối trực tiếp qua **Google Gemini API** và cơ sở dữ liệu đám mây **Firebase Firestore** (Dành cho bộ phận kỹ thuật công nghệ thông tin).
3. **Về sản phẩm thực hành:** Tự tay triển khai và vận hành được một hệ sinh thái website OTA du lịch hoàn chỉnh, có kết nối dữ liệu mạng lưới tour, có giao diện trải nghiệm trực tuyến trên Internet (Vercel).

---

## 🗺️ TỔNG QUAN QUY TRÌNH THỰC HIỆN (ROADMAP 5 BƯỚC)

1. **BƯỚC 1: Chuẩn hóa Dữ liệu Tour (Knowledge Base & JSON RAG)**
2. **BƯỚC 2: Xây dựng Nền tảng Website OTA (Frontend)**
3. **BƯỚC 3: Thiết lập Chatbot No-code trên Dify.ai (Góc Trái)**
4. **BƯỚC 4: Lập trình Native Chatbot Gemini & Firebase Cloud (Góc Phải)**
5. **BƯỚC 5: Xuất bản Toàn cầu (GitHub & Vercel CI/CD)**

---

## BƯỚC 1: XÂY DỰNG & CHUẨN HÓA DỮ LIỆU DU LỊCH (KNOWLEDGE BASE)

Học viên cần chuẩn bị 2 định dạng dữ liệu cho 2 mục đích khác nhau:
1. **Dữ liệu cấu trúc JSON (`1000_tours_vietnam.json`):** Dành cho website hiển thị lưới danh sách tour, bộ lọc vùng miền, mức giá, tìm kiếm từ khóa.
2. **Dữ liệu phi cấu trúc văn bản (`DU_LIEU_DU_LICH_VIETNAM.txt`):** Dành cho kho tri thức RAG của AI đọc hiểu ngữ cảnh tự nhiên.

### Cấu trúc thông tin chuẩn của một sản phẩm Tour:
- `id`: Mã định danh (VD: `TOUR_MB_001`).
- `name`: Tên tour đầy đủ, hấp dẫn du khách.
- `region`: Phân vùng (Bắc / Trung / Nam / Tây Bắc / Tây Nguyên / Biển Đảo).
- `destination`: Điểm đến chính.
- `duration`: Thời lượng (VD: `3 ngày 2 đêm`).
- `price`: Giá niêm yết (VNĐ/khách).
- `departure`: Lịch khởi hành và điểm đón.
- `transport`: Phương tiện di chuyển (Máy bay, xe limousine cao cấp...).
- `operator`: Tên công ty lữ hành cung cấp tour (Travel Operator).
- `highlights`: Điểm nhấn nổi bật của chuyến đi.
- `schedule`: Tóm tắt hành trình từng ngày (Ngày 1, Ngày 2, Ngày 3...).
- `policy`: Chính sách bao gồm, không bao gồm, phụ thu trẻ em và quy định hoàn/hủy.

---

## BƯỚC 2: THIẾT KẾ NỀN TẢNG WEBSITE OTA (FRONTEND)

* **Công nghệ cốt lõi:** HTML5 ngữ nghĩa, CSS3 hiện đại (Responsive đa thiết bị từ điện thoại đến máy tính), Vanilla JavaScript (tối ưu tốc độ tải trang, không phụ thuộc framework phức tạp).
* **Kiến trúc giao diện:**
  - **Hero Banner:** Lời chào, ảnh đại diện chào đón sinh viên cao học, thông điệp giới thiệu mạng lưới lữ hành liên kết.
  - **Thanh công cụ lọc thông minh (Interactive Filters):** Tìm kiếm theo từ khóa, lọc theo vùng miền (Tabs), lọc theo mức giá (Dưới 3 triệu, 3-7 triệu, trên 7 triệu), sắp xếp theo giá tăng/giảm hoặc điểm đánh giá.
  - **Lưới hiển thị Tour (Tour Cards Grid):** Thẻ thông tin trực quan, nhãn vùng miền, thời lượng, nhà điều hành, giá tiền và nút "Xem Chi Tiết".
  - **Modal Chi Tiết Tour (`<dialog>`):** Hiển thị đầy đủ lịch trình chi tiết từng ngày, chính sách bảo hiểm, hướng dẫn viên và nút gửi yêu cầu tư vấn nhanh vào chatbot.
  - **Bố cục 2 góc màn hình (Dual Floating Widgets):**
    - Góc dưới bên trái: Nút kích hoạt **Dify AI**.
    - Góc dưới bên phải: Nút kích hoạt **Gemini AI**.

---

## BƯỚC 3: THIẾT LẬP CHATBOT DIFY.AI (MÔ HÌNH NO-CODE CHATFLOW)

### Quy trình từng thao tác trên Dify Cloud (https://cloud.dify.ai):
1. **Tạo Kho Tri thức (Knowledge Base):**
   - Vào mục **Knowledge** ──► Bấm **Create Knowledge**.
   - Tải file `DU_LIEU_DU_LICH_VIETNAM.txt` lên.
   - **Lưu ý quan trọng cho học viên:** Chọn chế độ đánh chỉ mục là **Economy (Kinh tế)**. Chế độ này dùng giải pháp lập chỉ mục từ khóa/đảo ngữ (keyword/inverted index) hoàn toàn miễn phí, không yêu cầu cấu hình thêm Embedding Model của OpenAI.
2. **Tạo ứng dụng Chatflow:**
   - Vào **Studio** ──► **Create from Blank** ──► Chọn loại **Chatflow**.
   - Đặt tên: *Trợ Lý Du Lịch VietJourneys OTA*.
3. **Thiết lập luồng Canvas (Visual Node Wiring):**
   Nối các khối theo đường thẳng:
   ```text
   [START / USER INPUT] ──► [KNOWLEDGE RETRIEVAL] ──► [LLM] ──► [ANSWER]
   ```
   - **Tại node `KNOWLEDGE RETRIEVAL`:** Chọn kho tri thức vừa tạo, đặt Query lấy từ `sys.query` (hoặc `User Input / query`).
   - **Tại node `LLM`:**
     - Mục **Model**: Chọn **`gemini-3.5-flash-lite`** (hoặc model Google Gemini đang mở).
     - Mục **Context**: Chọn biến đầu ra `{x} result` của node `KNOWLEDGE RETRIEVAL`.
     - Mục **System / Instruction**: Dán **PROMPT MẪU 1** bên dưới.
   - **Tại node `ANSWER`:** Đầu ra lấy `{x} text` từ node `LLM`.
4. **Xuất bản & Lấy mã nhúng:**
   - Bấm **Publish** (Xuất bản) ở góc trên bên phải.
   - Vào mục **Access Point** (hoặc Overview) ──► Chọn **Embedded on website** ──► Sao chép mã thẻ `<iframe>` để dán vào góc trái website.

---

## BƯỚC 4: THIẾT LẬP CHATBOT GEMINI NATIVE API & FIREBASE (MÔ HÌNH CODE-DRIVEN)

1. **Khởi tạo API Key:**
   - Truy cập Google AI Studio: `https://aistudio.google.com/`.
   - Bấm **Get API key** ──► **Create API key**.
   - *Chi phí:* Hoàn toàn miễn phí ($0) với hạn mức 1.500 lượt chat/ngày.
2. **Khởi tạo Cơ sở Dữ liệu Đám mây (Firebase Firestore):**
   - Truy cập Firebase Console: `https://console.firebase.google.com/`.
   - Tạo Project (Ví dụ: `website-otas-vietnam`).
   - Bật dịch vụ **Cloud Firestore** ở chế độ Test Mode:
     - Tạo collection `chat_logs`: Tự động ghi lại toàn bộ câu hỏi của khách và câu trả lời của AI cùng dấu mốc thời gian (timestamp).
     - Tạo collection `bookings`: Tự động lưu hồ sơ khi khách hàng đồng ý đặt tour qua chatbot (Họ tên, SĐT, Số khách, Tên tour, Ngày khởi hành mong muốn).
3. **Cài đặt Prompt vào mã nguồn JavaScript (`js/app.js`):**
   - Đưa **PROMPT MẪU 2** vào tham số `systemInstruction` của lời gọi API Google Gemini (`v1beta/models/gemini-3.8-flash:generateContent`).
   - Kết nối cơ chế trích xuất thực thể đặt chỗ bằng **PROMPT MẪU 3**.

---

## BƯỚC 5: TRIỂN KHAI LÊN INTERNET (GITHUB & VERCEL)

1. **Đưa mã nguồn lên GitHub:**
   - Khởi tạo Git repository trong thư mục dự án.
   - Commit toàn bộ mã nguồn HTML, CSS, JS, hình ảnh, file dữ liệu.
   - Push lên GitHub (kho lưu trữ công khai hoặc riêng tư).
2. **Triển khai tự động (Continuous Deployment) với Vercel:**
   - Truy cập `https://vercel.com/` và đăng nhập bằng tài khoản GitHub.
   - Bấm **Add New Project** ──► Chọn repository vừa tạo.
   - Bấm **Deploy**.
   - Trong vòng 30 giây, Vercel cung cấp đường link website trực tuyến toàn cầu (VD: `https://otasvietnam.vercel.app`).
   - *Ưu điểm:* Mỗi khi học viên thay đổi dữ liệu hay code và đẩy lên GitHub, website trên Vercel tự động cập nhật ngay lập tức.

---

## 📑 BỘ PROMPTS CHUẨN DÀNH CHO GIẢNG VIÊN VÀ HỌC VIÊN

### 📌 PROMPT 1: Dùng cho LLM Node trong Dify Chatflow (Kèm RAG Context)
> **Mục đích:** Cài đặt vào ô Instructions/System của node LLM trên Dify để bot trả lời dựa trên tri thức đã truy xuất, phong cách lịch thiệp, định hướng chốt tour.

```markdown
Bạn là "Trợ Lý Du Lịch AI VietJourneys OTA" - chuyên viên tư vấn lữ hành cao cấp thuộc nền tảng liên kết các Travel Operators uy tín khắp Việt Nam.

Nhiệm vụ của bạn là tư vấn tour, thiết kế lịch trình và giải đáp mọi thắc mắc của du khách dựa trên kho dữ liệu được cung cấp dưới đây:

<context>
{{#context#}}
</context>

NGUYÊN TẮC TƯ VẤN BẮT BUỘC:
1. TRUNG THỰC VÀ BÁM SÁT DỮ LIỆU: Chỉ tư vấn các tour, mức giá, thời lượng và chính sách có trong phần <context>. Tuyệt đối không tự bịa đặt thông tin tour hoặc giá vé không có trong tài liệu.
2. NẾU THÔNG TIN KHÔNG CÓ TRONG DỮ LIỆU: Hãy nhã nhặn trả lời: "Dạ hiện tại hệ thống chưa cập nhật thông tin chi tiết cho điểm đến này. Em xin phép ghi nhận yêu cầu và kết nối với các đối tác lữ hành địa phương để gửi lịch trình riêng cho Quý khách ạ!"
3. CẤU TRÚC CÂU TRẢ LỜI:
   - Chào hỏi thân thiện, xưng "Em" và gọi khách là "Quý khách" hoặc "Anh/Chị".
   - Đưa ra 2 - 3 gợi ý tour phù hợp nhất kèm: Tên tour, Thời lượng, Mức giá niêm yết, Điểm nhấn hành trình.
   - Nhắc đến đơn vị vận hành (Travel Operator) để tăng tính minh bạch và uy tín.
   - Đặt câu hỏi mở ở cuối để khuyến khích khách hàng tiếp tục tương tác (Ví dụ: "Quý khách dự kiến đi vào ngày nào và đoàn mình có bao nhiêu người để em hỗ trợ kiểm tra chỗ trống tốt nhất ạ?").
4. ĐỊNH DẠNG: Sử dụng gạch đầu dòng rõ ràng, in đậm các thông tin quan trọng (Giá tiền, Điểm nổi bật) để khách hàng dễ đọc trên điện thoại di động.
```

---

### 📌 PROMPT 2: Dùng cho Gemini Native API trên Website (`js/app.js`)
> **Mục đích:** Đóng vai trò System Instruction trực tiếp trong code JavaScript, vừa tư vấn vừa có khả năng nhận biết ý định đặt tour của khách.

```markdown
Bạn là Trợ Lý Du Lịch AI thông minh của nền tảng VietJourneys OTA Marketplace (Hệ thống kết nối hơn 150+ nhà điều hành tour bản địa khắp Việt Nam).
Bạn đang trực tiếp hỗ trợ khách hàng trên website và đồng hành cùng đề tài nghiên cứu chuyển đổi số du lịch của các học viên Cao học Lữ hành.

CƠ SỞ TRI THỨC TOÀN DIỆN VỀ SẢN PHẨM:
- Bạn nắm rõ toàn bộ hệ thống tour trải dài qua 6 vùng du lịch: Miền Bắc, Miền Trung, Miền Nam, Vùng Tây Bắc kỳ vĩ, Đại ngàn Tây Nguyên và các Thiên đường Biển Đảo.
- Các mức giá niêm yết là giá trọn gói đã bao gồm bảo hiểm du lịch, hướng dẫn viên, phương tiện và lưu trú tiêu chuẩn.
- Chính sách trẻ em: Dưới 5 tuổi miễn phí (ngồi chung ghế, ngủ chung giường bố mẹ); Từ 5-10 tuổi tính 75% giá vé người lớn; Từ 11 tuổi tính như người lớn.
- Chính sách hoàn hủy: Hủy trước 7 ngày miễn phí 100%; Hủy trước 3-6 ngày phí 50%; Hủy trong vòng 48h phí 100%.

PHONG CÁCH TƯ VẤN:
- Tác phong: Chuyên nghiệp, am hiểu sâu sắc văn hóa - ẩm thực địa phương, chu đáo và mến khách.
- Khi khách hỏi chung chung (VD: "Có tour nào đi biển đẹp không?"): Hãy gợi ý 3 điểm đến tiêu biểu (Đà Nẵng - Hội An, Nha Trang, Phú Quốc) kèm mức giá và thời gian lý tưởng nhất.
- Khi khách tỏ ý muốn đặt tour: Hướng dẫn khách để lại 3 thông tin cơ bản: (1) Họ và tên, (2) Số điện thoại liên hệ, (3) Ngày dự kiến khởi hành và số lượng thành viên trong đoàn để bộ phận điều hành giữ chỗ ưu tiên.
```

---

### 📌 PROMPT 3: Prompt trích xuất thực thể đặt tour tự động (Entity Extraction)
> **Mục đích:** Sau khi khách hàng đồng ý đặt tour trong đoạn chat, prompt này giúp AI tự động trích xuất dữ liệu thành định dạng JSON chuẩn để ghi thẳng vào Firebase Database.

```markdown
Dựa vào lịch sử cuộc trò chuyện giữa Khách hàng và Trợ lý AI du lịch dưới đây, hãy trích xuất thông tin đặt tour của khách hàng thành duy nhất một định dạng JSON hợp lệ.

ĐOẠN HỘI THOẠI:
"""
{CONVERSATION_HISTORY}
"""

YÊU CẦU ĐẦU RA JSON (Không kèm bất kỳ lời dẫn hay ký tự markdown nào ngoài cặp ngoặc nhọn):
{
  "customer_name": "Tên khách hàng (hoặc null nếu chưa có)",
  "phone_number": "Số điện thoại (hoặc null nếu chưa có)",
  "tour_name": "Tên tour khách quan tâm đặt",
  "departure_date": "Ngày khởi hành mong muốn (hoặc null)",
  "pax_count": "Số lượng khách dự kiến (số nguyên, mặc định 1 nếu không rõ)",
  "special_requests": "Ghi chú đặc biệt (ăn chay, người già, em bé...)",
  "booking_status": "PENDING"
}
```

---

### 📌 PROMPT 4: Dành cho Học viên sử dụng AI tạo tự động 1.000 dữ liệu Tour mẫu
> **Mục đích:** Dành cho học viên tự thực hành mở rộng kho dữ liệu tour cho các tỉnh thành đặc thù (Du lịch sinh thái Đồng bằng sông Cửu Long, Du lịch di sản Miền Trung...).

```markdown
Đóng vai trò là Chuyên gia thiết kế sản phẩm lữ hành (Product Tour Designer) có 15 năm kinh nghiệm tại Việt Nam.

Hãy tạo cho tôi danh sách 20 gói tour du lịch chi tiết thuộc khu vực [ĐIỀN TÊN VÙNG MIỀN, VÍ DỤ: TÂY NGUYÊN] dưới định dạng JSON mảng các đối tượng (Array of Objects).

Mỗi tour phải đảm bảo đầy đủ các thuộc tính kỹ thuật sau:
1. "id": Mã duy nhất theo định dạng "TOUR_[VÙNG]_[SỐ_THỨ_TỰ]"
2. "name": Tên thương mại cuốn hút, thể hiện rõ hành trình
3. "region": Tên phân vùng
4. "destination": Các điểm tham quan cốt lõi
5. "duration": Thời lượng chuẩn (VD: "3 Ngày 2 Đêm", "4 Ngày 3 Đêm")
6. "price": Giá tiền tính theo VNĐ (số nguyên, từ 1.800.000 đến 12.000.000)
7. "departure": Tần suất và điểm đón (VD: "Thứ 6 hàng tuần từ TP.HCM")
8. "transport": Phương tiện di chuyển cụ thể
9. "operator": Tên một công ty du lịch địa phương uy tín (sáng tạo tên thực tế)
10. "rating": Điểm đánh giá (từ 4.6 đến 5.0)
11. "reviews_count": Số lượt đánh giá thực tế (từ 45 đến 350)
12. "highlights": Mảng 3-4 trải nghiệm đắt giá nhất của tour
13. "schedule": Mảng lịch trình tóm tắt từng ngày (Ngày 1, Ngày 2, Ngày 3)

Dữ liệu cần phản ánh chân thực văn hóa bản địa, ẩm thực đặc trưng và thời gian di chuyển hợp lý.
```

---

## 🎓 GỢI Ý HƯỚNG ĐỀ TÀI NGHIÊN CỨU & LUẬN VĂN THẠC SĨ TỪ HỆ THỐNG NÀY

Học viên cao học có thể tận dụng trực tiếp nền tảng song song 2 chatbot này để làm dữ liệu thực nghiệm cho luận văn tốt nghiệp:

1. **Đề tài 1: Đánh giá sự chấp nhận công nghệ của du khách đối với AI Chatbot**
   - Ứng dụng mô hình **TAM (Technology Acceptance Model)** hoặc **UTAUT**: Đo lường Mối quan hệ giữa *Tính dễ sử dụng cảm nhận (PEOU)*, *Tính hữu ích cảm nhận (PU)* đối với *Ý định đặt tour trực tuyến (Behavioral Intention)*.
2. **Đề tài 2: Nghiên cứu so sánh A/B Testing giữa No-code RAG Chatbot và Native API Chatbot**
   - So sánh về: Thời gian phản hồi (Response Latency), Tỷ lệ chuyển đổi đơn đặt tour (Conversion Rate), và Mức độ hài lòng của khách hàng (CSAT).
3. **Đề tài 3: Quản trị trải nghiệm khách hàng (Customer Experience - CX) trong kỷ nguyên du lịch thông minh**
   - Khảo sát du khách tại TP.HCM hoặc sinh viên các trường đại học du lịch khi tương tác với nền tảng VietJourneys OTA để tìm ra các rào cản tâm lý khi ra quyết định du lịch thông qua trợ lý ảo.
