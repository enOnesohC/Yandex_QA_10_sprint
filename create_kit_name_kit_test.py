import sender_stand_request


def get_kit_body(name):
    # задаём переменную, которая будет являться телом запроса
    # значение переменной формируется в формате json, поэтому скобки, "name": и само значение переменной
    current_name = {"name": name}
    # функция возвращает сформированную переменную
    return current_name

def positive_assert(name):

    # формируем переменную на основе введённого аргумента в тесте.
    current_name = get_kit_body(name)
    # задаём значение переменной, получаем результат post запроса с указанным аргументом
    kit_response = sender_stand_request.post_new_client_kit(current_name)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201

    # Проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == current_name["name"]


def negative_assert_code_400(name):
    current_name = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(current_name)

    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400


#Позитивные проверки

def test_symbols_1():
    positive_assert("afe")
    #   Допустимое количество символов (1)


def test_symbols_511():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    # 	Допустимое количество символов (511)

def test_symbols_en():
    positive_assert("QWErty")
    #	Английский алфавит

def test_symbols_ru():
    positive_assert("Мария")
    #	Русский алфавит

def test_symbols_spec():
    positive_assert("№%@")
    #   Спецсимволы

def test_symbols_space():
    positive_assert(" Человек и КО ")
    #   Пробелы в строке

def test_symbols_num():
    positive_assert("123")
    #   число в строке

# Негативные проверки

def test_symbols_0():
    negative_assert_code_400("")
    #   Количество символов в запросе - 0

def test_symbols_512():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    # 	Превышение количества символов (512)

def test_symbols_empty():
    negative_assert_code_400({})
    #   Пустой запрос

def test_symbols_int():
    negative_assert_code_400(123)
    #   Число(integer) в запросе
