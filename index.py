# Create a standalone full index.html file with all features integrated & fixed (using gemini-2.5-flash)

html_content = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Food Nutrition Tracker</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Sarabun', sans-serif;
    }
  </style>
</head>
<body class="bg-slate-100 min-h-screen p-4 sm:p-6 text-slate-800">
  <div class="max-w-md mx-auto space-y-5">
    
    <!-- Header Card -->
    <div class="bg-gradient-to-r from-blue-600 to-indigo-600 rounded-2xl p-5 text-white shadow-lg">
      <div class="flex items-center space-x-3">
        <div class="p-2 bg-white/10 rounded-xl backdrop-blur-sm">
          <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/>
          </svg>
        </div>
        <div>
          <h1 class="text-xl font-bold">AI Food Tracker</h1>
          <p class="text-xs text-blue-100">ถ่ายรูปสแกนโภชนาการอาหารด้วย AI</p>
        </div>
      </div>
    </div>

    <!-- Main Scanner Form Card -->
    <div class="bg-white rounded-2xl shadow-sm border border-slate-200/80 p-5 space-y-4">
      
      <!-- API Key Input -->
      <div>
        <div class="flex justify-between items-center mb-1">
          <label class="block text-xs font-semibold text-slate-600">Gemini API Key</label>
          <a href="https://aistudio.google.com/" target="_blank" class="text-[11px] text-blue-600 hover:underline">รับ Key ฟรีชั่วคราว</a>
        </div>
        <input type="password" id="apiKey" class="w-full border border-slate-300 rounded-xl p-2.5 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition" placeholder="วาง API Key ที่นี่...">
      </div>

      <!-- Image Input & Preview -->
      <div>
        <label class="block text-xs font-semibold text-slate-600 mb-1">ถ่ายรูป หรือ เลือกรูปอาหาร</label>
        <label class="flex flex-col items-center justify-center w-full h-36 border-2 border-dashed border-slate-300 rounded-xl cursor-pointer bg-slate-50 hover:bg-slate-100 transition relative overflow-hidden">
          <div id="uploadPlaceholder" class="flex flex-col items-center justify-center pt-5 pb-6">
            <svg class="w-8 h-8 mb-2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            <p class="text-xs text-slate-500 font-medium">แตะเพื่อถ่ายภาพหรือเลือกไฟล์</p>
          </div>
          <img id="imagePreview" class="hidden absolute inset-0 w-full h-full object-cover">
          <input type="file" id="imageInput" accept="image/*" capture="environment" class="hidden" onchange="previewSelectedImage(event)">
        </label>
      </div>

      <button onclick="analyzeFood()" id="btnSubmit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition duration-150 shadow-md shadow-blue-500/20 text-sm flex justify-center items-center space-x-2">
        <span>วิเคราะห์รูปภาพอาหาร</span>
      </button>

      <!-- Results Form (Editable) -->
      <div id="resultSection" class="hidden border-t border-slate-200 pt-4 space-y-4">
        <div class="flex items-center justify-between">
          <h2 class="font-bold text-sm text-slate-700 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500 inline-block"></span>
            ผลการวิเคราะห์ (แก้ไขก่อนบันทึกได้)
          </h2>
        </div>
        
        <div>
          <label class="text-xs text-slate-500 font-medium">ชื่ออาหาร</label>
          <input type="text" id="foodName" class="w-full border border-slate-300 rounded-lg p-2 text-sm font-semibold focus:ring-2 focus:ring-blue-500 outline-none">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="text-xs text-slate-500 font-medium">น้ำหนักประมาณ (กรัม)</label>
            <input type="number" id="weight" class="w-full border border-slate-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
          </div>
          <div>
            <label class="text-xs text-slate-500 font-medium">แคลอรีรวม (kcal)</label>
            <input type="number" id="calories" class="w-full border border-slate-300 rounded-lg p-2 text-sm font-bold text-amber-600 focus:ring-2 focus:ring-blue-500 outline-none">
          </div>
        </div>

        <div class="grid grid-cols-3 gap-2">
          <div>
            <label class="text-xs text-slate-500 font-medium">โปรตีน (g)</label>
            <input type="number" id="protein" class="w-full border border-slate-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
          </div>
          <div>
            <label class="text-xs text-slate-500 font-medium">คาร์บ (g)</label>
            <input type="number" id="carbs" class="w-full border border-slate-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
          </div>
          <div>
            <label class="text-xs text-slate-500 font-medium">ไขมัน (g)</label>
            <input type="number" id="fat" class="w-full border border-slate-300 rounded-lg p-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
          </div>
        </div>

        <button onclick="saveMeal()" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-semibold py-2.5 rounded-xl transition shadow-md shadow-emerald-600/20 text-sm">
          + บันทึกรายการลงในประวัติประจำวัน
        </button>
      </div>
    </div>

    <!-- Daily Summary & History Card -->
    <div class="bg-white rounded-2xl shadow-sm border border-slate-200/80 p-5 space-y-4">
      <div class="flex justify-between items-center border-b border-slate-100 pb-3">
        <h2 class="font-bold text-base text-slate-800">สรุปโภชนาการวันนี้</h2>
        <span id="currentDate" class="text-xs text-slate-400 font-medium"></span>
      </div>

      <!-- Stats Display -->
      <div class="bg-gradient-to-br from-slate-900 to-slate-800 text-white rounded-xl p-4 text-center shadow">
        <p class="text-xs text-slate-400 font-medium uppercase tracking-wider">แคลอรีสะสมรวมวันนี้</p>
        <p class="text-3xl font-extrabold text-amber-400 mt-1"><span id="totalCalories">0</span> <span class="text-sm font-normal text-slate-300">kcal</span></p>
      </div>

      <div class="grid grid-cols-3 gap-2 text-center text-xs">
        <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
          <p class="text-slate-400">โปรตีนรวม</p>
          <p class="font-bold text-slate-700 mt-0.5"><span id="totalProtein" class="text-sm">0</span> g</p>
        </div>
        <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
          <p class="text-slate-400">คาร์บรวม</p>
          <p class="font-bold text-slate-700 mt-0.5"><span id="totalCarbs" class="text-sm">0</span> g</p>
        </div>
        <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-100">
          <p class="text-slate-400">ไขมันรวม</p>
          <p class="font-bold text-slate-700 mt-0.5"><span id="totalFat" class="text-sm">0</span> g</p>
        </div>
      </div>

      <!-- Meal History List -->
      <div class="space-y-2 pt-2">
        <h3 class="font-bold text-xs text-slate-500 uppercase tracking-wider">รายการอาหารประจำวัน</h3>
        <div id="historyList" class="space-y-2 max-h-64 overflow-y-auto pr-1">
          <!-- Meal items populated dynamically -->
        </div>
      </div>
    </div>

  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // โหลด API Key ที่บันทึกไว้ (ถ้ามี)
      const savedKey = localStorage.getItem('gemini_api_key');
      if (savedKey) document.getElementById('apiKey').value = savedKey;
      
      const today = new Date().toISOString().split('T')[0];
      document.getElementById('currentDate').innerText = today;
      
      renderHistory();
    });

    function previewSelectedImage(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          const preview = document.getElementById('imagePreview');
          preview.src = e.target.result;
          preview.classList.remove('hidden');
          document.getElementById('uploadPlaceholder').classList.add('hidden');
        }
        reader.readAsDataURL(file);
      }
    }

    async function analyzeFood() {
      const apiKey = document.getElementById('apiKey').value.trim();
      const fileInput = document.getElementById('imageInput');
      const btn = document.getElementById('btnSubmit');

      if (!apiKey) return alert('กรุณาใส่ Gemini API Key ก่อนใช้งาน');
      if (!fileInput.files[0]) return alert('กรุณาถ่ายรูปหรือเลือกไฟล์ภาพอาหาร');

      // บันทึก Key ลงใน LocalStorage เพื่อความสะดวกครั้งต่อไป
      localStorage.setItem('gemini_api_key', apiKey);

      btn.innerText = '⏳ กำลังวิเคราะห์รูปภาพด้วย AI...';
      btn.disabled = true;

      try {
        const file = fileInput.files[0];
        const base64Image = await convertToBase64(file);
        const pureBase64 = base64Image.split(',')[1];

        const prompt = `วิเคราะห์ภาพอาหารนี้ แล้วตอบกลับเป็น JSON ภาษาไทยเท่านั้น ห้ามใส่อักขระอื่นนอกเหนือจากโครงสร้าง JSON นี้:
        {
          "foodName": "ชื่ออาหาร",
          "weight": น้ำหนักเป็นกรัม (ตัวเลข),
          "calories": แคลอรีรวม (ตัวเลข),
          "protein": โปรตีนเป็นกรัม (ตัวเลข),
          "carbs": คาร์โบไฮเดรตเป็นกรัม (ตัวเลข),
          "fat": ไขมันเป็นกรัม (ตัวเลข)
        }`;

        // ใช้โมเดล gemini-2.5-flash เวอร์ชันปัจจุบัน
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{
              parts: [
                { text: prompt },
                { inline_data: { mime_type: file.type, data: pureBase64 } }
              ]
            }],
            generationConfig: { response_mime_type: "application/json" }
          })
        });

        const data = await response.json();

        // ดักจับ Error จาก API
        if (data.error) {
          throw new Error(`[API Error ${data.error.code}]: ${data.error.message}`);
        }

        if (!data.candidates || data.candidates.length === 0) {
          throw new Error('ไม่พบผลลัพธ์จาก AI (อาจติดตัวกรองความปลอดภัย)');
        }

        const resultText = data.candidates[0].content.parts[0].text;
        const foodData = JSON.parse(resultText);

        // แสดงผลลัพธ์ใส่ฟอร์มที่ให้ผู้ใช้แก้ไขได้
        document.getElementById('foodName').value = foodData.foodName || '';
        document.getElementById('weight').value = foodData.weight || 0;
        document.getElementById('calories').value = foodData.calories || 0;
        document.getElementById('protein').value = foodData.protein || 0;
        document.getElementById('carbs').value = foodData.carbs || 0;
        document.getElementById('fat').value = foodData.fat || 0;

        document.getElementById('resultSection').classList.remove('hidden');
        document.getElementById('resultSection').scrollIntoView({ behavior: 'smooth' });
      } catch (err) {
        alert('เกิดข้อผิดพลาดในการวิเคราะห์: ' + err.message);
        console.error('API Error:', err);
      } finally {
        btn.innerText = 'วิเคราะห์รูปภาพอาหาร';
        btn.disabled = false;
      }
    }

    function saveMeal() {
      const meal = {
        id: Date.now(),
        date: new Date().toISOString().split('T')[0],
        time: new Date().toLocaleTimeString('th-TH', { hour: '2-digit', minute: '2-digit' }),
        foodName: document.getElementById('foodName').value || 'ไม่ระบุชื่อ',
        weight: Number(document.getElementById('weight').value) || 0,
        calories: Number(document.getElementById('calories').value) || 0,
        protein: Number(document.getElementById('protein').value) || 0,
        carbs: Number(document.getElementById('carbs').value) || 0,
        fat: Number(document.getElementById('fat').value) || 0
      };

      const history = JSON.parse(localStorage.getItem('food_history') || '[]');
      history.push(meal);
      localStorage.setItem('food_history', JSON.stringify(history));

      // ล้างค่าฟอร์มสแกน
      document.getElementById('resultSection').classList.add('hidden');
      document.getElementById('imageInput').value = '';
      document.getElementById('imagePreview').classList.add('hidden');
      document.getElementById('uploadPlaceholder').classList.remove('hidden');

      renderHistory();
    }

    function deleteMeal(id) {
      if (!confirm('ต้องการลบรายการนี้ใช่หรือไม่?')) return;
      let history = JSON.parse(localStorage.getItem('food_history') || '[]');
      history = history.filter(item => item.id !== id);
      localStorage.setItem('food_history', JSON.stringify(history));
      renderHistory();
    }

    function renderHistory() {
      const today = new Date().toISOString().split('T')[0];
      const history = JSON.parse(localStorage.getItem('food_history') || '[]');
      const todayMeals = history.filter(item => item.date === today);

      const historyList = document.getElementById('historyList');
      historyList.innerHTML = '';

      let totalCal = 0, totalP = 0, totalC = 0, totalF = 0;

      if (todayMeals.length === 0) {
        historyList.innerHTML = '<p class="text-xs text-center text-slate-400 py-6">ยังไม่มีรายการอาหารวันนี้</p>';
      } else {
        todayMeals.forEach(meal => {
          totalCal += meal.calories;
          totalP += meal.protein;
          totalC += meal.carbs;
          totalF += meal.fat;

          const card = document.createElement('div');
          card.className = 'flex justify-between items-center bg-slate-50 hover:bg-slate-100/80 p-3 rounded-xl border border-slate-200/60 transition text-xs';
          card.innerHTML = `
            <div>
              <p class="font-bold text-slate-800">${meal.foodName} <span class="font-normal text-slate-400">(${meal.weight}g)</span></p>
              <p class="text-slate-500 mt-0.5">${meal.time} • P:${meal.protein}g C:${meal.carbs}g F:${meal.fat}g</p>
            </div>
            <div class="flex items-center space-x-3">
              <span class="font-bold text-amber-600 bg-amber-50 px-2 py-1 rounded-md border border-amber-200/50">${meal.calories} kcal</span>
              <button onclick="deleteMeal(${meal.id})" class="text-slate-400 hover:text-red-500 font-bold p-1 transition">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
              </button>
            </div>
          `;
          historyList.appendChild(card);
        });
      }

      // สรุปผลยอดรวม
      document.getElementById('totalCalories').innerText = totalCal.toLocaleString();
      document.getElementById('totalProtein').innerText = totalP;
      document.getElementById('totalCarbs').innerText = totalC;
      document.getElementById('totalFat').innerText = totalF;
    }

    function convertToBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
      });
    }
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated index.html successfully.")