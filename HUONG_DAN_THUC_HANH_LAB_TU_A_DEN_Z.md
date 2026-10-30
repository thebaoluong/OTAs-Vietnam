# TÀI LIỆU HƯỚNG DẪN THỰC HÀNH LAB (STEP-BY-STEP HANDS-ON MANUAL)
## XÂY DỰNG WEBSITE OTA, QUẢN LÝ DỮ LIỆU ĐÁM MÂY VÀ TÍCH HỢP AI CHATBOT
**Dành cho Học viên Cao học Du lịch (VLU Masters in Tourism)**  
*Giảng viên hướng dẫn: TS. Lương Thế Bảo*

---

## 🏗️ 1. CẤU TRÚC THƯ MỤC DỰ ÁN CHI TIẾT (PROJECT ARCHITECTURE)

Học viên tổ chức mã nguồn dự án thành cây thư mục chuẩn mực như sau:

```text
13_Tich hop chatbot tu dong/
├── index.html                   # Giao diện chính của website (Semantic HTML5)
├── css/
│   └── styles.css               # Toàn bộ mã định dạng giao diện, responsive và 2 chatbot widget
├── js/
│   ├── app.js                   # Logic vận hành: Lọc tour, modal, Gemini 3.8 Flash API
│   └── firebase-service.js      # Kết nối Google Firebase Firestore (lưu logs & bookings)
├── data/
│   ├── 1000_tours_vietnam.json  # Dữ liệu 1.000 tour chuẩn hóa cấu trúc (dành cho website)
│   └── DU_LIEU_DU_LICH_VIETNAM.txt # Dữ liệu văn bản tri thức (dành cho RAG của Dify & Gemini)
├── slides_assets/               # Thư mục chứa 3 hình ảnh minh họa kiến trúc & chi phí
│   ├── architecture_diagram.png # Sơ đồ kiến trúc tổng thể 2 chatbot
│   ├── cost_breakdown.png       # Infographic cam kết chi phí $0
│   └── rag_workflow.png         # Sơ đồ quy trình RAG
├── Bai_Giang_Tich_Hop_AI_Chatbot_Du_Lich.pptx # Slide bài giảng trình chiếu
├── GIAO_TRINH_TICH_HOP_AI_CHATBOT_DU_LICH.md # Giáo trình lý thuyết và bộ Prompts chuẩn
└── README.md                    # Tài liệu giới thiệu dự án
```

### Chức năng chi tiết từng file cốt lõi:
1. `index.html`: Chứa toàn bộ cấu trúc trang: Header menu, Banner Hero chào mừng sinh viên VLU, Bộ lọc tour, Lưới hiển thị danh sách tour, Hộp thoại xem chi tiết tour (`<dialog>`), và 2 Widget kích hoạt chatbot nổi ở 2 góc dưới màn hình.
2. `css/styles.css`: Thiết kế giao diện hiện đại theo tông màu thiên nhiên du lịch Việt Nam (Emerald & Ocean Blue), hỗ trợ co giãn trên điện thoại, máy tính bảng và màn hình lớn.
3. `js/app.js`: Tự động nạp dữ liệu từ `data/1000_tours_vietnam.json`, xử lý tìm kiếm theo từ khóa và vùng miền, điều khiển đóng/mở 2 chatbot và gọi API Google Gemini để trả lời câu hỏi.
4. `js/firebase-service.js`: Nhúng Firebase SDK v11, kết nối đến dự án Firebase trên Google Cloud để tự động lưu trữ thông tin khách hỏi và đơn đặt tour.

---

## 🌐 2. TẠO WEBSITE LỮ HÀNH OTA VÀ BỐ TRÍ 2 GÓC CHATBOT

