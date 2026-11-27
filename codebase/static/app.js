/* Travel SOS — UI logic. Một màn hình chat, nhiều trạng thái (docs/wireframe.md).
   Không thư viện ngoài. Agent gọi qua POST /api/answer (codebase/web.py). */
"use strict";

/* ---- i18n: người dùng chọn ngôn ngữ trả lời trên giao diện (PRD bước 1) ---- */
const I18N = {
  en: {
    welcomeLine: "We're here when your trip doesn't go to plan.",
    welcomeAsk: "First — which language should I reply in?",
    welcomeNote: "I only suggest steps — every action is yours to decide.",
    greeting: "Hi! I'm here to help. Tell me what happened, whenever you're ready — for example: \"I lost my passport in Hanoi\".",
    placeholder: "Describe your situation…",
    tabs: [
      { label: "🛂 Lost passport", questions: [
        "I lost my passport — what should I do?",
        "What documents do I need to report it at the police station?",
        "I already have the police report — what's next?",
        "How long does the whole process take?",
      ]},
      { label: "✈️ Missed flight", questions: [
        "I missed my flight — what are my options?",
        "My flight was delayed for hours — what am I entitled to?",
      ]},
      { label: "🏨 Hotel cancelled", questions: [
        "My hotel cancelled my room late at night — what should I do?",
      ]},
      { label: "🗣️ Phrases", questions: [
        "Give me a short Vietnamese phrase to show the police",
        "How do I say \"I need help\" in Vietnamese?",
      ]},
      { label: "🚨 Emergency", questions: [
        "I was just robbed and I'm hurt — what do I do?",
      ]},
    ],
    sourceNote: "Sources and their viewed dates come from the team's playbook (PB-xx). Numbers can change — always confirm before you travel.",
    emergency: { title: "🚨 CALL NOW", police: "113 Police", ambulance: "115 Ambulance",
                 note: "Then contact your embassy. I can't give medical advice — call first, I'll help with the rest." },
    langNote: "(Please reply in English.)",
    typing: "Typing…",
    errorPrefix: "Sorry, something went wrong: ",
    micTitle: "Speak instead of typing",
    micOff: "⏹ Mic off",
    listening: "🎙️ Listening… pause 5s to auto-send",
    micUnsupported: "Voice input isn't supported in this browser — please type instead.",
    voiceTitle: "Agent speaks its replies aloud",
    speaking: "🔊 Speaking… tap to stop",
    voiceUnsupported: "Speech output isn't supported in this browser — staying in chat mode.",
    switched: "Sure — I'll reply in English from now on. How can I help?",
  },
  vi: {
    welcomeLine: "Mình luôn ở đây khi chuyến đi không theo kế hoạch.",
    welcomeAsk: "Trước tiên — bạn muốn mình trả lời bằng ngôn ngữ nào?",
    welcomeNote: "Mình chỉ tư vấn các bước — mọi hành động bạn tự quyết.",
    greeting: "Chào bạn, mình luôn ở đây để giúp bạn. Khi nào sẵn sàng thì kể mình nghe chuyện gì đang xảy ra nhé... ví dụ như: \"Tôi bị mất hộ chiếu ở Hà Nội\".",
    placeholder: "Nhắn tình huống của bạn…",
    tabs: [
      { label: "🛂 Mất hộ chiếu", questions: [
        "Tôi bị mất hộ chiếu — phải làm gì?",
        "Ra đồn công an cần mang theo giấy tờ gì?",
        "Tôi đã có biên bản trình báo — bước tiếp theo là gì?",
        "Toàn bộ quy trình mất khoảng bao lâu?",
      ]},
      { label: "✈️ Lỡ chuyến bay", questions: [
        "Tôi lỡ chuyến bay — có phương án gì bây giờ?",
        "Chuyến bay bị hoãn nhiều giờ — tôi có quyền lợi gì?",
      ]},
      { label: "🏨 Khách sạn huỷ phòng", questions: [
        "Khách sạn báo huỷ phòng lúc tối muộn — tôi phải làm gì?",
      ]},
      { label: "🗣️ Câu khẩn cấp", questions: [
        "Cho tôi câu tiếng Việt ngắn để đưa công an đọc",
        "Nói \"Tôi cần giúp đỡ\" bằng tiếng Việt thế nào?",
      ]},
      { label: "🚨 Khẩn cấp", questions: [
        "Tôi vừa bị cướp và bị thương — phải làm gì?",
      ]},
    ],
    sourceNote: "Nguồn và ngày xem lấy từ playbook của nhóm (PB-xx). Con số có thể thay đổi — luôn xác nhận trước khi di chuyển.",
    emergency: { title: "🚨 GỌI NGAY", police: "113 Công an", ambulance: "115 Cấp cứu",
                 note: "Rồi báo Đại sứ quán của bạn. Mình không tư vấn y tế được — gọi trước, mình giúp phần sau." },
    langNote: "(Hãy trả lời bằng tiếng Việt.)",
    typing: "Đang soạn…",
    errorPrefix: "Xin lỗi, có lỗi xảy ra: ",
    micTitle: "Nói thay vì gõ",
    micOff: "⏹ Tắt mic",
    listening: "🎙️ Đang nghe… dừng 5 giây sẽ tự gửi",
    micUnsupported: "Trình duyệt này chưa hỗ trợ nhập bằng giọng nói — bạn gõ giúp nhé.",
    voiceTitle: "Agent trả lời bằng giọng nói",
    speaking: "🔊 Đang nói… bấm để dừng",
    voiceUnsupported: "Trình duyệt này chưa hỗ trợ đọc giọng nói — quay lại chế độ chat.",
    switched: "Được nhé, từ giờ mình sẽ trả lời bằng tiếng Việt. Bạn cần giúp gì không?",
  },
};
const LANGS = { en: "English", vi: "Tiếng Việt" };

