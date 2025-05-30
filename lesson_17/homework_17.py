import requests
import os

# Я задаю URL і параметри для запиту до NASA API
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'  # Можу замінити на свій власний API-ключ
}

# Створюю папку для збереження фото, якщо вона ще не існує
output_dir = 'mars_photos'
os.makedirs(output_dir, exist_ok=True)

# Надсилаю GET-запит до API з вказаними параметрами
response = requests.get(url, params=params)
data = response.json()

# Отримую перші 2 фото зі списку (якщо вони є)
photos = data.get('photos', [])[:2]

# Проходжу по кожному фото і завантажую його
for i, photo in enumerate(photos, start=1):
    img_url = photo['img_src']
    print(f'Завантаження фото {i}: {img_url}')
    img_response = requests.get(img_url)

    # Якщо запит успішний, зберігаю фото у файл
    if img_response.status_code == 200:
        file_path = os.path.join(output_dir, f'mars_photo{i}.jpg')
        with open(file_path, 'wb') as f:
            f.write(img_response.content)
        print(f'Фото {i} збережено як {file_path}')
    else:
        # Якщо сталася помилка, виводжу повідомлення
        print(f'Не вдалося завантажити фото {i}')

# Якщо фото не знайдено, виводжу відповідне повідомлення
if not photos:
    print("Фото не знайдено для вказаних параметрів.")
