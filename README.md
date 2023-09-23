# Yandex_QA_10_sprint
request tests
git checkout master
git branch main master -f
git checkout main
git push origin main -f

если не хочет совмещать master and main


Автотесты по 10му спринту

configuration - переменные в которых записан путь до адреса и ручек пользователя и набора

data - данные для тестов, для создания пользователя и набора

create_kit_name_kit_test - функции для проверок, тестовые функции

sender_stand_request - функции для создания нового пользователя и набора


Для запуска тестов

1. распаковать папку

2. в файле configuration.py перезадать корректный URL-адрес

3. открыть эту папку в терминале

4. выполнить pytest -v
