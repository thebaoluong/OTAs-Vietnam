import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

os.makedirs("slides_assets", exist_ok=True)

# -----------------------------------------------------------------------------
# 1. GENERATE ILLUSTRATION 1: ARCHITECTURE DIAGRAM
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis('off')

# Background canvas
fig.patch.set_facecolor('#F8FAFC')
ax.set_facecolor('#F8FAFC')

# Title
ax.text(6, 6.5, "KIẾN TRÚC TỔNG THỂ: 2 HỆ THỐNG AI CHATBOT TRÊN OTA", 
        ha='center', va='center', fontsize=15, fontweight='bold', color='#0F172A')
ax.text(6, 6.15, "So sánh Mô hình No-code Agentic (Dify) vs. Mô hình Native API (Gemini + Cloud DB)", 
        ha='center', va='center', fontsize=10.5, color='#64748B')

# Client Box (Top center)
rect_user = patches.FancyBboxPatch((4.3, 4.7), 3.4, 0.9, boxstyle="round,pad=0.1", 
                                  fc='#1E293B', ec='#0F172A', lw=1.5)
ax.add_patch(rect_user)
ax.text(6, 5.25, "DU KHÁCH / HỌC VIÊN CAO HỌC", ha='center', va='center', fontsize=10.5, fontweight='bold', color='white')
ax.text(6, 4.9, "Truy cập: https://otasvietnam.vercel.app", ha='center', va='center', fontsize=8.5, color='#94A3B8')

# Left Branch: Dify.ai (Blue)
rect_dify_box = patches.FancyBboxPatch((0.6, 0.8), 5.0, 3.4, boxstyle="round,pad=0.15", 
                                      fc='#EFF6FF', ec='#3B82F6', lw=2, ls='--')
ax.add_patch(rect_dify_box)
ax.text(3.1, 3.9, "NHÁNH 1: DIFY.AI NO-CODE CHATFLOW (GÓC TRÁI)", ha='center', va='center', 
        fontsize=10.5, fontweight='bold', color='#1E40AF')