let lang = localStorage.getItem("sos-lang") || null;
const $ = (id) => document.getElementById(id);

/* ---- Màn chào ---- */
function buildLangButtons() {
  const wrap = $("lang-buttons");
  wrap.innerHTML = "";
  for (const [code, name] of Object.entries(LANGS)) {
    const b = document.createElement("button");
    b.textContent = name;
    b.addEventListener("click", () => enterChat(code));
    wrap.appendChild(b);
  }
}

function enterChat(code) {
  lang = code;
  localStorage.setItem("sos-lang", code);
  $("welcome").classList.add("hidden");
  $("chat").classList.remove("hidden");
  buildLangSelect();
  applyLang();
  $("input").focus();
  // Voice mode: bật lại mic (trạng thái "off" cũ không giữ sang phiên mới),
  // agent tự chào bằng giọng nói rồi mở mic cho user nói
  if (mode === "voice") {
    setMicEnabled(true);
    speak(I18N[lang].greeting, autoListen);
  }
}

/* ---- Chọn ngôn ngữ bất kỳ lúc nào ---- */
function buildLangSelect() {
  const sel = $("lang-select");
  sel.innerHTML = "";
  for (const [code, name] of Object.entries(LANGS)) {
    const o = document.createElement("option");
    o.value = code; o.textContent = "🌐 " + name;
    sel.appendChild(o);
  }
  sel.value = lang;
  sel.addEventListener("change", () => {
    stopListening();
    stopSpeaking();          // ngừng giọng cũ ngay
    lang = sel.value;
    localStorage.setItem("sos-lang", lang);
    applyLang();
    // Voice mode: xác nhận bằng giọng MỚI ngay, rồi mở mic
    if (mode === "voice") {
      speak(I18N[lang].switched, autoListen);
    }
  });
}

function applyLang() {
  const t = I18N[lang];
  document.documentElement.lang = lang;
  document.querySelector(".greeting").textContent = t.greeting;
  $("input").placeholder = t.placeholder;
  $("lang-select").value = lang;
  $("mic").title = t.micTitle;
  $("mode-voice").title = t.voiceTitle;
  buildTabs();
}

/* ---- Danh mục câu hỏi thường gặp (tab trên đầu) ---- */
let activeTab = 0;

function buildTabs() {
  const bar = $("category-tabs");
  bar.innerHTML = "";
  const tabs = I18N[lang].tabs;
  activeTab = Math.min(activeTab, tabs.length - 1);
  tabs.forEach((tab, i) => {
    const b = document.createElement("button");
    b.textContent = tab.label;
    b.classList.toggle("active", i === activeTab);
    b.addEventListener("click", () => { activeTab = i; buildTabs(); });
    bar.appendChild(b);
  });
  buildChips();
}

