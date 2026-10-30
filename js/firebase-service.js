/**
 * VIETJOURNEYS OTA - FIREBASE FIRESTORE INTEGRATION SERVICE
 * Serves Master's Thesis empirical data collection:
 * 1. 'bookings': Records customer tour bookings dispatched to Travel Operators.
 * 2. 'chat_logs': Records conversation logs with AI Assistant for thesis empirical metrics (accuracy, intent, volume).
 */

const FIREBASE_CONFIG_STORAGE_KEY = 'vietjourneys_firebase_config';

// FIREBASE CONFIG CHÍNH THỨC CỦA DỰ ÁN
const defaultFirebaseConfig = {
  apiKey: "AIzaSyAPy8_1S8V1fgxaa_UmgIRMfuCAzSPH98o",
  authDomain: "website-otas-vietnam.firebaseapp.com",
  projectId: "website-otas-vietnam",
  storageBucket: "website-otas-vietnam.firebasestorage.app",
  messagingSenderId: "65033967168",
  appId: "1:65033967168:web:53770e24de491cde77f1a5",
  measurementId: "G-CHF3M33TB0"
};

let db = null;
let isConnected = false;

function initFirebase() {
  // Check localStorage for any custom config saved via UI, or use default
  let config = defaultFirebaseConfig;
  const savedConfig = localStorage.getItem(FIREBASE_CONFIG_STORAGE_KEY);
  if (savedConfig) {
    try {
      config = JSON.parse(savedConfig);
    } catch (e) {
      console.warn('Lỗi đọc config Firebase từ localStorage:', e);
    }
  }

  // Validate if real keys are provided
  if (config.apiKey && config.apiKey !== "YOUR_API_KEY" && typeof firebase !== 'undefined') {
    try {
      if (!firebase.apps.length) {
        firebase.initializeApp(config);
      }
      db = firebase.firestore();
      if (typeof firebase.analytics === 'function') {
        firebase.analytics();
      }
      isConnected = true;
      console.log('✅ Firebase Firestore & Analytics đã kết nối thành công tới project website-otas-vietnam!');
    } catch (err) {
      console.error('❌ Lỗi khởi tạo Firebase:', err);
    }
  } else {
    console.log('ℹ️ Firebase đang ở chế độ chờ cấu hình (Fallback LocalStorage). Để lưu đám mây, hãy nhập Firebase Config.');
  }
}

/**
 * Lưu đơn đặt tour gửi tới Travel Operator
 */
async function recordBooking(bookingData) {
  const payload = {
    ...bookingData,
    createdAt: new Date().toISOString(),
    status: 'pending_operator_dispatch',
    platform: 'VietJourneys_OTA_Marketplace'
  };

  if (isConnected && db) {
    try {
      const docRef = await db.collection('bookings').add(payload);
      console.log('Booking đã lưu lên Firestore với ID:', docRef.id);
      return { success: true, id: docRef.id, cloud: true };
    } catch (e) {
      console.error('Lỗi lưu booking Firestore:', e);
    }
  }

  // Fallback local storage
  const localBookings = JSON.parse(localStorage.getItem('vietjourneys_bookings') || '[]');
  localBookings.push(payload);
  localStorage.setItem('vietjourneys_bookings', JSON.stringify(localBookings));
  return { success: true, local: true };
}

/**
 * Lưu nhật ký hội thoại AI Chatbot (Phục vụ số liệu nghiên cứu Luận văn)
 */
async function recordChatLog(query, answer, contextTourId = null) {
  const logItem = {
    timestamp: new Date().toISOString(),
    userQuery: query,
    aiAnswerSnippet: answer.replace(/<[^>]*>?/gm, '').substring(0, 300),
    contextTourId: contextTourId,
    userAgent: navigator.userAgent
  };

  if (isConnected && db) {
    try {
      await db.collection('chat_logs').add(logItem);
      return;
    } catch (e) {
      console.error('Lỗi ghi chat log Firestore:', e);
    }
  }

  // Fallback local storage
  const localLogs = JSON.parse(localStorage.getItem('vietjourneys_chat_logs') || '[]');
  localLogs.push(logItem);
  localStorage.setItem('vietjourneys_chat_logs', JSON.stringify(localLogs.slice(-200)));
}

// Khởi chạy khi load script
if (typeof window !== 'undefined') {
  window.addEventListener('DOMContentLoaded', initFirebase);
  window.FirebaseService = {
    recordBooking,
    recordChatLog,
    isConnected: () => isConnected,
    saveConfig: (newConfig) => {
      localStorage.setItem(FIREBASE_CONFIG_STORAGE_KEY, JSON.stringify(newConfig));
      location.reload();
    }
  };
}
