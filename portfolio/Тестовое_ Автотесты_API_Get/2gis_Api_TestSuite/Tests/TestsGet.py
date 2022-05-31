import json
import requests
import unittest

from config import BASE_URL
# BASE_URL = "https://regions-test.2gis.com/1.0/regions"


class TestsGetRegions(unittest.TestCase):

# Запрос списка регионов
    def test_region_status_code_is_200(self):
        response = requests.get(BASE_URL)
        assert response.status_code == 200, "Cтатус код не: 200 OK"

# Запрос списка регионов: количество регионов на странице по умолчанию
    def test_region_count_on_page(self):
        response = requests.get(BASE_URL)
        items_on_page = json.loads(response.text)
        count_items = len(items_on_page['items'])
        assert count_items == 15, "Количество элементов на странице по умолчанию не равно 15"

# Проверка соответсвия количества уникальных объектов в базе и строке <total>
    def test_region_total_count(self):
        response = requests.get(BASE_URL)
        assert response.json()['total'] == 21, "Общее количество записей не равно <total>"

# Запрос списка регионов: проверка отсутсвия фильтра по коду страны
    def test_region_without_filter_country_code(self):
        response = requests.get(BASE_URL)
        for item in response.json()['items']:
            assert item['country']['name'] == "Россия", "Фильтр по коду региона отсутвует"

