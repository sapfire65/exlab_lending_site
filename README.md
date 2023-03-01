[![N|Solid](https://github.com/sapfire65/exlab_lending_site/blob/main/files_for_readme/logo_black.png?raw=true)](https://exlab.team)
## _ _UI - tests  /  ExLab Community site_

| Files                             | readme                                      |
|-----------------------------------|---------------------------------------------|
| conftest.py                       | Фикстура с конфигурацией запуска            |
| pytest.ini                        | Убирает вывод ненужной информации в консоли |
| test_landing_page.py              | Запускаемый файл с тестами лендинга         |
| landing_page.py                   | Файл компановки проверок                    |
| base_page.py                      | Файл с базовыми методами проверок           |
| locators_for_test_lending_page.py | Файл с локаторами элементов лендинга        |

### _ _Install package for Ubuntu 22.04 :_
```shell
sudo apt install python3-pip
```
```shell
sudo apt-get install default-jre
```
```shell
wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb; sudo dpkg -i allure_2.18.1-1_all.deb
```
```sh
python3 -m pip install -r requirements.txt; pip list
```


### _ _START all TESTS_
```sh
python3 -m pytest -v -s  --tb=line --reruns 1  --browser_name=chrome --width_window=1920 --height_window=700 --headless=true --alluredir allureres  test* 
```
### _ _Генерация отчета из папки allureres_
```shell 
allure serve allureres
```
 
| ✨ default settings   conftest.py  | ✨ Supports readme (pytest)                                                |
|-----------------------------------|---------------------------------------------------------|
| --browser_name= (chrome)          | Параметр отвечающий за выбор браузера (добавить нужные) |
| --language=ru (default='en')      | Передает в URL языковые настройки                       |
| --headless=true (default='None')  | Отображение окна браузера, во время тестирования        |
| --width_window=(default='1920')   | Задаем ширину окна браузера                             |
| --height_window=(default='1080')  | Задаем высоту окна браузера                             |
| --alluredir allureres             | Сохранение результатов тестов в папке "allureres"       |


### _ _Pytest: - изменение вывода сообщений трассировки_

| ✨ Тип трасировки  | ✨ Пояснение                                                                                        |
|-------------------|-----------------------------------------------------------------------------------------------------|
| pytest --showlocals | показывать локальные переменные в сообщениях                                                      |
| pytest -l         | показывать локальные переменные в сообщениях (краткий вариант)                                      |
| pytest --tb=auto  | (по умолчанию) "расширенный" вывод для первого и последнего сообщений, и "короткий" для остальных   |
| pytest --tb=long  | исчерпывающий, подробный формат сообщений                                                           |
| pytest --tb=native | стандартный формат библиотеки Python                                                               |
| pytest --tb=no    | никаких сообщений                                                                                   |