# Sub components Left
sub_dify_ui = patches.FancyBboxPatch((0.9, 2.7), 4.4, 0.7, boxstyle="round,pad=0.08", fc='#DBEAFE', ec='#60A5FA')
ax.add_patch(sub_dify_ui)
ax.text(3.1, 3.05, "Iframe Widget (udify.app)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1E3A8A')

sub_dify_rag = patches.FancyBboxPatch((0.9, 1.8), 4.4, 0.7, boxstyle="round,pad=0.08", fc='#DBEAFE', ec='#60A5FA')
ax.add_patch(sub_dify_rag)
ax.text(3.1, 2.15, "Dify Knowledge Base (Economy Indexing)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1E3A8A')

sub_dify_llm = patches.FancyBboxPatch((0.9, 0.9), 4.4, 0.7, boxstyle="round,pad=0.08", fc='#2563EB', ec='#1D4ED8')
ax.add_patch(sub_dify_llm)
ax.text(3.1, 1.25, "LLM: Gemini 3.5 Flash-lite (Free Tier $0)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='white')

# Right Branch: Gemini Native (Green)
rect_gem_box = patches.FancyBboxPatch((6.4, 0.8), 5.0, 3.4, boxstyle="round,pad=0.15", 
                                     fc='#F0FDF4', ec='#16A34A', lw=2, ls='--')
ax.add_patch(rect_gem_box)
ax.text(8.9, 3.9, "NHÁNH 2: NATIVE GEMINI API & FIREBASE (GÓC PHẢI)", ha='center', va='center', 
        fontsize=10.5, fontweight='bold', color='#166534')

# Sub components Right
sub_gem_ui = patches.FancyBboxPatch((6.7, 2.7), 4.4, 0.7, boxstyle="round,pad=0.08", fc='#DCFCE7', ec='#4ADE80')
ax.add_patch(sub_gem_ui)
ax.text(8.9, 3.05, "Native Vanilla JS Floating Widget", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#14532D')

sub_gem_rag = patches.FancyBboxPatch((6.7, 1.8), 4.4, 0.7, boxstyle="round,pad=0.08", fc='#15803D', ec='#166534')
ax.add_patch(sub_gem_rag)
ax.text(8.9, 2.15, "Google Gemini 3.8 Flash (Direct API - Free)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='white')

sub_gem_db = patches.FancyBboxPatch((6.7, 0.9), 4.4, 0.7, boxstyle="round,pad=0.08", fc='#DCFCE7', ec='#4ADE80')
ax.add_patch(sub_gem_db)
ax.text(8.9, 1.25, "Google Cloud Firestore: 'chat_logs' & 'bookings'", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#14532D')

# Connecting Arrows
ax.annotate('', xy=(3.1, 4.3), xytext=(5.1, 4.7), 
            arrowprops=dict(arrowstyle="->", lw=2, color='#2563EB', connectionstyle="arc3,rad=-0.1"))
ax.annotate('', xy=(8.9, 4.3), xytext=(6.9, 4.7), 
            arrowprops=dict(arrowstyle="->", lw=2, color='#16A34A', connectionstyle="arc3,rad=0.1"))

plt.tight_layout()
plt.savefig("slides_assets/architecture_diagram.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

# -----------------------------------------------------------------------------
# 2. GENERATE ILLUSTRATION 2: COST BREAKDOWN INFOGRAPHIC
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 6.5)
ax.axis('off')

fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

ax.text(6, 6.0, "BẢNG MINH BẠCH CHI PHÍ AI: AN TÂM 100% CHO SINH VIÊN", 
        ha='center', va='center', fontsize=15, fontweight='bold', color='#0F172A')
ax.text(6, 5.6, "Chính sách Free Tier $0 của Google AI Studio & Dify Cloud Sandbox", 
        ha='center', va='center', fontsize=10.5, color='#475569')

# Card 1: Google Gemini API Free Tier
card1 = patches.FancyBboxPatch((0.8, 1.0), 3.2, 4.2, boxstyle="round,pad=0.15", fc='#F8FAFC', ec='#3B82F6', lw=2)
ax.add_patch(card1)
ax.text(2.4, 4.8, "GOOGLE GEMINI API", ha='center', va='center', fontsize=11, fontweight='bold', color='#1E40AF')
ax.text(2.4, 4.35, "GÓI MIỄN PHÍ ($0)", ha='center', va='center', fontsize=14, fontweight='bold', color='#16A34A')
items1 = [
    "• 15 lượt chat / phút (15 RPM)",
    "• 1.500 câu hỏi / ngày (1,500 RPD)",
    "• 1 Triệu tokens / phút (1M TPM)",
    "• KHÔNG cần thẻ Visa/Mastercard",
    "• KHÔNG tự động trừ tiền",
    "• Vượt hạn mức: Tự ngắt an toàn,\n  không phát sinh nợ cước"
]
for idx, text in enumerate(items1):
    ax.text(1.0, 3.8 - (idx * 0.46), text, fontsize=9.2, color='#334155', va='top')

# Card 2: Dify Cloud Sandbox
card2 = patches.FancyBboxPatch((4.4, 1.0), 3.2, 4.2, boxstyle="round,pad=0.15", fc='#F8FAFC', ec='#8B5CF6', lw=2)
ax.add_patch(card2)
ax.text(6.0, 4.8, "DIFY.AI SANDBOX", ha='center', va='center', fontsize=11, fontweight='bold', color='#6D28D9')
ax.text(6.0, 4.35, "NO-CODE FREE TIER", ha='center', va='center', fontsize=14, fontweight='bold', color='#16A34A')
items2 = [
    "• Dify Cloud Sandbox miễn phí",
    "• Chế độ Economy Indexing ($0)",
    "• Dùng API Key Gemini miễn phí",
    "• Không tốn phí lưu trữ Chatflow",
    "• Dễ dàng nhúng Iframe vào web",
    "• Học viên thao tác trực quan,\n  không cần mua thêm credit"
]
for idx, text in enumerate(items2):
    ax.text(4.6, 3.8 - (idx * 0.46), text, fontsize=9.2, color='#334155', va='top')

# Card 3: So sánh Chi phí nếu trả phí (Pay-As-You-Go)
card3 = patches.FancyBboxPatch((8.0, 1.0), 3.2, 4.2, boxstyle="round,pad=0.15", fc='#FEF2F2', ec='#EF4444', lw=2)
ax.add_patch(card3)
ax.text(9.6, 4.8, "NẾU SAU NÀY TRẢ PHÍ?", ha='center', va='center', fontsize=11, fontweight='bold', color='#991B1B')
ax.text(9.6, 4.35, "SIÊU RẺ (TIẾT KIỆM)", ha='center', va='center', fontsize=14, fontweight='bold', color='#DC2626')
items3 = [
    "• Gemini 3.5 Flash-lite:",
    "  Chỉ ~$0.075 / 1.000.000 tokens",
    "• 1.000.000 chữ ≈ 2.000 VNĐ",
    "• 1 cuộc chat hỏi tour ≈ 2 VNĐ",
    "• Cả lớp học chat cả tuần:",
    "  Chưa bằng 1/2 cốc cà phê!",
    "• Rẻ hơn GPT-4o từ 20-50 lần"
]
for idx, text in enumerate(items3):
    ax.text(8.2, 3.8 - (idx * 0.46), text, fontsize=9.2, color='#334155', va='top')

plt.tight_layout()
plt.savefig("slides_assets/cost_breakdown.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

# -----------------------------------------------------------------------------
# 3. GENERATE ILLUSTRATION 3: RAG WORKFLOW EXPLAINED
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 4.5), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 5)
ax.axis('off')
fig.patch.set_facecolor('#F8FAFC')
ax.set_facecolor('#F8FAFC')

ax.text(6, 4.5, "NGUYÊN LÝ RAG (RETRIEVAL-AUGMENTED GENERATION) TRONG DU LỊCH", 
        ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')

steps = [
    ("1. CÂU HỎI DU KHÁCH", "\"Có tour Tây Bắc 3 ngày\ngiá dưới 4 triệu không?\"", '#1E293B', '#F1F5F9', '#0F172A'),
    ("2. TRUY XUẤT RAG", "Tìm kiếm trong file dữ liệu\n1.000 tour chuẩn hóa", '#2563EB', '#EFF6FF', '#1E40AF'),
    ("3. GHÉP BỐI CẢNH", "Prompt + Dữ liệu tour\n+ Câu hỏi của khách", '#7C3AED', '#F5F3FF', '#5B21B6'),
    ("4. LLM TƯ VẤN", "Gemini AI trả lời chính xác\ngiá, lịch trình & lữ hành", '#16A34A', '#F0FDF4', '#15803D')
]

for idx, (title, desc, border_col, bg_col, text_col) in enumerate(steps):
    x = 0.6 + idx * 2.85
    box = patches.FancyBboxPatch((x, 1.2), 2.5, 2.4, boxstyle="round,pad=0.1", fc=bg_col, ec=border_col, lw=2)
    ax.add_patch(box)
    ax.text(x + 1.25, 3.1, title, ha='center', va='center', fontsize=10, fontweight='bold', color=text_col)
    ax.text(x + 1.25, 2.1, desc, ha='center', va='center', fontsize=9.2, color='#334155', multialignment='center')
    
    if idx < 3:
        ax.annotate('', xy=(x + 2.8, 2.4), xytext=(x + 2.55, 2.4), 
                    arrowprops=dict(arrowstyle="->", lw=2.5, color='#64748B'))

plt.tight_layout()
plt.savefig("slides_assets/rag_workflow.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()

print("All illustration assets generated successfully!")

# -----------------------------------------------------------------------------
# 4. BUILD ACADEMIC PRESENTATION (PPTX)
# -----------------------------------------------------------------------------
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

DARK_NAVY = RGBColor(0x0F, 0x17, 0x2A)
PRIMARY_BLUE = RGBColor(0x1F, 0x4E, 0x79)
ACCENT_BLUE = RGBColor(0x25, 0x63, 0xEB)
EMERALD_GREEN = RGBColor(0x11, 0x57, 0x35)
CARD_BG = RGBColor(0xF8, 0xFA, 0xFC)
MUTED_TEXT = RGBColor(0x64, 0x74, 0x8B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

def add_header(slide, action_title, category="CHUYÊN ĐỀ CAO HỌC DU LỊCH • VLU MASTERS"):
    # Category tag
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.35))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category.upper()
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = ACCENT_BLUE

    # Action title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.8))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = action_title
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY

# -----------------------------------------------------------------------------
# SLIDE 1: TITLE SLIDE
# -----------------------------------------------------------------------------
s1 = prs.slides.add_slide(blank_layout)

# Decorative background strip
bg_box = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg_box.fill.solid()
bg_box.fill.fore_color.rgb = RGBColor(0xF1, 0xF5, 0xF9)
bg_box.line.fill.background()

card_title = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.0), Inches(11.333), Inches(5.5))
card_title.fill.solid()
card_title.fill.fore_color.rgb = WHITE
card_title.line.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

# Title content
tb = s1.shapes.add_textbox(Inches(1.5), Inches(1.6), Inches(10.3), Inches(4.3))
tf = tb.text_frame
tf.word_wrap = True

p1 = tf.paragraphs[0]
p1.text = "TÍCH HỢP HỆ THỐNG TRỢ LÝ AI CHATBOT VÀO NỀN TẢNG DU LỊCH TRỰC TUYẾN (OTA)"
p1.font.size = Pt(28)
p1.font.bold = True
p1.font.color.rgb = PRIMARY_BLUE

p2 = tf.add_paragraph()
p2.text = "Chuyên đề Ứng dụng GenAI, RAG & Cloud trong Quản trị Lữ hành số"
p2.font.size = Pt(18)
p2.font.bold = True
p2.font.color.rgb = EMERALD_GREEN
p2.space_before = Pt(14)

p3 = tf.add_paragraph()
p3.text = "• Phân tích so sánh 2 kiến trúc: Dify.ai No-code Chatflow vs. Google Gemini Native API\n" \
          "• Cơ sở dữ liệu RAG kết nối mạng lưới các Travel Operators uy tín khắp Việt Nam\n" \
          "• Hướng dẫn chi tiết chi phí $0 Free Tier và các hướng đề tài Luận văn Thạc sĩ"
p3.font.size = Pt(14)
p3.font.color.rgb = DARK_NAVY
p3.space_before = Pt(20)

p4 = tf.add_paragraph()
p4.text = "🎓 Giảng viên hướng dẫn: TS. Lương Thế Bảo | Học viên thực hiện: Lớp Cao học Du lịch (VLU Masters)"
p4.font.size = Pt(13)
p4.font.bold = True
p4.font.color.rgb = ACCENT_BLUE
p4.space_before = Pt(24)

# -----------------------------------------------------------------------------
# SLIDE 2: BỐI CẢNH & VẤN ĐỀ TRONG QUẢN TRỊ DU LỊCH
# -----------------------------------------------------------------------------
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "Bối Cảnh Quản Trị: Trợ Lý AI Giải Quyết Bài Toán Quá Tải Tư Vấn Tour 24/7")

# 3 Columns
col_width = Inches(3.64)
col_gap = Inches(0.39)
left_base = Inches(0.8)

cols_data = [
    ("THỰC TRẠNG NGÀNH LỮ HÀNH", 
     "• Khách du lịch hiện đại đòi hỏi phản hồi tức thì về giá, lịch trình và chỗ trống.\n"
     "• Đội ngũ tư vấn viên quá tải vào ban đêm và mùa cao điểm du lịch hè, lễ tết.\n"
     "• Mạng lưới đối tác (Travel Operators) phân tán, khó đồng bộ thông tin kịp thời.",
     RGBColor(0xFE, 0xF2, 0xF2), RGBColor(0xEF, 0x44, 0x44)),
    
    ("GIẢI PHÁP GENAI & RAG", 
     "• AI Chatbot tư vấn tức thì 24/7/365, không mệt mỏi, phản hồi dưới 1 giây.\n"
     "• Công nghệ RAG đảm bảo trả lời đúng 100% dữ liệu tour, không bị ảo giác giá.\n"
     "• Tự động thu thập thông tin khách hàng và chốt đơn đặt chỗ (Lead Generation).",
     RGBColor(0xF0, 0xFD, 0xF4), RGBColor(0x16, 0xA3, 0x4A)),
    
    ("Ý NGHĨA HỌC THUẬT & THỰC TIỄN", 
     "• Học viên làm chủ cả tư duy quản trị số (No-code) và giải pháp kỹ thuật (API).\n"
     "• Cung cấp dữ liệu thực nghiệm phục vụ viết Luận văn Thạc sĩ (TAM, UTAUT).\n"
     "• Khả năng ứng dụng thực tế ngay tại các doanh nghiệp lữ hành đang công tác.",
     RGBColor(0xEF, 0xF6, 0xFF), RGBColor(0x3B, 0x82, 0xF6))
]

for idx, (title, content, bg_col, border_col) in enumerate(cols_data):
    x = left_base + idx * (col_width + col_gap)
    card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), col_width, Inches(4.9))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_col
    card.line.color.rgb = border_col
    card.line.width = Pt(1.5)
    
    tb = s2.shapes.add_textbox(x + Inches(0.25), Inches(2.0), col_width - Inches(0.5), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p_t = tf.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(14)
    p_t.font.bold = True
    p_t.font.color.rgb = border_col
    
    p_c = tf.add_paragraph()
    p_c.text = content
    p_c.font.size = Pt(13)
    p_c.font.color.rgb = DARK_NAVY
    p_c.space_before = Pt(14)

# -----------------------------------------------------------------------------
# SLIDE 3: KIẾN TRÚC TỔNG THỂ (CÓ HÌNH MINH HỌA)
# -----------------------------------------------------------------------------
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "Kiến Trúc Song Song: Tách Biệt 2 Góc Màn Hình Phục Vụ So Sánh Thực Nghiệm")

s3.shapes.add_picture("slides_assets/architecture_diagram.png", Inches(0.8), Inches(1.65), width=Inches(11.73))

# -----------------------------------------------------------------------------
# SLIDE 4: CÔNG NGHỆ RAG TRÁNH ẢO GIÁC
# -----------------------------------------------------------------------------
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "Công Nghệ RAG (Retrieval-Augmented Generation): Bí Quyết Trả Lời Đúng Tour")

