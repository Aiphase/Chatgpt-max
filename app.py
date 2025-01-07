from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Конфигурация API GigaChat
GIGACHAT_API_URL = "https://api.gigachat.com/v1/chat"  # Замените на актуальный URL API
API_KEY = "your_api_key_here"  # Ваш API-ключ
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.route('/process', methods=['POST'])
def process_request():
    try:
        # Получение данных от фронтенда
        data = request.json
        user_input = data.get("text", "")

        # Формируем запрос к GigaChat API
        payload = {
            "message": user_input,
            "parameters": {
                "temperature": 0.7,
                "max_length": 200
            }
        }

        # Отправляем запрос к GigaChat
        response = requests.post(GIGACHAT_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        # Возвращаем ответ от GigaChat клиенту
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
