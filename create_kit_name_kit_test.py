import sender_stand_request
import data

# я не понял, зачем надо делать эту функцию, я же получаю токен при создании нового пользователя
# а затем передаю его при создании набора.
# также, при создании тестов запускается функция создания набора, то есть, сначала опять создаётся новый пользователь, который уже создаёт новый набор
# насколько я понимаю, я реализовал такую логику.

#def get_new_user_token():
#    pass


def positive_assert(kit_body):
    # задаём значение переменной, получаем результат post запроса с указанным аргументом
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201

    # Проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]
    #print(kit_body["name"])
    #print(kit_response.json()["name"])



def negative_assert_code_400(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400


#Позитивные проверки

def test_symbols_1():
    positive_assert(kit_body = data.kit_body_1)

def test_symbols_511():
    positive_assert(kit_body = data.kit_body_511)

def test_symbols_en():
    positive_assert(kit_body = data.kit_body_en)

def test_symbols_ru():
    positive_assert(kit_body = data.kit_body_ru)

def test_symbols_spec():
    positive_assert(kit_body = data.kit_body_spec)

def test_symbols_space():
    positive_assert(kit_body = data.kit_body_space)

def test_symbols_num():
    positive_assert(kit_body = data.kit_body_num)

# Негативные проверки

def test_symbols_0():
    negative_assert_code_400(kit_body = data.kit_body_0)

def test_symbols_512():
    negative_assert_code_400(kit_body = data.kit_body_512)

def test_symbols_empty():
    negative_assert_code_400(kit_body = data.kit_body_empty)

def test_symbols_int():
    negative_assert_code_400(kit_body = data.kit_body_int)