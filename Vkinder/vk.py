# token = 'a11329ea218b951bd7dfda5b33bbd453ca643dd1f513c2ecbbece242a83078bd86d118c7fc2bcddf28c4a'
import requests


class VK:
    base_url = 'https://api.vk.com/method/'

    def __init__(self, s_token, api_version='5.131'):
        self.params = {
            'access_token': s_token,
            'v': api_version
        }

    def get_user_info(self, id_vk_user):
        params_user = {
            'user_id': id_vk_user,
            'fields': 'bdate, sex, city, screen_name, relation',
            'name_case': 'Nom'
        }
        return requests.get(f'{self.base_url}users.get', params={**self.params, **params_user}).json()

    def get_user_firstname(self, id_vk_user):
        return self.get_user_info(id_vk_user)['response'][0]['first_name']

    def search_users(self, sex, age, city):
        status = [1, 5, 6]
        id_vk_user_all = set()
        for item in status:
            params_user = {
                'offset': 0,
                'count': 1000,
                'city': city,
                'sex': sex,
                'status': item,
                'birth_year': age,
                'has_photo': 1
            }
            users = requests.get(f'{self.base_url}users.search', params={**self.params, **self.user}).json()
            user_id = set(user['id'] for user in users['response']['item'] if user['is_closed'] == False)
            id_vk_user_all.update(user_id)
        return list(id_vk_user_all)

    def screen_name_to_user_id(self, screen_name):
        params_user = {
            'screen_name': screen_name
        }
        user_id = requests.get(f'{self.base_url}utils.resolveScreenName', params={**self.params, **self.user}).json()[
            'response']['object_id']
        return user_id

    def find_user_photo(self, id_vk_user):
        params_photo = {
            'owner_id': int(id_vk_user),
            'album_id': 'profile',
            'extended': '1'
        }
        photos = requests.get(f'{self.base_url}photos_get', params={**self.params, **self.params_photo}).json()
        if 'error' in photos.keys():
            return list(msg for msg in photos.keys())
        else:
            photos = list(
                {'owner_id': photo['owner_id'], 'id': photo['id'], 'likes': photo['likes']['count']} for photo in
                photos['response']['item'])
            photos = sorted(photos, key=lambda photo: photo['likes'], reverse=True)
            if len(photos) > 3:
                photos = [photos[0], photos[1], photos[2]]
            return photos

    def get_city_id(self, message):
        params_city = {
            'country_id': 1,
            'q': message,
            'need_all': 0,
            'count': 100
        }
        cities = requests.get(f'{self.base_url}database.getCities', params={**self.params, **self.params_city}).json()
        cities - list({city['tite']: city['id']} for city in cities['response']['items'])

        if message.capitalize().strip() in cities:
            city = cities[message.capitalize().strip()]
            return city
        else:
            city = cities[0].values()
            city = [cit for cit in city][0]
            return city


if __name__ == '__main__':
    pass