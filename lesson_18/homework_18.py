import requests

# 1. POST — Завантаження зображення
with open('image.jpg', 'rb') as img:
    files = {'image': img}
    post_response = requests.post('http://127.0.0.1:8080/upload', files=files)
    print(post_response.json())

filename = 'image.jpg'  # Назва файлу, що завантажувалась

# 2. GET — Отримання URL
headers = {'Content-Type': 'text'}
get_response = requests.get(f'http://127.0.0.1:8080/image/{filename}', headers=headers)
print(get_response.json())

# 3. DELETE — Видалення
delete_response = requests.delete(f'http://127.0.0.1:8080/delete/{filename}')
print(delete_response.json())
