import requests
import pytest

class New_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    # def test_create_new_random_joke(self):
    #     """Создание случайной шутки"""
    #
    #     url = 'https://api.chucknorris.io/jokes/random'
    #     print(url)
    #     result = requests.get(url)
    #     print("status:" + str(result.status_code))
    #     assert 200 == result.status_code
    #     if result.status_code == 200:
    #         print('ok')
    #     else:
    #         print('bad')
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #     check = result.json()
    #     check_info = check.get("categories")
    #     print(check_info)
    #     assert check_info == []
    #     print("категория верна")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("Chuck присутствует")
    #     else:
    #         print("Chuck отсутствует")

    def test_create_new_random_categories_joke(self):
        """Создание случайной шутки определенной категории"""
        category = 'sport'
        url = 'https://api.chucknorris.io/jokes/random?category='+ category
        print(url)
        result = requests.get(url)
        print("status:" + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print('ok')
        else:
            print('bad')
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        # print("категория верна")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Chuck присутствует")
        # else:
        #     print("Chuck отсутствует")


# random_joke = Test_new_joke()
# random_joke.test_create_new_random_joke()
sport_joke = New_joke()
sport_joke.test_create_new_random_categories_joke()