function buildChips() {
  const wrap = $("quick-chips");
  wrap.innerHTML = "";
  const questions = I18N[lang].tabs[activeTab]?.questions || [];
  for (const text of questions) {
    const b = document.createElement("button");
    b.textContent = text;
    b.addEventListener("click", () => { $("input").value = text; $("input").focus(); });
    wrap.appendChild(b);
  }
}

/* ---- Hiện tin nhắn ---- */
function addUser(text) {
  const d = document.createElement("div");
  d.className = "bubble user-bubble";
  d.textContent = text;
  $("messages").appendChild(d);
  scrollDown();
}

/* PB-xx trong câu trả lời → tag bấm được (wireframe 3.8) */
function addAgent(text) {
  const d = document.createElement("div");
  d.className = "bubble agent-bubble";
  for (const part of String(text).split(/(\[PB-\d+\])/g)) {
    const m = part.match(/^\[PB-(\d+)\]$/);
    if (m) {
      const chip = document.createElement("button");
      chip.className = "pb-chip";
      chip.textContent = "PB-" + m[1];
      chip.addEventListener("click", () => openSource("PB-" + m[1]));
      d.appendChild(chip);
    } else if (part) {
      d.appendChild(document.createTextNode(part));
    }
  }
  addWarnHint(d);
  $("messages").appendChild(d);
  scrollDown();
}

/* Nhắc "dự kiến" sau mỗi câu trả lời có con số — nguyên tắc "nói thật" */
function addWarnHint(bubble) {
  if (/\d+\s*(ngày|days|đồng|VND)/i.test(bubble.textContent)) {
    const w = document.createElement("div");
    w.className = "warn-block";
    w.textContent = "⚠️ " + (lang === "vi"
      ? "Thời gian / lệ phí chỉ là dự kiến — có thể thay đổi."
      : "Times and fees are estimates only — they can change.");
    bubble.appendChild(w);
  }
}

/* Thẻ khẩn cấp nổi trên cùng khi phát hiện từ khoá nguy hiểm (wireframe 3.6) */
const EMERGENCY_RE = /(115|113|bleeding|unconscious|robbed|mugged|stabbed|heart attack|bị cướp|bị thương|chảy máu|đau ngực|tai nạn|ngất)/i;

function addEmergency() {
  const e = I18N[lang].emergency;
  const d = document.createElement("div");
  d.className = "emergency-card";
  d.innerHTML = "";
  const title = document.createElement("div");
  title.className = "em-title"; title.textContent = e.title;
  const btns = document.createElement("div");
  btns.className = "em-buttons";
  for (const [label, num] of [[e.ambulance, "115"], [e.police, "113"]]) {
    const a = document.createElement("a");
    a.href = "tel:" + num; a.textContent = label;
    btns.appendChild(a);
  }
  const note = document.createElement("div");
  note.className = "em-note"; note.textContent = e.note;
  d.append(title, btns, note);
  $("messages").appendChild(d);
  scrollDown();
}

function addTyping() {
  const d = document.createElement("div");
  d.className = "typing";
  d.id = "typing";
  d.textContent = I18N[lang].typing;
  $("messages").appendChild(d);
  scrollDown();
}

function addError(msg) {
  const d = document.createElement("div");
  d.className = "bubble agent-bubble";
  d.textContent = I18N[lang].errorPrefix + msg;
  $("messages").appendChild(d);
  scrollDown();
}

function scrollDown() {
  const m = $("messages");
  m.scrollTop = m.scrollHeight;
}

