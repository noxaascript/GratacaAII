import requests

# Masukkan API Key baru Anda di bawah ini secara rahasia
API_KEY = "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"

def research_engine(model_type, messages):
    # Mapping Model yang lebih stabil
    models = {
        "GratacaUltraFlash 3.0WPPIDXM": "meta-llama/llama-3-8b-instruct:free",
        "GratacaUltraCoding 5.0WPPIDXM": "qwen/qwen-2.5-72b-instruct:free",
        "GratacaUltraZoom 4.0WPPIDXM": "mistralai/mistral-7b-instruct:free"
    }
    
    selected_model = models.get(model_type)
    
    payload = {
        "model": selected_model,
        "messages": messages,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        return response.json()['choices'][0]['message']['content']
    except:
        return "⚠️ Koneksi ke pusat riset terputus. Silakan coba lagi, Yang Mulia."
      