s4.shapes.add_picture("slides_assets/rag_workflow.png", Inches(0.8), Inches(1.65), width=Inches(11.73))

# Explanatory card below
bot_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.8), Inches(11.73), Inches(1.9))
bot_card.fill.solid()
bot_card.fill.fore_color.rgb = RGBColor(0xF8, 0xFA, 0xFC)
bot_card.line.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

tb = s4.shapes.add_textbox(Inches(1.1), Inches(4.95), Inches(11.1), Inches(1.6))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "🎯 TẠI SAO NGÀNH DU LỊCH BẮT BUỘC PHẢI DÙNG RAG?"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = PRIMARY_BLUE

p2 = tf.add_paragraph()
p2.text = "1. AI mặc định chỉ có kiến thức chung trên Internet, KHÔNG BIẾT giá tour và lịch trình cụ thể của công ty bạn.\n" \
          "2. RAG đóng vai trò như 'mở sách tài liệu': Khi du khách hỏi, hệ thống trích xuất đúng đoạn thông tin của tour đó rồi đưa vào câu lệnh để AI trả lời.\n" \
          "3. Kết quả: Đảm bảo độ chính xác 100% về giá tiền, điều khoản hoàn hủy và uy tín của nhà điều hành tour bản địa."
p2.font.size = Pt(12)
p2.font.color.rgb = DARK_NAVY
p2.space_before = Pt(6)

