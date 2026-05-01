def get_payload(history):
    return {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "system", "content": "Anda GratacaUltraFlash. Asisten ramah, sopan, dan panggil KAREEMXD 'Yang Mulia'."}] + history
    }
  