/* ---- Gửi / nhận ---- */
async function send() {
  const input = $("input");
  const text = input.value.trim();
  if (!text) return;
  input.value = "";
  $("send").disabled = true;
  clearTimeout(autoSendTimer);
  autoSendTimer = null;
  stopListening();
  stopSpeaking();

  if (EMERGENCY_RE.test(text)) addEmergency();   // nổi trước mọi thứ, không chờ agent
  addUser(text);
  addTyping();

  try {
    const res = await fetch("/api/answer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text + "\n" + I18N[lang].langNote }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) {
      addError(data.error || "HTTP " + res.status);
    } else {
      $("typing").remove();
      addAgent(data.output || "");
      if (EMERGENCY_RE.test(String(data.output))) addEmergency();
      if (mode === "voice") {
        // Voice mode: agent đọc to, xong tự mở mic để tiếp tục hội thoại
        speak(data.output || "", autoListen);
      }
    }
  } catch (err) {
    $("typing")?.remove();
    addError(String(err));
  } finally {
    $("typing")?.remove();
    $("send").disabled = false;
    $("input").focus();
  }
}

/* ---- Toggle Chat / Voice ---- */
let mode = localStorage.getItem("sos-mode") || "chat";

function initModeToggle() {
  if (!window.speechSynthesis && mode === "voice") mode = "chat";
  for (const btn of document.querySelectorAll("#mode-toggle button")) {
    btn.addEventListener("click", () => {
      const next = btn.dataset.mode;
      if (next === "voice" && !window.speechSynthesis) {
        addError(I18N[lang].voiceUnsupported);
        return;
      }
      if (next === "chat") stopSpeaking();
      if (next === "voice") setMicEnabled(true);   // quay lại voice là mic bật lại
      setMode(next);
    });
  }
  setMode(mode);
}

function setMode(next) {
  mode = next;
  localStorage.setItem("sos-mode", mode);
  for (const btn of document.querySelectorAll("#mode-toggle button")) {
    btn.classList.toggle("active", btn.dataset.mode === mode);
  }
  setMicEnabled(micEnabled);   // nút Tắt mic chỉ hiện ở voice mode
  $("mode-voice").title = I18N[lang].voiceTitle;
}

