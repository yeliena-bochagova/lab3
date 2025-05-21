def test_example():
    assert 1 + 1 == 2

from django.test import TestCase
from django.urls import reverse

class PostPageTests(TestCase):  # Створюємо клас для тестів сторінки поста, наслідуємо від TestCase
    def test_post_page_status_code(self):  # Назва тесту: перевірка статус-коду сторінки поста
        response = self.client.get(reverse('post'))  # reverse('post') повертає URL за ім'ям маршруту 'post'; self.client.get() виконує GET-запит
        self.assertEqual(response.status_code, 200)  # Перевіряємо, що сервер повернув статус 200 (успішно)