# -----------------------------------------------------------------------------
# SLIDE 5: CHATBOT GÓC TRÁI - DIFY.AI
# -----------------------------------------------------------------------------
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Góc Trái: Trợ Lý Dify.ai (Mô Hình No-code Agentic Chatflow Dành Cho Nhà Quản Trị)")

# Left column: Workflow
card_l = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.1))
card_l.fill.solid()
card_l.fill.fore_color.rgb = RGBColor(0xEF, 0xF6, 0xFF)
card_l.line.color.rgb = RGBColor(0x3B, 0x82, 0xF6)

tb_l = s5.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.0), Inches(4.7))
tf_l = tb_l.text_frame
tf_l.word_wrap = True
p = tf_l.paragraphs[0]
p.text = "QUY TRÌNH THIẾT KẾ TRÊN DIFY CLOUD"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)

p_steps = tf_l.add_paragraph()
p_steps.text = "1. Nạp Tri thức (Knowledge Base):\n" \
               "   • Tải file DU_LIEU_DU_LICH_VIETNAM.txt.\n" \
               "   • Chọn chế độ Economy Indexing ($0 hoàn toàn).\n\n" \
               "2. Kéo thả Visual Chatflow Canvas:\n" \
               "   • START ──► KNOWLEDGE RETRIEVAL ──► LLM ──► ANSWER\n\n" \
               "3. Cấu hình Node LLM:\n" \
               "   • Model: gemini-3.5-flash-lite (Free Tier)\n" \
               "   • Context: Chọn biến đầu ra từ Knowledge\n\n" \
               "4. Nhúng Iframe vào Website:\n" \
               "   • Lấy mã nhúng nhúng cố định vào góc trái web."