### 2.1. Cấu trúc 2 góc màn hình (Dual Widget Layout) trong `index.html`
Để sinh viên so sánh trực quan, hai con chatbot được đặt độc lập:
* **Góc Trái (`#difyWidgetContainer`):** Đại diện cho hướng tiếp cận No-code của nhà quản trị lữ hành. Nhúng trực tiếp chatbot từ Dify Cloud qua thẻ `<iframe>`.
* **Góc Phải (`#geminiWidgetContainer`):** Đại diện cho giải pháp lập trình Native API của kỹ sư công nghệ. Giao diện tùy biến riêng bằng JavaScript kết nối Gemini 3.8 Flash.

```html
<!-- 1. GÓC TRÁI: DIFY.AI NO-CODE CHATFLOW WIDGET -->
<div class="ai-chatbot-dify-widget" id="difyWidgetContainer">
  <button type="button" class="dify-launcher-btn" id="difyLauncherBtn">🌐</button>
  <aside class="dify-window" id="difyWindow" hidden>
    <iframe src="https://udify.app/chatbot/HG0SqfA46yYMtZ2h" frameborder="0"></iframe>
  </aside>
</div>

<!-- 2. GÓC PHẢI: GOOGLE GEMINI NATIVE CHATBOT WIDGET -->
<div class="ai-chatbot-gemini-widget" id="geminiWidgetContainer">
  <button type="button" class="gemini-launcher-btn" id="chatbotLauncherBtn">🤖</button>
  <aside class="gemini-window" id="chatbotWindow" hidden>
    <!-- Khung chat tuỳ biến: Lịch sử tin nhắn, ô nhập liệu & nút gửi -->
  </aside>
</div>
```

---

## 🔥 3. KẾT NỐI CƠ SỞ DỮ LIỆU ĐÁM MÂY GOOGLE FIREBASE

Cơ sở dữ liệu đám mây giúp học viên thu thập dữ liệu khách hàng thực tế để làm bài nghiên cứu hoặc luận văn thạc sĩ.

### Bước 3.1: Khởi tạo Project trên Firebase Console
1. Truy cập: `https://console.firebase.google.com/` bằng tài khoản Google.
2. Bấm **Add project** ──► Đặt tên dự án (Ví dụ: `website-otas-vietnam`).
3. Tắt Google Analytics (hoặc bật nếu muốn đo lường) ──► Bấm **Create project**.

### Bước 3.2: Kích hoạt Cloud Firestore Database
1. Trong menu bên trái, chọn **Build** ──► Chọn **Firestore Database**.
2. Bấm **Create database** ──► Chọn vị trí lưu trữ (khuyến nghị: `asia-southeast1` hoặc `nam5-us-central`).
3. Chọn chế độ bảo mật: Chọn **Start in test mode** (để sinh viên dễ dàng đọc/ghi dữ liệu trong quá trình học tập) ──► Bấm **Enable**.

### Bước 3.3: Lấy thông số cấu hình (Firebase Config)
1. Bấm vào biểu tượng bánh răng **Project Settings** (Cài đặt dự án) ──► Kéo xuống mục *Your apps*.
2. Bấm vào biểu tượng Web (`</>`) để đăng ký ứng dụng Web.
3. Copy đoạn mã cấu hình gồm `apiKey`, `authDomain`, `projectId`, `storageBucket`, `appId`.

### Bước 3.4: Điền cấu hình vào file `js/firebase-service.js`
```javascript
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSy...",
  authDomain: "website-otas-vietnam.firebaseapp.com",
  projectId: "website-otas-vietnam",
  storageBucket: "website-otas-vietnam.appspot.com",
  messagingSenderId: "...",
  appId: "..."
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Hàm tự động ghi log cuộc hội thoại
export async function logChatMessage(userMsg, aiMsg) {
  try {
    await addDoc(collection(db, "chat_logs"), {
      user_message: userMsg,
      ai_response: aiMsg,
      timestamp: serverTimestamp()
    });
  } catch (e) {
    console.warn("Lưu chat log:", e);
  }
}

// Hàm tự động ghi nhận đơn đặt tour
export async function saveTourBooking(bookingData) {
  return await addDoc(collection(db, "bookings"), {
    ...bookingData,
    created_at: serverTimestamp()
  });
}
```