# Нечёткий поиск по названию региона:
    def test_name_region_status_code_is_200(self):
        response = requests.get(BASE_URL, params={'q': 'Новосибирск'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"

    def test_search_name_region_2_letters(self):
        response = requests.get(BASE_URL, params={'q': 'би'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'q' должен быть не менее 3 символов", "Ошибка: параметр должен быть не менее 3 символов"

    def test_search_name_region_3_letters(self):
        response = requests.get(BASE_URL, params={'q': 'бир'})
        assert response.json()['items'][0]['name'] == "Новосибирск", "По запросу ничего не найдено"

    def test_search_name_region_3_uppercase_letters(self):
        response = requests.get(BASE_URL, params={'q': 'БИР'})
        assert response.json()['items'][0]['name'] == "Новосибирск", "По запросу ничего не найдено"

    def test_search_name_region_4_letters(self):
        response = requests.get(BASE_URL, params={'q': 'бирс'})
        assert response.json()['items'][0]['name'] == "Новосибирск", "По запросу ничего не найдено"

    def test_search_name_region_empty(self):
        response = requests.get(BASE_URL, params={'q': ''})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'q' должен быть не менее 3 символов", "Ошибка: параметр должен быть не менее 3 символов"

    def test_search_name_region_space_left(self):
        response = requests.get(BASE_URL, params={'q': ' но'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['items'][0]['name'] == "Нижний Новгород", "По запросу ничего не найдено"

    def test_search_name_region_space_right(self):
        response = requests.get(BASE_URL, params={'q': 'ий '})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['items'][0]['name'] == "Нижний Новгород", "По запросу ничего не найдено"

    def test_search_name_region_with_space(self):
        response = requests.get(BASE_URL, params={'q': 'й н'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['items'][0]['name'] == "Нижний Новгород", "По запросу ничего не найдено"

    def test_search_name_region_with_hyphen(self):
        response = requests.get(BASE_URL, params={'q': 'к-к'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['items'][0]['name'] == "Петропавловск-Камчатский", "По запросу ничего не найдено"

    def test_search_name_region_long_name(self):
        response = requests.get(BASE_URL, params={'q': 'Крунг Тхеп Маханакхон Амон Раттанакосин Махинтараюттхая Махадилок Пхоп Ноппарат Ратчатхани Буриром Удомратчанивет Махасатан Амон Пиман Аватан Сатит Саккатхаттийя Витсанукам Прасит'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['items'][0]['name'] == "Крунг Тхеп Маханакхон Амон Раттанакосин Махинтараюттхая Махадилок Пхоп Ноппарат Ратчатхани Буриром Удомратчанивет Махасатан Амон Пиман Аватан Сатит Саккатхаттийя Витсанукам Прасит", "Не найдено"

# Поиск по названию региона с использованием фильтрации по коду страны
    def test_search_name_region_with_country_code(self):
        response = requests.get(BASE_URL, params={'country_code': 'kz', 'q': 'Омск'})
        assert response.json()['items'][0]['name'] == "Омск", "Нет региона 'Омск' с кодом страны 'kz'"

# Проверка фильтрации по коду страны
    def test_country_code_filter_status_code_is_200(self):
        response = requests.get(BASE_URL, params={'country_code': 'ru'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"

    def test_country_code_filter_ru(self):
        response = requests.get(BASE_URL, params={'country_code': 'ru'})
        for item in response.json()['items']:
            assert item['country']['name'] == "Россия", "Ошибка фильтрации по коду региона, в списке не только регионы России"

    def test_country_code_filter_cz(self):
        response = requests.get(BASE_URL, params={'country_code': 'cz'})
        for item in response.json()['items']:
            assert item['country']['name'] == "Чехия", "Ошибка фильтрации по коду региона, в списке не только регионы Чехии"

    def test_country_code_filter_kg(self):
        response = requests.get(BASE_URL, params={'country_code': 'kg'})
        for item in response.json()['items']:
            assert item['country']['name'] == "Кыргызстан", "Ошибка фильтрации по коду региона, в списке не только регионы Кыргызстана"

    def test_country_code_filter_kz(self):
        response = requests.get(BASE_URL, params={'country_code': 'kg'})
        for item in response.json()['items']:
            assert item['country']['name'] == "Казахстана", "Ошибка фильтрации по коду региона, в списке не только регионы Казахстана"

# Проверка поиска по порядковому номеру страницы
    def test_search_page_number_status_code_is_200(self):
        response = requests.get(BASE_URL, params={'page': '1'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"

    def test_search_page_number_1(self):
        response = requests.get(BASE_URL, params={'page': '1'})
        items_on_page = json.loads(response.text)
        count_items = len(items_on_page['items'])
        assert count_items >= 0, "Параметр 'page' должен быть больше 0"

    def test_search_page_number_2(self):
        response = requests.get(BASE_URL, params={'page': '2'})
        items_on_page = json.loads(response.text)
        count_items = len(items_on_page['items'])
        assert count_items >= 0, "Параметр 'page' должен быть больше 0"

    def test_search_page_number_1234(self):
        response = requests.get(BASE_URL, params={'page': '1234'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        items_on_page = json.loads(response.text)
        count_items = len(items_on_page['items'])
        assert count_items >= 0, 'Параметр "page" должен быть больше 0'

    def test_search_page_number_0(self):
        response = requests.get(BASE_URL, params={'page': '0'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page' должен быть больше 0"

    def test_search_page_number_minus_1234(self):
        response = requests.get(BASE_URL, params={'page': '-1234'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page' должен быть больше 0"

    def test_search_page_number_empty(self):
        response = requests.get(BASE_URL, params={'page': ''})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page' должен быть целым числом"

    def test_search_page_number_null(self):
        response = requests.get(BASE_URL, params={'page': 'null'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page' должен быть целым числом"

# Проверка корректности ограничения количества объектов на странице
    def test_page_size_15(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '15'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        items_on_page = json.loads(response.text)
        count_items = len(items_on_page['items'])
        assert count_items == 15, "Количество элементов на странице по умолчанию не равно 15"

    def test_page_size_10(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '10'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        items_on_page = json.loads(response.text)
        count_items = len(items_on_page['items'])
        assert count_items == 10, "Количество элементов на странице по умолчанию не равно 10"

    def test_page_size_5(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '5'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        items_on_page = json.loads(response.text)
        count_items = len(items_on_page['items'])
        assert count_items == 5, "Количество элементов на странице по умолчанию не равно 5"

# Проверка ограничения количества объектов на странице
    def test_page_size_16(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '16'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"

    def test_page_size_14(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '14'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"

    def test_page_size_11(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '11'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"

    def test_page_size_9(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '9'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"

    def test_page_size_6(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '6'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"

    def test_page_size_4(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '4'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"

    def test_page_size_minus_100(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': '-100'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"

    def test_page_size_null(self):
        response = requests.get(BASE_URL, params={'page': '1', 'page_size': 'null'})
        assert response.status_code == 200, "Cтатус код не: 200 OK"
        assert response.json()['error']['message'] == "Параметр 'page_size' должен быть целым числом"

# Получения ответа через незащищенный протокол HTTP
    def test_wrong_http(self):
        response = requests.get(url="http://regions-test.2gis.com/1.0/regions")
        assert response.status_code == 400, "Конфиденциальность информации путем шифрования не обеспечена"