p_steps.font.size = Pt(12.5)
p_steps.font.color.rgb = DARK_NAVY
p_steps.space_before = Pt(10)

# Right column: Pedagogical Value
card_r = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.7), Inches(5.6), Inches(5.1))
card_r.fill.solid()
card_r.fill.fore_color.rgb = WHITE
card_r.line.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

tb_r = s5.shapes.add_textbox(Inches(7.2), Inches(1.9), Inches(5.0), Inches(4.7))
tf_r = tb_r.text_frame
tf_r.word_wrap = True
p = tf_r.paragraphs[0]
p.text = "GIÁ TRỊ GIẢNG DẠY CHO HỌC VIÊN CAO HỌC"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = PRIMARY_BLUE

p_val = tf_r.add_paragraph()
p_val.text = "• Không rào cản lập trình: Bất kỳ học viên quản trị kinh doanh du lịch nào cũng tự tạo được bot thông minh chỉ sau 15 phút.\n\n" \
             "• Trực quan hóa tư duy logic: Sơ đồ khối giúp người học hiểu rõ đường đi của dữ liệu từ khi khách hỏi đến khi AI trả lời.\n\n" \
             "• Thân thiện với ngân sách nghiên cứu: Tận dụng hoàn toàn gói Sandbox và Free API của Google, không mất tiền duy trì.\n\n" \
             "• Quản lý lịch sử hội thoại: Dify có sẵn màn hình Logs & Annotations để học viên tải dữ liệu chat về phân tích định tính."