---

## 🤖 4. CẤU HÌNH TRỢ LÝ NO-CODE TRÊN DIFY.AI (GÓC TRÁI)

### Bước 4.1: Tạo Kho Tri Thức (Knowledge Base)
1. Truy cập `https://cloud.dify.ai/` ──► Đăng ký/Đăng nhập tài khoản miễn phí.
2. Vào mục **Knowledge** ──► Bấm **Create Knowledge** ──► Chọn tải file từ máy tính: `data/DU_LIEU_DU_LICH_VIETNAM.txt`.
3. **Thao tác quan trọng:** Tại bước cấu hình Indexing, chọn **Economy (Kinh tế)**:
   * *Lợi ích:* Không tốn credit, không cần cấu hình embedding model, hoàn toàn $0.
4. Bấm **Save & Process**. Dify sẽ xử lý và lập chỉ mục trong 10 giây.

### Bước 4.2: Thiết kế sơ đồ Chatflow
1. Vào mục **Studio** ──► Bấm **Create from Blank** ──► Chọn **Chatflow** ──► Đặt tên bot.
2. Trên màn hình Canvas kéo thả các khối:
   * **Node 1 (`START / USER INPUT`):** Tiếp nhận câu hỏi của khách hàng.
   * **Node 2 (`KNOWLEDGE RETRIEVAL`):** Kéo dây từ `START` sang. Chọn kho tri thức vừa tạo ở Bước 4.1. Ô Query đặt là `sys.query`.
   * **Node 3 (`LLM`):** Kéo dây từ `KNOWLEDGE RETRIEVAL` sang.
     - Ô **Model**: Chọn `gemini-3.5-flash-lite` (hoặc `gpt-4o-mini`).
     - Ô **Context**: Bấm chọn biến `{x} result` từ `KNOWLEDGE RETRIEVAL`.
     - Ô **System / Instructions**: Dán **PROMPT 1** trong giáo trình vào.
   * **Node 4 (`ANSWER`):** Kéo dây từ `LLM` sang. Ô Answer chọn biến `{x} text` của `LLM`.
3. Bấm **Publish** (Xuất bản) ở góc phải trên.
4. Vào mục **Access Point** (hoặc Overview) ──► Chọn **Embedded on website** ──► Copy đường link iframe để gắn vào `index.html`.

---

## 🐙 5. QUẢN LÝ MÃ NGUỒN VỚI GITHUB

GitHub đóng vai trò là "két sắt" lưu trữ mã nguồn và là cầu nối để tự động đưa website lên Internet.

### Bước 5.1: Tạo Repository mới trên GitHub
1. Truy cập `https://github.com/` ──► Đăng nhập tài khoản.
2. Bấm vào dấu `+` ở góc trên cùng bên phải ──► Chọn **New repository**.
3. Đặt tên: `OTAs-Vietnam` (chọn Public hoặc Private đều được) ──► Bấm **Create repository**.

### Bước 5.2: Khởi tạo và đẩy code từ máy tính lên GitHub
Mở cửa sổ dòng lệnh (Terminal trên Mac/Linux hoặc Git Bash trên Windows) tại thư mục dự án và gõ các lệnh sau:

```bash
# 1. Khởi tạo kho lưu trữ cục bộ
git init

# 2. Thêm toàn bộ các file trong thư mục vào hàng đợi
git add .

# 3. Đóng gói phiên bản với thông điệp ghi chú
git commit -m "Khoi tao website du lich OTAs Vietnam va tich hop Dual Chatbots"

# 4. Đặt tên nhánh chính là main
git branch -M main

# 5. Liên kết với kho chứa trên GitHub của học viên
git remote add origin https://github.com/thebaoluong/OTAs-Vietnam.git

# 6. Đẩy toàn bộ mã nguồn lên GitHub
git push -u origin main
```

