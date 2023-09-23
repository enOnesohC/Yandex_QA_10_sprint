import configuration
import requests
import data


# параметр user_body не используется в функции, поэтому лучше создать функцию без передаваемого параметра

# в моей реализации он использовался. Ну, или я плохо понимаю то что делаю, скорее всего.
# Ну, странно, но допустим. Мне понравилось, что я все вводимые данные использовал в data.py
#Также
#А зачем тогда в подсказках сказано "Тела POST-запросов вынеси в отдельный файл data.py."?
# вижу разночтения здесь

def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json={"firstName": "Григорий",
                               "email": "kekekeke@ke.com",
                               "phone": "+74441237887",
                               "comment": "Ребёнок спит, не шумите",
                               "address": "г. Москва, ул. Хохотушкина, д. 16"
                               },  # тут тело
                         headers={"Content-Type": "application/json",
                                  "Authorization": None
                                  })


def post_new_client_kit(name):
    response = post_new_user()
    auth_token = response.json()
    header = {"Authorization": f"Bearer {auth_token}"}

    return requests.post(configuration.URL_SERVICE +
                         configuration.CREATE_KITS_PATH,
                         json=name,
                         headers=header)