p_val.font.size = Pt(12.5)
p_val.font.color.rgb = DARK_NAVY
p_val.space_before = Pt(10)

# -----------------------------------------------------------------------------
# SLIDE 6: CHATBOT GÓC PHẢI - GOOGLE GEMINI NATIVE
# -----------------------------------------------------------------------------
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Góc Phải: Trợ Lý Gemini 3.8 Flash & Google Cloud Firestore (Mô Hình Native Code)")

card_l2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.1))
card_l2.fill.solid()
card_l2.fill.fore_color.rgb = RGBColor(0xF0, 0xFD, 0xF4)
card_l2.line.color.rgb = RGBColor(0x16, 0xA3, 0x4A)

tb_l2 = s6.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.0), Inches(4.7))
tf_l2 = tb_l2.text_frame
tf_l2.word_wrap = True
p = tf_l2.paragraphs[0]
p.text = "ĐẶC ĐIỂM KIẾN TRÚC CODE-DRIVEN"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RGBColor(0x16, 0x65, 0x34)

p_code = tf_l2.add_paragraph()
p_code.text = "• Lập trình trực tiếp bằng JavaScript: Gọi thẳng endpoint API của Google Gemini 3.8 Flash, không qua trung gian.\n\n" \
              "• Tích hợp sâu vào UI/UX: Nút xem tour trên website có thể tự động điền câu hỏi vào khung chat.\n\n" \
              "• Tự động đồng bộ Firebase Firestore:\n" \
              "   - Bảng 'chat_logs': Ghi nhận từng lượt chat.\n" \
              "   - Bảng 'bookings': Lưu hồ sơ đặt tour tự động.\n\n" \
              "• Tốc độ phản hồi cực nhanh: Dưới 0.8 giây cho mỗi câu trả lời tư vấn lịch trình."
p_code.font.size = Pt(12.5)
p_code.font.color.rgb = DARK_NAVY
p_code.space_before = Pt(10)

card_r2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.7), Inches(5.6), Inches(5.1))
card_r2.fill.solid()
card_r2.fill.fore_color.rgb = WHITE
card_r2.line.color.rgb = RGBColor(0xCB, 0xD5, 0xE1)

tb_r2 = s6.shapes.add_textbox(Inches(7.2), Inches(1.9), Inches(5.0), Inches(4.7))
tf_r2 = tb_r2.text_frame
tf_r2.word_wrap = True
p = tf_r2.paragraphs[0]
p.text = "Ý NGHĨA TRONG NGHIÊN CỨU HỌC THUẬT"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = PRIMARY_BLUE

p_res = tf_r2.add_paragraph()
p_res.text = "• Thu thập dữ liệu thực nghiệm chuẩn xác: Toàn bộ tương tác của khách hàng lưu trữ trên Firebase có thể xuất ra Excel/CSV để chạy SPSS / SmartPLS.\n\n" \
             "• Kiểm chứng tỷ lệ chuyển đổi (Conversion Rate): Đo lường xem du khách hỏi bao nhiêu câu thì tiến tới hành vi để lại thông tin đặt tour.\n\n" \
             "• So sánh A/B Testing: Cho một nhóm sinh viên dùng Dify và một nhóm dùng Gemini để đo lường mức độ hài lòng và trải nghiệm công nghệ."
p_res.font.size = Pt(12.5)
p_res.font.color.rgb = DARK_NAVY
p_res.space_before = Pt(10)

# -----------------------------------------------------------------------------
# SLIDE 7: BẢNG DỰ TOÁN CHI PHÍ ($0 AN TÂM CHO SINH VIÊN)
# -----------------------------------------------------------------------------
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Bảng Minh Bạch Chi Phí: Sinh Viên Hoàn Toàn An Tâm Thực Hành Với Chi Phí $0")

