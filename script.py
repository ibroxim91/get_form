import requests



fast_api_port = 8001
django_port = 8000

# URL API
url = f"http://localhost:{django_port}/get_form"  

# JSON данные
payload = {
    "name": "Contact Form",
    "lead_email": "email@mail.ru",
    "user_phone": "+78991234567",
    "submission_date": "15.10.2024"
}

def test_get_form():
    # Отправка POST-запроса

    response = requests.post(url, json=payload)

    # Проверка ответа
    if response.status_code == 200:
        print("Тест пройден!")
        print("Данные ответа:", response.json())
    else:
        print(f"Тест не пройден. Код ошибки: {response.status_code}")
        print("Ответ с ошибкой:", response.text)

# Запуск теста
if __name__ == "__main__":
    test_get_form()
