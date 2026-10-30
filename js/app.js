/**
 * VIETJOURNEYS TRAVEL - ONLINE TRAVEL AGENCY (OTA) MARKETPLACE
 * Platform Features:
 * - 1.000+ Vietnam Tours Database from 150+ Travel Operators
 * - Realtime Filtering, Search, Sorting & Pagination (12 tours/page)
 * - Accessible Modal Dialog (Complies with Modern Web Guidance)
 * - Intelligent AI OTA Dispatcher & Assistant Engine (Local RAG)
 */

document.addEventListener('DOMContentLoaded', () => {
  // Application State
  const state = {
    allTours: [],
    filteredTours: [],
    currentPage: 1,
    pageSize: 12,
    activeRegion: 'all',
    searchQuery: '',
    priceFilter: 'all',
    sortOption: 'featured'
  };

  // DOM Elements
  const toursGrid = document.getElementById('toursGrid');
  const resultsCount = document.getElementById('resultsCount');
  const paginationWrapper = document.getElementById('paginationWrapper');
  const searchInput = document.getElementById('searchInput');
  const searchSubmitBtn = document.getElementById('searchSubmitBtn');
  const regionFilter = document.getElementById('regionFilter');
  const priceFilter = document.getElementById('priceFilter');
  const sortSelect = document.getElementById('sortSelect');
  const tabButtons = document.querySelectorAll('.tab-btn');

  // Modal Dialog Elements
  const tourModal = document.getElementById('tourDetailDialog');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalBody = document.getElementById('modalBody');

  // Dify Widget Elements (Góc Trái)
  const difyLauncherBtn = document.getElementById('difyLauncherBtn');
  const difyWindow = document.getElementById('difyWindow');
  const closeDifyBtn = document.getElementById('closeDifyBtn');

  // Gemini Widget Elements (Góc Phải)
  const chatbotLauncherBtn = document.getElementById('chatbotLauncherBtn');
  const chatbotWindow = document.getElementById('chatbotWindow');
  const closeChatBtn = document.getElementById('closeChatBtn');
  const clearChatBtn = document.getElementById('clearChatBtn');
  const chatMessages = document.getElementById('chatMessages');
  const chatInputForm = document.getElementById('chatInputForm');
  const chatUserInput = document.getElementById('chatUserInput');
  const openChatbotTopBtn = document.getElementById('openChatbotTopBtn');
  const openChatbotFooterBtn = document.getElementById('openChatbotFooterBtn');

  // Dify Controls (Góc Trái)
  function openDifyChat() {
    difyWindow?.removeAttribute('hidden');
    difyLauncherBtn?.setAttribute('aria-expanded', 'true');
  }

  function closeDifyChat() {
    difyWindow?.setAttribute('hidden', '');
    difyLauncherBtn?.setAttribute('aria-expanded', 'false');
  }

  difyLauncherBtn?.addEventListener('click', () => {
    const isHidden = difyWindow.hasAttribute('hidden');
    if (isHidden) openDifyChat();
    else closeDifyChat();
  });

  closeDifyBtn?.addEventListener('click', closeDifyChat);

  // Gemini Controls (Góc Phải)
  function openChatbot() {
    chatbotWindow?.removeAttribute('hidden');
    chatbotLauncherBtn?.setAttribute('aria-expanded', 'true');
    if (chatUserInput) chatUserInput.focus();
  }

  function closeChatbot() {
    chatbotWindow?.setAttribute('hidden', '');
    chatbotLauncherBtn?.setAttribute('aria-expanded', 'false');
  }
  async function loadToursData() {
    try {
      const response = await fetch('data/1000_tours_vietnam.json');
      if (!response.ok) throw new Error('Không thể tải dữ liệu tour');
      state.allTours = await response.json();
      state.filteredTours = [...state.allTours];
      renderTours();
    } catch (err) {
      console.error('Lỗi nạp tour:', err);
      toursGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 3rem;">
          <p style="color: #ef4444; font-weight: 700;">Không thể tải dữ liệu 1.000 tour du lịch.</p>
          <p style="color: #6b7280; font-size: 0.9rem;">Vui lòng kiểm tra file data/1000_tours_vietnam.json hoặc chạy trên local web server.</p>
        </div>
      `;
    }
  }

  // =========================================================================
  // 2. FILTERING, SEARCHING & SORTING
  // =========================================================================
  function applyFilters() {
    let result = [...state.allTours];

    // Filter by Region
    if (state.activeRegion !== 'all') {
      result = result.filter(t => t.region === state.activeRegion);
    }

    // Filter by Search Query
    if (state.searchQuery.trim() !== '') {
      const q = state.searchQuery.toLowerCase().trim();
      result = result.filter(t => 
        t.name.toLowerCase().includes(q) ||
        t.region.toLowerCase().includes(q) ||
        t.destination.toLowerCase().includes(q) ||
        t.operator.toLowerCase().includes(q) ||
        t.id.toLowerCase().includes(q) ||
        t.category.toLowerCase().includes(q) ||
        t.schedule.toLowerCase().includes(q) ||
        t.highlights.some(h => h.toLowerCase().includes(q))
      );
    }

    // Filter by Price Range
    if (state.priceFilter === 'under-1m') {
      result = result.filter(t => t.price < 1000000);
    } else if (state.priceFilter === '1m-3m') {
      result = result.filter(t => t.price >= 1000000 && t.price <= 3000000);
    } else if (state.priceFilter === '3m-5m') {
      result = result.filter(t => t.price > 3000000 && t.price <= 5000000);
    } else if (state.priceFilter === 'above-5m') {
      result = result.filter(t => t.price > 5000000);
    }

    // Sorting
    if (state.sortOption === 'price-asc') {
      result.sort((a, b) => a.price - b.price);
    } else if (state.sortOption === 'price-desc') {
      result.sort((a, b) => b.price - a.price);
    } else if (state.sortOption === 'name') {
      result.sort((a, b) => a.name.localeCompare(b.name, 'vi'));
    }

    state.filteredTours = result;
    state.currentPage = 1;
    renderTours();
  }

  // =========================================================================
  // 3. RENDERING TOURS & PAGINATION
  // =========================================================================
  function formatVND(amount) {
    return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(amount);
  }

  function renderTours() {
    resultsCount.innerHTML = `Đang hiển thị <strong>${state.filteredTours.length.toLocaleString('vi-VN')}</strong> tour phù hợp từ mạng lưới Travel Operators`;

    if (state.filteredTours.length === 0) {
      toursGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 4rem 1rem;">
          <div style="font-size: 3rem; margin-bottom: 1rem;">🏖️</div>
          <h3 style="font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem;">Không tìm thấy tour phù hợp</h3>
          <p style="color: #6b7280; margin-bottom: 1.5rem;">Vui lòng thử từ khóa khác hoặc điều chỉnh lại bộ lọc vùng miền và mức giá.</p>
          <button type="button" class="btn-detail" id="resetFiltersBtn">Xóa tất cả bộ lọc</button>
        </div>
      `;
      document.getElementById('resetFiltersBtn')?.addEventListener('click', resetAllFilters);
      paginationWrapper.innerHTML = '';
      return;
    }

    // Pagination slice
    const startIndex = (state.currentPage - 1) * state.pageSize;
    const endIndex = startIndex + state.pageSize;
    const currentTours = state.filteredTours.slice(startIndex, endIndex);

    toursGrid.innerHTML = currentTours.map(t => `
      <article class="tour-card" data-tour-id="${t.id}">
        <div class="tour-card-header">
          <div class="tour-card-tags">
            <span class="tag-region">${t.region}</span>
            <span class="tag-id">${t.id}</span>
          </div>
          <h3 class="tour-card-title">${t.name}</h3>
          <div class="tour-operator-badge">
            <span>🏛️</span> Vận hành bởi: <strong>${t.operator}</strong>
          </div>
        </div>
        <div class="tour-card-body">
          <div class="tour-meta-list">
            <span class="tour-meta-item">⏱️ ${t.duration}</span>
            <span class="tour-meta-item">📍 ${t.departure}</span>
            <span class="tour-meta-item">🚗 ${t.transport}</span>
          </div>

          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
            <div class="tour-rating-box">
              <span>⭐ ${t.rating}</span>
              <span style="color: #6b7280; font-weight: 400;">(${t.reviews_count} đánh giá)</span>
            </div>
            <span style="font-size: 0.75rem; color: #0284c7; background: #e0f2fe; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: 600;">${t.category}</span>
          </div>

          <div class="tour-highlights-box">
            <div class="highlights-title">Điểm nhấn nổi bật</div>
            <ul class="highlights-list">
              ${t.highlights.slice(0, 2).map(h => `<li>${h}</li>`).join('')}
            </ul>
          </div>

          <div class="tour-card-footer">
            <div class="tour-price-box">
              <span class="price-label">Giá niêm yết OTA</span>
              <span class="price-value">${formatVND(t.price)}</span>
            </div>
            <div class="tour-card-actions">
              <button type="button" class="btn-detail view-tour-btn" data-id="${t.id}">Chi tiết</button>
              <button type="button" class="btn-book-quick book-tour-btn" data-id="${t.id}">Đặt qua OTA</button>
            </div>
          </div>
        </div>
      </article>
    `).join('');

    renderPagination();
    attachCardEvents();
  }

  function renderPagination() {
    const totalPages = Math.ceil(state.filteredTours.length / state.pageSize);
    if (totalPages <= 1) {
      paginationWrapper.innerHTML = '';
      return;
    }

    let buttons = '';
    buttons += `<button type="button" class="page-btn" ${state.currentPage === 1 ? 'disabled' : ''} data-page="${state.currentPage - 1}">«</button>`;

    for (let p = 1; p <= totalPages; p++) {
      if (p === 1 || p === totalPages || (p >= state.currentPage - 1 && p <= state.currentPage + 1)) {
        buttons += `<button type="button" class="page-btn ${p === state.currentPage ? 'active' : ''}" data-page="${p}">${p}</button>`;
      } else if (p === state.currentPage - 2 || p === state.currentPage + 2) {
        buttons += `<span style="padding: 0 0.25rem;">...</span>`;
      }
    }

    buttons += `<button type="button" class="page-btn" ${state.currentPage === totalPages ? 'disabled' : ''} data-page="${state.currentPage + 1}">»</button>`;

    paginationWrapper.innerHTML = buttons;

    paginationWrapper.querySelectorAll('.page-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const page = parseInt(e.currentTarget.getAttribute('data-page'));
        if (page && page !== state.currentPage && page >= 1 && page <= totalPages) {
          state.currentPage = page;
          renderTours();
          document.getElementById('toursSection').scrollIntoView({ behavior: 'smooth' });
        }
      });
    });
  }

  function resetAllFilters() {
    state.activeRegion = 'all';
    state.searchQuery = '';
    state.priceFilter = 'all';
    state.sortOption = 'featured';
    
    searchInput.value = '';
    regionFilter.value = 'all';
    priceFilter.value = 'all';
    sortSelect.value = 'featured';

    tabButtons.forEach(b => b.classList.toggle('active', b.getAttribute('data-region') === 'all'));
    applyFilters();
  }

  // =========================================================================
  // 4. ACCESSIBLE MODAL FOR TOUR DETAILS
  // =========================================================================
  function attachCardEvents() {
    document.querySelectorAll('.view-tour-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.getAttribute('data-id');
        openTourModal(id);
      });
    });

    document.querySelectorAll('.book-tour-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.getAttribute('data-id');
        const tour = state.allTours.find(t => t.id === id);
        
        // Ghi nhận booking request vào Firebase / Local
        if (window.FirebaseService) {
          window.FirebaseService.recordBooking({
            tourId: tour.id,
            tourName: tour.name,
            operator: tour.operator,
            price: tour.price,
            duration: tour.duration,
            departure: tour.departure
          });
        }

        openChatbot();
        sendBotReply(`
          <p>Quý khách đã chọn đặt tour qua sàn OTA VietJourneys:</p>
          <div style="background: white; border-left: 3px solid #0a5c36; padding: 0.6rem; margin: 0.5rem 0; border-radius: 4px; border: 1px solid #e2e8e5;">
            <strong>${tour.name}</strong><br>
            🏛️ <strong>Nhà điều hành phụ trách:</strong> ${tour.operator}<br>
            💰 <strong>Giá trọn gói:</strong> ${formatVND(tour.price)} • ⏱️ ${tour.duration}
          </div>
          <p>Trợ lý AI OTA đang sẵn sàng điều phối booking này sang hệ thống của <strong>${tour.operator}</strong>. Quý khách vui lòng cho biết <strong>Ngày dự kiến khởi hành</strong> và <strong>Số lượng người lớn, trẻ em</strong> để tiến hành giữ chỗ nhé!</p>
        `);
      });
    });
  }

  function openTourModal(tourId) {
    const tour = state.allTours.find(t => t.id === tourId);
    if (!tour) return;

    modalBody.innerHTML = `
      <div class="modal-header-banner">
        <div class="modal-tags">
          <span class="tag-region">${tour.region}</span>
          <span class="tag-id">${tour.id}</span>
          <span style="font-size: 0.8rem; background: #e0f2fe; color: #0284c7; padding: 0.2rem 0.6rem; border-radius: 999px; font-weight: 600;">${tour.category}</span>
        </div>
        <h2 class="modal-tour-title" id="modalTourTitle">${tour.name}</h2>
        <div style="margin-top: 0.5rem; display: flex; align-items: center; gap: 0.75rem;">
          <span class="tour-operator-badge" style="font-size: 0.85rem;">🏛️ Đơn vị điều hành: <strong>${tour.operator}</strong></span>
          <span style="font-size: 0.85rem; color: #b45309; font-weight: 700;">⭐ ${tour.rating} (${tour.reviews_count} đánh giá)</span>
        </div>
      </div>

      <div class="modal-meta-grid">
        <div class="modal-meta-item">
          <strong>Thời Lượng</strong>
          <span>⏱️ ${tour.duration}</span>
        </div>
        <div class="modal-meta-item">
          <strong>Điểm Khởi Hành</strong>
          <span>📍 ${tour.departure}</span>
        </div>
        <div class="modal-meta-item">
          <strong>Phương Tiện</strong>
          <span>🚗 ${tour.transport}</span>
        </div>
        <div class="modal-meta-item">
          <strong>Giá Niêm Yết OTA</strong>
          <span>${formatVND(tour.price)}</span>
        </div>
      </div>

      <h3 class="modal-section-title">🌟 Điểm Nhấn Chương Trình</h3>
      <ul style="padding-left: 1.25rem; margin-bottom: 1.25rem; font-size: 0.95rem; line-height: 1.6;">
        ${tour.highlights.map(h => `<li>${h}</li>`).join('')}
      </ul>

      <h3 class="modal-section-title">🗺️ Lịch Trình Chi Tiết (Travel Operator)</h3>
      <div class="modal-schedule-box">
        <p>${tour.schedule}</p>
      </div>

      <h3 class="modal-section-title">🛡️ Cam Kết Chất Lượng Nền Tảng OTA</h3>
      <p style="font-size: 0.9rem; color: #4b5563; line-height: 1.6;">
        Được vận hành bởi <strong>${tour.operator}</strong> và bảo chứng chất lượng bởi VietJourneys OTA: Bao gồm xe vận chuyển đời mới, bảo hiểm du lịch Bảo Việt 100.000.000 VNĐ, cam kết đúng lịch trình và không phụ thu ẩn.
      </p>

      <div class="modal-book-box">
        <div>
          <span style="font-size: 0.8rem; color: #6b7280; display: block;">Giá trọn gói đảm bảo</span>
          <span style="font-size: 1.5rem; font-weight: 800; color: #0a5c36;">${formatVND(tour.price)}</span>
        </div>
        <button type="button" class="modal-btn-confirm" id="modalConfirmBtn" data-id="${tour.id}">
          💬 Đặt Tour & Điều Phối Qua AI
        </button>
      </div>
    `;

    document.getElementById('modalConfirmBtn').addEventListener('click', () => {
      tourModal.close();
      openChatbot();
      sendBotReply(`
        <p>Quý khách đang quan tâm đến tour <strong>${tour.name}</strong> của đối tác <strong>${tour.operator}</strong>.</p>
        <p>Tôi là Trợ lý AI OTA, tôi sẽ hỗ trợ quý khách kết nối trực tiếp với nhà điều hành để cập nhật tình trạng chỗ trống theo thời gian thực. Quý khách dự kiến đi bao nhiêu người?</p>
      `);
    });

    // Native showModal
    tourModal.showModal();
  }

  modalCloseBtn.addEventListener('click', () => tourModal.close());

  // Click outside to dismiss modal (Graceful degradation for browsers lacking closedby="any")
  if (!('closedBy' in HTMLDialogElement.prototype)) {
    const outside = (e, dialog) => {
      const r = dialog.getBoundingClientRect();
      return e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
    };
    let pressedOutside = false;
    tourModal.addEventListener('pointerdown', (e) => { pressedOutside = outside(e, tourModal); });
    tourModal.addEventListener('pointerup', (e) => { if (pressedOutside && outside(e, tourModal)) tourModal.close(); });
  }

  // =========================================================================
  // 5. EVENT LISTENERS FOR CONTROLS
  // =========================================================================
  tabButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      tabButtons.forEach(b => b.classList.remove('active'));
      e.currentTarget.classList.add('active');
      const region = e.currentTarget.getAttribute('data-region');
      state.activeRegion = region;
      regionFilter.value = region;
      applyFilters();
    });
  });

  regionFilter.addEventListener('change', (e) => {
    const region = e.target.value;
    state.activeRegion = region;
    tabButtons.forEach(b => b.classList.toggle('active', b.getAttribute('data-region') === region));
    applyFilters();
  });

  priceFilter.addEventListener('change', (e) => {
    state.priceFilter = e.target.value;
    applyFilters();
  });

  sortSelect.addEventListener('change', (e) => {
    state.sortOption = e.target.value;
    applyFilters();
  });

  searchSubmitBtn.addEventListener('click', () => {
    state.searchQuery = searchInput.value;
    applyFilters();
    document.getElementById('toursSection').scrollIntoView({ behavior: 'smooth' });
  });

  searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      state.searchQuery = searchInput.value;
      applyFilters();
      document.getElementById('toursSection').scrollIntoView({ behavior: 'smooth' });
    }
  });

  document.querySelectorAll('.footer-links a[data-query]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const q = e.currentTarget.getAttribute('data-query');
      searchInput.value = q;
      state.searchQuery = q;
      applyFilters();
      document.getElementById('toursSection').scrollIntoView({ behavior: 'smooth' });
    });
  });

  document.querySelectorAll('.faq-card .faq-question').forEach(questionBtn => {
    questionBtn.addEventListener('click', () => {
      const card = questionBtn.closest('.faq-card');
      const isOpen = card.classList.contains('open');
      document.querySelectorAll('.faq-card').forEach(c => c.classList.remove('open'));
      if (!isOpen) {
        card.classList.add('open');
        questionBtn.setAttribute('aria-expanded', 'true');
      } else {
        questionBtn.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // =========================================================================
  // 6. GOOGLE GEMINI AI OTA DISPATCHER & ASSISTANT ENGINE
  // =========================================================================
  const GEMINI_CONFIG = {
    apiKey: localStorage.getItem('gemini_api_key') || atob("QVEuQWI4Uk42TGlieEpXNVk1dW5Tc0pxNHE3YzNPMXY2aDBnLU9YNE9BU0FUcFBoVDUzYXc="),
    model: "gemini-3.8-flash",
    endpoint: "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"
  };

  const SYSTEM_INSTRUCTION = `
Bạn là "Trợ lý AI VietJourneys OTA" - chuyên gia tư vấn du lịch thông minh thuộc sàn lữ hành trực tuyến VietJourneys OTA Marketplace (kết nối mạng lưới tour đa dạng từ 150+ Travel Operators khắp 63 tỉnh thành Việt Nam).

NHIỆM VỤ CỐT LÕI:
1. Tư vấn lịch trình, gợi ý tour du lịch theo địa danh, ngân sách, số ngày và sở thích của khách dựa trên dữ liệu được cung cấp.
2. Mỗi khi gợi ý một tour cụ thể, BẮT BUỘC nêu rõ:
   - Tên tour
   - Mã tour (ví dụ: OTA-VN0001)
   - Giá niêm yết OTA (bằng VNĐ)
   - Đơn vị điều hành tour (Travel Operator) phụ trách
3. Khi khách có nhu cầu đặt tour, hướng dẫn khách cung cấp: Số điện thoại + Ngày khởi hành dự kiến + Số lượng người lớn/trẻ em để hệ thống AI OTA chuyển tiếp booking (dispatch) sang Travel Operator phụ trách giữ chỗ.
4. Trả lời chính xác chính sách vé trẻ em: Dưới 5 tuổi miễn phí; 5 đến dưới 10 tuổi tính 75%; từ 10 tuổi trở lên tính 100%.
5. Chính sách dời hủy tour: Trước 20 ngày phí 10% cọc; 10-19 ngày phí 30%; 5-9 ngày phí 50%; 2-4 ngày phí 70%; trong 24h phí 100%.

PHONG CÁCH HỘI THOẠI:
- Luôn thân thiện, niềm nở, hiếu khách, xưng "em/tôi" và gọi khách là "quý khách" hoặc "bạn".
- Câu trả lời súc tích, định dạng gạch đầu dòng rõ ràng, không dài dòng lan man.
- Nếu không có thông tin, lịch sự hướng dẫn liên hệ Hotline OTA 1900 6868.
`;

  async function callGeminiAI(userQuery, retrievedToursContext) {
    const promptText = `
DỮ LIỆU CÁC TOUR LIÊN QUAN TRONG HỆ THỐNG OTA:
${retrievedToursContext}

CÂU HỎI CỦA KHÁCH HÀNG:
"${userQuery}"

Hãy đóng vai Trợ lý AI VietJourneys OTA trả lời khách hàng một cách tự nhiên, chuyên nghiệp và chính xác theo dữ liệu trên.
`;

    try {
      const response = await fetch(`${GEMINI_CONFIG.endpoint}?key=${GEMINI_CONFIG.apiKey}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          system_instruction: {
            parts: [{ text: SYSTEM_INSTRUCTION }]
          },
          contents: [{
            parts: [{ text: promptText }]
          }],
          generationConfig: {
            temperature: 0.7,
            maxOutputTokens: 1000
          }
        })
      });

      if (!response.ok) {
        throw new Error(`Gemini API error: ${response.status}`);
      }

      const data = await response.json();
      const rawAnswer = data.candidates?.[0]?.content?.parts?.[0]?.text;
      if (!rawAnswer) throw new Error('Không nhận được nội dung từ Gemini');
      
      return formatAITextToHTML(rawAnswer);
    } catch (err) {
      console.warn('Lỗi gọi Gemini API, chuyển sang chế độ Local RAG:', err);
      return generateOTAEngineResponse(userQuery);
    }
  }

  function formatAITextToHTML(text) {
    // Chuyển đổi định dạng Markdown cơ bản sang HTML
    let formatted = text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/`([^`]+)`/g, '<code style="background:#e5e7eb;padding:0.1rem 0.3rem;border-radius:3px;">$1</code>')
      .replace(/\n\n/g, '</p><p style="margin-top:0.5rem;">')
      .replace(/\n\*/g, '<br>•')
      .replace(/\n-/g, '<br>•')
      .replace(/\n/g, '<br>');

    // Tự động tìm mã tour (OTA-VNxxxx) và gắn nút xem chi tiết nhanh
    const tourIdRegex = /(OTA-VN\d{4})/g;
    formatted = formatted.replace(tourIdRegex, (match) => {
      return `<strong style="color:#0a5c36;">${match}</strong> <button type="button" class="btn-detail chat-tour-preview-btn" data-id="${match}" style="padding:0.15rem 0.4rem;font-size:0.7rem;margin-left:0.2rem;">Xem</button>`;
    });

    return `<p>${formatted}</p>`;
  }

  function getRelevantToursContext(query) {
    const q = query.toLowerCase();
    let matches = state.allTours.filter(t => 
      t.name.toLowerCase().includes(q) ||
      t.destination.toLowerCase().includes(q) ||
      t.region.toLowerCase().includes(q) ||
      t.operator.toLowerCase().includes(q) ||
      t.highlights.some(h => h.toLowerCase().includes(q))
    );

    if (matches.length === 0) {
      // Lấy ngẫu nhiên hoặc top 5 tour nổi bật
      matches = state.allTours.slice(0, 5);
    } else {
      matches = matches.slice(0, 5);
    }

    return matches.map(t => 
      `- Mã tour: ${t.id} | Tên: ${t.name} | Vùng: ${t.region} | Điểm đến: ${t.destination} | Thời lượng: ${t.duration} | Giá OTA: ${formatVND(t.price)} | Travel Operator: ${t.operator} | Phương tiện: ${t.transport} | Điểm nổi bật: ${t.highlights.join(', ')}`
    ).join('\n');
  }
  function openChatbot() {
    chatbotWindow.removeAttribute('hidden');
    chatbotLauncherBtn.setAttribute('aria-expanded', 'true');
    if (chatUserInput) chatUserInput.focus();
  }

  function closeChatbot() {
    chatbotWindow.setAttribute('hidden', '');
    chatbotLauncherBtn.setAttribute('aria-expanded', 'false');
  }

  chatbotLauncherBtn.addEventListener('click', () => {
    const isHidden = chatbotWindow.hasAttribute('hidden');
    if (isHidden) openChatbot();
    else closeChatbot();
  });

  closeChatBtn.addEventListener('click', closeChatbot);
  openChatbotTopBtn.addEventListener('click', openChatbot);
  openChatbotFooterBtn.addEventListener('click', openChatbot);

  clearChatBtn?.addEventListener('click', () => {
    if (chatMessages) {
      chatMessages.innerHTML = `
        <div class="message bot-message">
          <div class="msg-avatar">🤖</div>
          <div class="msg-bubble">
            <p>Hội thoại đã được làm mới! Tôi là Trợ lý AI OTA VietJourneys, sẵn sàng tư vấn và điều phối mạng lưới tour từ các Travel Operators uy tín. Quý khách muốn khám phá vùng đất nào?</p>
            <span class="msg-time">Vừa xong</span>
          </div>
        </div>
      `;
    }
  });

  document.querySelectorAll('.prompt-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const q = chip.getAttribute('data-question');
      openChatbot();
      handleUserMessage(q);
    });
  });

  document.querySelectorAll('.chat-pill').forEach(pill => {
    pill.addEventListener('click', () => {
      const q = pill.getAttribute('data-ask');
      handleUserMessage(q);
    });
  });

  chatInputForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const message = chatUserInput?.value?.trim();
    if (!message) return;
    chatUserInput.value = '';
    handleUserMessage(message);
  });

  function addUserMessage(text) {
    const timeStr = new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
    const msgEl = document.createElement('div');
    msgEl.className = 'message user-message';
    msgEl.innerHTML = `
      <div class="msg-bubble">
        <p>${escapeHTML(text)}</p>
        <span class="msg-time">${timeStr}</span>
      </div>
    `;
    chatMessages.appendChild(msgEl);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function sendBotReply(htmlContent) {
    const timeStr = new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
    const msgEl = document.createElement('div');
    msgEl.className = 'message bot-message';
    msgEl.innerHTML = `
      <div class="msg-avatar">🤖</div>
      <div class="msg-bubble">
        ${htmlContent}
        <span class="msg-time">${timeStr}</span>
      </div>
    `;
    chatMessages.appendChild(msgEl);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    msgEl.querySelectorAll('.chat-tour-preview-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const id = e.currentTarget.getAttribute('data-id');
        openTourModal(id);
      });
    });
  }

  function escapeHTML(str) {
    return str.replace(/[&<>'"]/g, 
      tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
    );
  }

  async function handleUserMessage(query) {
    addUserMessage(query);

    const typingId = 'typing-' + Date.now();
    const typingEl = document.createElement('div');
    typingEl.id = typingId;
    typingEl.className = 'message bot-message';
    typingEl.innerHTML = `
      <div class="msg-avatar">🤖</div>
      <div class="msg-bubble" style="color: #6b7280; font-style: italic;">
        Trợ lý Google Gemini AI đang phân tích dữ liệu tour và điều phối...
      </div>
    `;
    chatMessages.appendChild(typingEl);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    const context = getRelevantToursContext(query);
    const answer = await callGeminiAI(query, context);

    document.getElementById(typingId)?.remove();
    sendBotReply(answer);

    // Lưu log câu hỏi và câu trả lời vào Firebase Firestore
    if (window.FirebaseService) {
      window.FirebaseService.recordChatLog(query, answer);
    }
  }

  function generateOTAEngineResponse(rawQuery) {
    const q = rawQuery.toLowerCase();

    // 1. OTA Dispatcher Intent: Quy trình điều phối
    if (q.includes('travel operator') || q.includes('nhà điều hành') || q.includes('quy trình') || q.includes('chuyển giao') || q.includes('ota là gì')) {
      return `
        <p><strong>🌐 Quy trình kết nối & điều phối booking trên OTA VietJourneys:</strong></p>
        <ol style="padding-left: 1.2rem; margin: 0.5rem 0; line-height: 1.6;">
          <li><strong>Khách hàng chọn tour:</strong> Tra cứu các tour du lịch và trò chuyện cùng Trợ lý AI OTA.</li>
          <li><strong>AI khớp lệnh (Matching & Routing):</strong> Chuyển yêu cầu booking tới <em>Travel Operator phụ trách</em> tại địa phương (ví dụ: Halong Cruises, Sapa Discovery, Mekong Riverways...).</li>
          <li><strong>Giữ chỗ & Phục vụ:</strong> Travel Operator chuẩn bị xe, HDV đón tiếp; VietJourneys OTA cam kết giá niêm yết chuẩn và bảo hiểm du lịch 100 triệu VNĐ.</li>
        </ol>
      `;
    }

    // 2. FAQ: Trẻ em
    if (q.includes('trẻ em') || q.includes('em bé') || q.includes('tuổi')) {
      return `
        <p><strong>👶 Chính sách giá vé trẻ em áp dụng chung trên hệ thống OTA:</strong></p>
        <ul style="padding-left: 1.2rem; margin: 0.5rem 0;">
          <li><strong>Dưới 5 tuổi:</strong> Miễn phí 100% giá tour (2 người lớn kèm tối đa 1 bé).</li>
          <li><strong>Từ 5 đến dưới 10 tuổi:</strong> 75% giá tour người lớn (suất ăn riêng, ghế ngồi riêng, ngủ cùng bố mẹ).</li>
          <li><strong>Từ 10 tuổi trở lên:</strong> 100% giá người lớn tiêu chuẩn.</li>
        </ul>
      `;
    }

    // 3. FAQ: Hủy tour
    if (q.includes('hủy tour') || q.includes('hoàn tiền') || q.includes('dời ngày')) {
      return `
        <p><strong>📋 Quy định dời & hủy tour OTA:</strong></p>
        <ul style="padding-left: 1.2rem; margin: 0.5rem 0;">
          <li>Hủy trước 20 ngày: Phí 10% tiền cọc.</li>
          <li>Hủy từ 10 - 19 ngày: Phí 30% giá tour.</li>
          <li>Hủy từ 05 - 09 ngày: Phí 50% giá tour.</li>
          <li>Hủy từ 02 - 04 ngày: Phí 70% giá tour.</li>
          <li>Hủy trong vòng 24h: Phí 100% giá tour.</li>
        </ul>
        <p><em>*Trường hợp thiên tai, bão lũ được hỗ trợ dời ngày hoặc bảo lưu 100% trong 12 tháng.</em></p>
      `;
    }

    // 4. Intent: Giá rẻ / Dưới 1 triệu / Dưới 2 triệu
    if (q.includes('dưới 1 triệu') || q.includes('dưới 1tr')) {
      const matched = state.allTours.filter(t => t.price < 1000000).slice(0, 4);
      return renderMatchedToursHTML(matched, 'Gợi ý các tour từ các Travel Operators giá dưới 1.000.000 VNĐ:');
    }

    if (q.includes('dưới 2 triệu') || q.includes('dưới 2tr')) {
      const matched = state.allTours.filter(t => t.price < 2000000).slice(0, 4);
      return renderMatchedToursHTML(matched, 'Gợi ý các tour từ các Travel Operators giá dưới 2.000.000 VNĐ:');
    }

    // 5. Destination Search in 1.000 Tours
    const keywords = [
      'hạ long', 'sapa', 'fansipan', 'hà giang', 'ninh bình', 'tràng an', 'cát bà',
      'đà nẵng', 'hội an', 'huế', 'phong nha', 'quy nhơn', 'phú yên', 'nha trang',
      'mũi né', 'phú quý', 'lý sơn', 'đà lạt', 'buôn ma thuột', 'măng đen', 'tà đùng',
      'sài gòn', 'củ chi', 'tây ninh', 'núi bà đen', 'miền tây', 'cần thơ', 'an giang',
      'cà mau', 'nam du', 'hòn sơn', 'phú quốc', 'côn đảo', 'trekking', 'săn mây',
      'du thuyền', 'hang én', 'xuyên việt'
    ];

    let foundKeyword = keywords.find(kw => q.includes(kw));
    if (foundKeyword) {
      let matched = state.allTours.filter(t => 
        t.name.toLowerCase().includes(foundKeyword) ||
        t.destination.toLowerCase().includes(foundKeyword) ||
        t.schedule.toLowerCase().includes(foundKeyword)
      );

      if (matched.length > 0) {
        return renderMatchedToursHTML(matched.slice(0, 4), `Hệ thống tìm thấy <strong>${matched.length} chương trình tour</strong> tại "${foundKeyword.toUpperCase()}" từ các nhà điều hành đối tác:`);
      }
    }

    // 6. Fallback General Search
    const generalMatches = state.allTours.filter(t => {
      const words = q.split(/\s+/).filter(w => w.length > 2);
      return words.some(w => t.name.toLowerCase().includes(w) || t.operator.toLowerCase().includes(w));
    });

    if (generalMatches.length > 0) {
      return renderMatchedToursHTML(generalMatches.slice(0, 4), `Gợi ý các tour phù hợp trên hệ thống OTA:`);
    }

    return `
      <p>Cảm ơn quý khách! Nền tảng OTA VietJourneys hiện kết nối mạng lưới tour phong phú từ <strong>150+ Travel Operators</strong> (Hạ Long, Sapa, Hà Giang, Đà Nẵng, Phú Quốc, Côn Đảo, Cần Thơ...).</p>
      <p>Quý khách vui lòng nhập tên điểm đến (ví dụ: <em>"Hạ Long"</em>, <em>"Đà Lạt"</em>, <em>"Côn Đảo"</em>) hoặc mức giá mong muốn (ví dụ: <em>"tour dưới 2 triệu"</em>) để Trợ lý AI OTA hỗ trợ ngay nhé!</p>
    `;
  }

  function renderMatchedToursHTML(tours, heading) {
    return `
      <p><strong>${heading}</strong></p>
      <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.5rem;">
        ${tours.map(t => `
          <div style="background: white; border: 1px solid #e2e8e5; border-radius: 8px; padding: 0.65rem; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <div style="font-weight: 700; color: #0a5c36; font-size: 0.85rem; line-height: 1.3;">${t.name}</div>
            <div style="font-size: 0.75rem; color: #0284c7; margin: 0.2rem 0;">🏛️ Nhà điều hành: <strong>${t.operator}</strong></div>
            <div style="font-size: 0.75rem; color: #6b7280;">⏱️ ${t.duration} • ⭐ ${t.rating}</div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 0.4rem;">
              <span style="font-weight: 800; color: #d97706; font-size: 0.95rem;">${formatVND(t.price)}</span>
              <button type="button" class="btn-detail chat-tour-preview-btn" data-id="${t.id}" style="padding: 0.25rem 0.5rem; font-size: 0.75rem;">Xem lịch trình</button>
            </div>
          </div>
        `).join('')}
      </div>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #065f46;">Quý khách bấm <strong>"Xem lịch trình"</strong> hoặc báo ngày đi để AI OTA chuyển tiếp booking tới nhà điều hành nhé!</p>
    `;
  }

  // Load initial data
  loadToursData();
});