/* ---- Agent đọc câu trả lời (giọng theo ngôn ngữ đã chọn) ---- */
function speechText(text) {
  return String(text)
    .replace(/\[PB-\d+\]/g, "")        // bỏ tag nguồn
    .replace(/[*_#>`]/g, "")           // bỏ markdown
    .replace(/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/gu, "") // bỏ emoji
    .replace(/\s+/g, " ")
    .trim();
}

function speak(text, onDone) {
  const clean = speechText(text);
  if (!clean) { onDone && onDone(); return; }
  stopSpeaking();
  const hint = document.createElement("div");
  hint.className = "speaking-hint";
  hint.id = "speaking-hint";
  hint.textContent = I18N[lang].speaking;
  hint.addEventListener("click", () => { stopSpeaking(); onDone && onDone(); });
  document.querySelector(".composer").before(hint);

  const u = new SpeechSynthesisUtterance(clean);
  u.lang = lang === "vi" ? "vi-VN" : "en-US";
  const voice = pickVoice(u.lang, lang);
  if (voice) u.voice = voice;
  const rate = lang === "vi" ? 1.05 : 0.95;  // chậm lại một chút cho giọng nhẹ nhàng
  u.rate = rate;
  u.pitch = 0.95;                            // hơi trầm xuống — ấm, dịu hơn

  // Một số trình duyệt không kích hoạt onend/onerror (đặc biệt khi giọng
  // tiếng Anh chọn không có sẵn) → mic sẽ không bao giờ được mở. Tự tính
  // thời lượng tối đa theo số từ và mở mic sau đó nếu onend chưa chạy.
  let done = false;
  const finish = () => {
    if (done) return;
    done = true;
    clearTimeout(fallback);
    $("avatar")?.classList.remove("talking");
    $("speaking-hint")?.remove();
    onDone && onDone();
  };
  const words = clean.split(/\s+/).length;
  const estMs = (words / (2.5 * rate)) * 1000 + 2500;
  const fallback = setTimeout(() => { try { speechSynthesis.cancel(); } catch (_) {} finish(); }, estMs);

  u.onstart = () => $("avatar")?.classList.add("talking");
  u.onend = finish;
  u.onerror = finish;
  speechSynthesis.speak(u);
}

/* Chọn giọng: tiếng Việt ưu tiên "Linh" — giọng nữ miền Bắc trẻ có sẵn trên
   macOS/iOS (nếu chưa có, cài ở System Settings → Accessibility → Spoken
   Content → Manage Voices → Vietnamese). Fallback: giọng vi-VN bất kỳ. */
function pickVoice(speechLang, lang) {
  const voices = speechSynthesis.getVoices();
  if (lang === "vi") {
    return voices.find(v => /linh/i.test(v.name) && v.lang.toLowerCase().startsWith("vi"))
      || voices.find(v => v.lang.toLowerCase().startsWith("vi"));
  }
  return voices.find(v => v.lang === speechLang)
    || voices.find(v => v.lang.startsWith(lang));
}

function stopSpeaking() {
  if (window.speechSynthesis) speechSynthesis.cancel();
  $("avatar")?.classList.remove("talking");
  $("speaking-hint")?.remove();
}

/* ---- Nói vào input (Web Speech API của trình duyệt, không thư viện) ---- */
const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition || null;
let recog = null;
let autoSendTimer = null;
let micEnabled = localStorage.getItem("sos-mic") !== "off";  // voice mode: agent có tự mở mic không

function setMicEnabled(on) {
  micEnabled = on;
  localStorage.setItem("sos-mic", on ? "on" : "off");
  $("mic").classList.toggle("off", !on);
  $("mic-off").classList.toggle("hidden", !(mode === "voice" && on));
  $("mic").title = on ? I18N[lang].micTitle : (lang === "vi" ? "Bấm để bật lại mic" : "Tap to re-enable mic");
}

function autoListen() {
  if (mode !== "voice" || !micEnabled) return;
  // Chrome cần nhả loa/mic sau khi tổng hợp giọng nói xong — mở mic ngay
  // lập tức có thể bị bỏ qua im lặng (đặc biệt giọng tiếng Anh) → trễ ngắn
  setTimeout(() => { if (mode === "voice" && micEnabled) startListening(); }, 400);
}

/* Voice mode: ngừng nói 5 giây → tự gửi, không cần bấm nút */
function armAutoSend() {
  clearTimeout(autoSendTimer);
  if (mode !== "voice") return;
  autoSendTimer = setTimeout(() => {
    autoSendTimer = null;
    if (mode === "voice" && !$("send").disabled && $("input").value.trim()) send();
  }, 5000);
}

function initMic() {
  const mic = $("mic");
  if (!SpeechRec) {          // trình duyệt không hỗ trợ (vd Firefox) → ẩn nút
    mic.classList.add("hidden");
    return;
  }
  mic.title = I18N[lang].micTitle;
  mic.addEventListener("click", () => {
    if (recog) { stopListening(); return; }
    setMicEnabled(true);   // bấm 🎙️ là bật lại mic sau khi từng tắt
    startListening();
  });
  $("mic-off").addEventListener("click", () => {
    stopListening();
    setMicEnabled(false);  // agent ngừng tự mở mic, chỉ trả lời bằng giọng nói
  });
}

function startListening() {
  const t = I18N[lang];
  micEnabled = true;
  localStorage.setItem("sos-mic", "on");
  recog = new SpeechRec();
  recog.lang = lang === "vi" ? "vi-VN" : "en-US";   // nghe theo ngôn ngữ đang chọn
  recog.interimResults = true;

  const hint = document.createElement("div");
  hint.className = "listening-hint";
  hint.id = "listening-hint";
  hint.textContent = t.listening;
  document.querySelector(".composer").before(hint);
  $("mic").classList.add("recording");

  recog.onresult = (e) => {
    let text = "";
    for (const r of e.results) text += r[0].transcript;
    $("input").value = text.trim();               // chỉ điền vào input, user tự bấm gửi
    armAutoSend();                                // ngừng nói 5s → tự gửi (voice mode)
  };
  recog.onend = () => {
    stopMic();   // tắt UI mic, nhưng GIỮ bộ đếm tự gửi — Chrome kết thúc phiên nghe khi user ngắt câu, nếu xoá timer ở đây thì sẽ không bao giờ tự gửi
    if (mode === "voice" && $("input").value.trim() && !autoSendTimer) armAutoSend();
  };
  recog.onerror = (e) => {
    stopMic();
    if (mode === "voice" && $("input").value.trim() && !autoSendTimer) armAutoSend();
    if (e.error !== "aborted" && e.error !== "no-speech") addError(e.error);
  };
  try { recog.start(); }
  catch (err) { stopMic(); addError(err?.message || "mic"); }
}

/* Chỉ tắt mic + UI nghe — giữ lại hẹn giờ tự gửi nếu đang có */
function stopMic() {
  if (recog) { try { recog.stop(); } catch (_) {} recog = null; }
  $("mic")?.classList.remove("recording");
  $("listening-hint")?.remove();
}

/* Huỷ toàn bộ: mic + hẹn giờ tự gửi (khi gửi tay, đổi mode, đổi ngôn ngữ…) */
function stopListening() {
  clearTimeout(autoSendTimer);
  autoSendTimer = null;
  stopMic();
}

/* ---- Modal nguồn PB-xx ---- */
function openSource(code) {
  $("source-title").textContent = code;
  $("source-note").textContent = I18N[lang].sourceNote;
  $("source-modal").classList.remove("hidden");
}

/* ---- Xoá phông trắng của ảnh nhân vật (chạy 1 lần khi mở trang) ----
   Flood-fill từ các pixel biên: chỉ xoá vùng trắng NỐI VỚI BIÊN —
   áo dài trắng bên trong không bị trong suốt. */
function prepAvatar() {
  const img = document.querySelector(".avatar-frame img");
  const apply = () => {
    try {
      const w = img.naturalWidth, h = img.naturalHeight;
      const canvas = document.createElement("canvas");
      canvas.width = w; canvas.height = h;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0);
      const im = ctx.getImageData(0, 0, w, h);
      const d = im.data;
      const bright = (i) => (d[i] + d[i + 1] + d[i + 2]) / 3;
      const visited = new Uint8Array(w * h);
      const queue = [];
      for (let x = 0; x < w; x++) { queue.push(x, x + (h - 1) * w); }
      for (let y = 0; y < h; y++) { queue.push(y * w, w - 1 + y * w); }
      const TH = 242;                       // ngưỡng "trắng" (đỡ lỗi nén JPEG)
      while (queue.length) {
        const p = queue.pop();
        if (visited[p]) continue;
        visited[p] = 1;
        const i = p * 4;
        if (bright(i) < TH) continue;       // chạm vào nhân vật → dừng nhánh
        d[i + 3] = 0;                       // nền → trong suốt
        const x = p % w, y = (p / w) | 0;
        if (x > 0) queue.push(p - 1);
        if (x < w - 1) queue.push(p + 1);
        if (y > 0) queue.push(p - w);
        if (y < h - 1) queue.push(p + w);
      }
      // làm mềm viền: pixel cạnh vùng trong suốt, sáng gần trắng → alpha theo độ trắng
      for (let p = 0; p < w * h; p++) {
        const i = p * 4;
        if (d[i + 3] === 0) continue;
        const x = p % w, y = (p / w) | 0;
        const nearTransparent = (x > 0 && d[(p - 1) * 4 + 3] === 0) || (x < w - 1 && d[(p + 1) * 4 + 3] === 0)
          || (y > 0 && d[(p - w) * 4 + 3] === 0) || (y < h - 1 && d[(p + w) * 4 + 3] === 0);
        if (!nearTransparent) continue;
        const b = bright(i);
        if (b >= 235) d[i + 3] = 0;
        else if (b >= 205) d[i + 3] = Math.round(255 * (235 - b) / 30);
      }
      ctx.putImageData(im, 0, 0);
      img.src = canvas.toDataURL("image/png");
      img.classList.add("cutout");
    } catch (_) { /* canvas bị chặn hay lỗi gì thì dùng ảnh gốc */ }
  };
  if (img.complete && img.naturalWidth) apply();
  else img.addEventListener("load", apply, { once: true });
}

function init() {
  buildLangButtons();
  prepAvatar();
  initMic();
  initModeToggle();
  $("send").addEventListener("click", send);
  $("input").addEventListener("keydown", (e) => { if (e.key === "Enter") send(); });
  $("source-close").addEventListener("click", () => $("source-modal").classList.add("hidden"));
  $("source-modal").addEventListener("click", (e) => {
    if (e.target === $("source-modal")) $("source-modal").classList.add("hidden");
  });
  if (lang) enterChat(lang);   // đã chọn ngôn ngữ từ trước → vào thẳng chat
}

init();
