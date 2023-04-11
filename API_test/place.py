import requests


class TestnewLocation():
    '''Работа с новой локацией'''

    def test_create_new_location(self):
        '''Создание новой локации'''

        base_url = 'https://rahulshettyacademy.com'  # базовый url
        key = "?key=qaclick123"  # параметр для запросов
        post_resource = '/maps/api/place/add/json'  # ресурс метода Post

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_new_location = {

        }

        result_post = requests.post(post_url)


new_place = TestnewLocation()
new_place.test_create_new_location()
