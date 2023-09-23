import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=data.user_body ,  # тут тело
                         headers=data.headers)


#response = post_new_user(data.user_body)
#print(response.status_code)
# print(response.json())

#auth_token = str(response.json())[14:-1]
#auth_token = response.json()
#print(auth_token)
#header =  {"Authorization": f"Bearer {auth_token}"}

def post_new_client_kit(kit_body):
    post_new_user(data.user_body)

    response = post_new_user(data.user_body)
    auth_token = response.json()
    header = {"Authorization": f"Bearer {auth_token}"}

    return requests.post(configuration.URL_SERVICE +
                         configuration.CREATE_KITS_PATH ,
                         json = kit_body,
                         headers = header)

#response1 = post_new_client_kit(data.kit_body_test)
#print(response1.status_code)
#print(response1.json())