*(Lưu ý: Khi GitHub yêu cầu mật khẩu đăng nhập, học viên tạo **Personal Access Token** tại GitHub Settings ──► Developer settings ──► Personal access tokens để dán vào).*

---

## 🚀 6. XUẤT BẢN WEBSITE LÊN INTERNET TOÀN CẦU VỚI VERCEL

Vercel là nền tảng điện toán đám mây hiện đại nhất hiện nay, cung cấp dịch vụ lưu trữ website tĩnh và Serverless hoàn toàn miễn phí, có chứng chỉ bảo mật HTTPS (ổ khóa xanh).

### Bước 6.1: Kết nối Vercel với GitHub
1. Truy cập `https://vercel.com/` ──► Chọn **Sign Up** (hoặc Log In) bằng chính tài khoản **GitHub**.
2. Trên màn hình chính của Vercel (Dashboard), bấm **Add New...** ──► Chọn **Project**.

### Bước 6.2: Triển khai dự án (Deploy)
1. Ở danh sách các kho mã nguồn bên trái, tìm tên kho `OTAs-Vietnam` ──► Bấm nút **Import**.
2. Màn hình *Configure Project* hiện ra:
   * **Project Name:** Giữ nguyên hoặc đặt tên theo ý muốn (Ví dụ: `otasvietnam`).
   * **Framework Preset:** Chọn `Other` (vì dự án của chúng ta là mã nguồn HTML/JS thuần cực kỳ tối ưu, không cần cài đặt node_modules).
   * **Root Directory:** Giữ nguyên `./`.
3. Bấm nút **Deploy** màu xanh.
4. Chờ 20 - 30 giây: Màn hình tung hoa pháo chúc mừng xuất hiện! Vercel sẽ cấp ngay một đường link tên miền chính thức (Ví dụ: `https://otasvietnam.vercel.app`).

### Bước 6.3: Cơ chế cập nhật tự động (CI/CD - Continuous Deployment)
* Từ nay về sau, mỗi khi học viên sửa đổi giá tour, thêm tour mới, hoặc tinh chỉnh câu lệnh Prompt trong máy tính:
* Chỉ cần gõ:
  ```bash
  git add .
  git commit -m "Cap nhat du lieu tour moi"
  git push
  ```
* Hệ thống Vercel sẽ tự động phát hiện và cập nhật lại website toàn cầu trong vòng 30 giây mà **không cần thao tác thủ công gì trên web hosting**.

---

## 📋 BẢNG TỔNG KẾT KIỂM TRA ĐẠT CHUẨN (LAB CHECKLIST)

| STT | Hạng mục kiểm tra | Trạng thái đạt yêu cầu |
| :---: | :--- | :--- |
| 1 | **Website OTA hiển thị** | Tải danh sách 1.000 tour mượt mà, bộ lọc vùng miền và giá hoạt động chính xác. |
| 2 | **Chatbot Trái (Dify)** | Bấm nút 🌐 mở khung chat iframe, hỏi về tour Sa Pa / Hạ Long trả lời đúng thông tin từ file dữ liệu. |
| 3 | **Chatbot Phải (Gemini)** | Bấm nút 🤖 mở khung chat Native, hỏi đáp siêu tốc, hỏi giá chính xác theo chính sách trẻ em. |
| 4 | **Đám mây Firebase** | Mở Firebase Console thấy các dòng dữ liệu mới trong collection `chat_logs` và `bookings`. |
| 5 | **Triển khai Vercel** | Truy cập đường link `.vercel.app` trên điện thoại di động hiển thị đẹp mắt, tương thích hoàn toàn. |
| 6 | **Chi phí ($0)** | Tài khoản không cần thẻ visa, sử dụng 100% tài nguyên Free Tier phục vụ học tập. |
