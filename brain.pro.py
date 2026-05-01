def get_payload(history):
    return {
        "model": "qwen/qwen-2.5-72b-instruct:free",
        "messages": [{"role": "system", "content": "Anda GratacaUltraCoding. Pakar IT yang sangat cerdas dan ramah kepada KAREEMXD."}] + history
    }
  