s7.shapes.add_picture("slides_assets/cost_breakdown.png", Inches(0.8), Inches(1.65), width=Inches(11.73))

# -----------------------------------------------------------------------------
# SLIDE 8: CÁC PROMPTS MẪU CHUẨN
# -----------------------------------------------------------------------------
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "Bộ Prompts Mẫu: Nghệ Thuật Thiết Kế Câu Lệnh Điều Khiển AI Chuyên Nghiệp")

cols8 = [
    ("PROMPT 1: SYSTEM INSTRUCTION (DIFY)",
     "• Định vị vai trò: Chuyên viên tư vấn lữ hành OTA cao cấp.\n"
     "• Ràng buộc: Chỉ trả lời dữ liệu có trong context, không bịa giá.\n"
     "• Xưng hô: Em - Quý khách, kết thúc bằng câu hỏi mở gợi ý chốt ngày đi.",
     RGBColor(0xEF, 0xF6, 0xFF), RGBColor(0x3B, 0x82, 0xF6)),
    
    ("PROMPT 2: NATIVE GEMINI ADVISOR",
     "• Nắm vững chính sách hoàn hủy, bảo hiểm và vé trẻ em.\n"
     "• Phân loại ngân sách: Dưới 3 triệu, 3-7 triệu, trên 7 triệu.\n"
     "• Hướng dẫn khách để lại SĐT và số lượng khách để giữ chỗ.",
     RGBColor(0xF0, 0xFD, 0xF4), RGBColor(0x16, 0xA3, 0x4A)),
    
    ("PROMPT 3: TRÍCH XUẤT ĐƠN ĐẶT TOUR",
     "• Đọc lịch sử trò chuyện và tự động trích xuất JSON.\n"
     "• Thuộc tính: Họ tên, SĐT, Tên tour, Ngày khởi hành, Số khách.\n"
     "• Ghi trực tiếp vào Firestore mà không cần nhân viên gõ tay.",
     RGBColor(0xFE, 0xF3, 0xC7), RGBColor(0xD9, 0x77, 0x06))
]

for idx, (title, content, bg_col, border_col) in enumerate(cols8):
    x = left_base + idx * (col_width + col_gap)
    card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), col_width, Inches(4.9))
    card.fill.solid()
    card.fill.fore_color.rgb = bg_col
    card.line.color.rgb = border_col
    card.line.width = Pt(1.5)
    
    tb = s8.shapes.add_textbox(x + Inches(0.25), Inches(2.0), col_width - Inches(0.5), Inches(4.4))
    tf = tb.text_frame
    tf.word_wrap = True
    p_t = tf.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(13)
    p_t.font.bold = True
    p_t.font.color.rgb = border_col
    
    p_c = tf.add_paragraph()
    p_c.text = content
    p_c.font.size = Pt(12.5)
    p_c.font.color.rgb = DARK_NAVY
    p_c.space_before = Pt(14)

# -----------------------------------------------------------------------------
# SLIDE 9: ĐỀ TÀI NGHIÊN CỨU LUẬN VĂN THẠC SĨ
# -----------------------------------------------------------------------------
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Định Hướng Đề Tài Luận Văn Thạc Sĩ: Ứng Dụng Mô Hình TAM & UTAUT")

card_res1 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.73), Inches(1.5))
card_res1.fill.solid()
card_res1.fill.fore_color.rgb = RGBColor(0xF8, 0xFA, 0xFC)
card_res1.line.color.rgb = PRIMARY_BLUE
tb1 = s9.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(11.3), Inches(1.3))
tf1 = tb1.text_frame
tf1.word_wrap = True
p = tf1.paragraphs[0]
p.text = "ĐỀ TÀI 1: YẾU TỐ ẢNH HƯỞNG ĐẾN Ý ĐỊNH ĐẶT TOUR QUA AI CHATBOT (MÔ HÌNH TAM)"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = PRIMARY_BLUE
p_sub = tf1.add_paragraph()
p_sub.text = "Nghiên cứu mối quan hệ giữa Tính dễ sử dụng cảm nhận (PEOU), Tính hữu ích cảm nhận (PU), và Niềm tin thương hiệu (Brand Trust) đối với Ý định đặt tour trực tuyến của du khách thế hệ Gen Z & Millennials."
p_sub.font.size = Pt(12)
p_sub.font.color.rgb = DARK_NAVY
p_sub.space_before = Pt(4)

card_res2 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.5), Inches(11.73), Inches(1.5))
card_res2.fill.solid()
card_res2.fill.fore_color.rgb = RGBColor(0xF8, 0xFA, 0xFC)
card_res2.line.color.rgb = EMERALD_GREEN
tb2 = s9.shapes.add_textbox(Inches(1.0), Inches(3.6), Inches(11.3), Inches(1.3))
tf2 = tb2.text_frame
tf2.word_wrap = True
p = tf2.paragraphs[0]
p.text = "ĐỀ TÀI 2: NGHIÊN CỨU SO SÁNH THỰC NGHIỆM A/B TESTING GIỮA NO-CODE VÀ NATIVE AI"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = EMERALD_GREEN
p_sub2 = tf2.add_paragraph()
p_sub2.text = "So sánh tỷ lệ giữ chân khách hàng (Retention Rate), độ trễ phản hồi (Response Latency), và chi phí vận hành giữa giải pháp No-code SaaS (Dify) và In-house Development (Gemini + Cloud Database) trong doanh nghiệp lữ hành vừa và nhỏ."
p_sub2.font.size = Pt(12)
p_sub2.font.color.rgb = DARK_NAVY
p_sub2.space_before = Pt(4)

card_res3 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.2), Inches(11.73), Inches(1.5))
card_res3.fill.solid()
card_res3.fill.fore_color.rgb = RGBColor(0xF8, 0xFA, 0xFC)
card_res3.line.color.rgb = RGBColor(0xD9, 0x77, 0x06)
tb3 = s9.shapes.add_textbox(Inches(1.0), Inches(5.3), Inches(11.3), Inches(1.3))
tf3 = tb3.text_frame
tf3.word_wrap = True
p = tf3.paragraphs[0]
p.text = "ĐỀ TÀI 3: QUẢN TRỊ TRẢI NGHIỆM KHÁCH HÀNG (CX) TRONG CHUYỂN ĐỔI SỐ DU LỊCH"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = RGBColor(0xD9, 0x77, 0x06)
p_sub3 = tf3.add_paragraph()
p_sub3.text = "Khảo sát sự hài lòng của du khách (CSAT, Net Promoter Score) khi được tư vấn bởi Trợ lý AI du lịch so với nhân viên tổng đài truyền thống: Cơ hội và rào cản tâm lý khi ra quyết định chi tiêu du lịch."
p_sub3.font.size = Pt(12)
p_sub3.font.color.rgb = DARK_NAVY
p_sub3.space_before = Pt(4)

# -----------------------------------------------------------------------------
# SLIDE 10: TỔNG KẾT & LỜI CHÚC
# -----------------------------------------------------------------------------
s10 = prs.slides.add_slide(blank_layout)

card_end = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.0), Inches(10.933), Inches(5.5))
card_end.fill.solid()
card_end.fill.fore_color.rgb = WHITE
card_end.line.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
card_end.line.width = Pt(2)

tb_end = s10.shapes.add_textbox(Inches(1.8), Inches(1.6), Inches(9.7), Inches(4.3))
tf_end = tb_end.text_frame
tf_end.word_wrap = True

p_e1 = tf_end.paragraphs[0]
p_e1.text = "TỔNG KẾT & THỰC HÀNH TRỰC TIẾP"
p_e1.font.size = Pt(26)
p_e1.font.bold = True
p_e1.font.color.rgb = PRIMARY_BLUE
p_e1.alignment = PP_ALIGN.CENTER

p_e2 = tf_end.add_paragraph()
p_e2.text = "🌐 Trải nghiệm trực tuyến sản phẩm hoàn thiện:\nhttps://otasvietnam.vercel.app"
p_e2.font.size = Pt(16)
p_e2.font.bold = True
p_e2.font.color.rgb = ACCENT_BLUE
p_e2.alignment = PP_ALIGN.CENTER
p_e2.space_before = Pt(20)

p_e3 = tf_end.add_paragraph()
p_e3.text = "✨ Chúc các bạn học viên Cao học Du lịch (VLU Masters) học tập xuất sắc,\nhoàn thành thắng lợi đề tài nghiên cứu và ứng dụng thành công AI vào chuyển đổi số lữ hành! ✨"
p_e3.font.size = Pt(15)
p_e3.font.bold = True
p_e3.font.color.rgb = EMERALD_GREEN
p_e3.alignment = PP_ALIGN.CENTER
p_e3.space_before = Pt(24)

# Save presentation
pptx_path = "Bai_Giang_Tich_Hop_AI_Chatbot_Du_Lich.pptx"
prs.save(pptx_path)
print(f"Presentation saved successfully to {pptx_path}!")
