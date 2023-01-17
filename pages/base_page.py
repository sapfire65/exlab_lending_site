import allure
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from .all_locators.locators_for_test_lending_page import BaseLocators
# from .test_lending_page import *
from colorama import init, Fore, Style
# from colorama import Fore, Style


class BasePage(object):
    waiting_time = 20
    """Класс базовых методов"""

    def __init__(self, browser, url=None) -> None:
        self.browser = browser
        self.url = url

    @allure.step("Метод открытия и перехода по ссылке page.open()")
    def open(self):
        self.browser.delete_all_cookies()  # Удоляем все куки
        self.browser.get(self.url)

    @allure.step("Клик по видимому обьекту страницы")
    def click(self, how, what):
        try:
            button = WebDriverWait(self.browser, self.waiting_time).until(
                EC.visibility_of_element_located((how, what)))
            button.click()
        except TimeoutException:
            return False
        return True

    @allure.step("Метод проверки достоверности перехода на нужную страницу)")
    def check_link(self, link_name):
        return self.browser.current_url == link_name

    @allure.step("Метод проверки достоверности заголовка страницы)")
    def check_title(self, title_name):
        try:
            WebDriverWait(self.browser, self.waiting_time).until(EC.title_is(title_name))
        except TimeoutException:
            return False
        return True

    @allure.step("Ожидание элемента в DOM страницы")
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.waiting_time).until(EC.presence_of_element_located((how, what)))

        except TimeoutException:
            return False
        return True

    @allure.step("Ожидание отсутствия элемента в DOM страницы")
    def is_element_not_present(self, how, what):
        try:
            WebDriverWait(self, self.waiting_time).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    @allure.step("Проверка ВИДИМОСТИ элемента на странице")
    def is_element_visibility(self, how, what):
        try:
            WebDriverWait(self.browser, self.waiting_time).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    @allure.step("Метод считает количество найденных элементов, и проверяет на наличие string + видимость")
    def element_contains_text(self, how, what):
        count = len(self.browser.find_elements(how, what))  # элементы блока
        count_text = len(self.browser.find_element(how, what).text)  # символы в строке
        if count == 0 or count_text == 0:
            return False

        print(Fore.YELLOW, f'Количество элементов: -{count}- / проверка содержимого типа - << str >>.', Style.RESET_ALL)
        for i in range(1, count + 1):
            try:
                position = self.browser.find_element(how, f'({what})[{i}]')
                self.browser.execute_script('return arguments[0].scrollIntoView();', position)

                WebDriverWait(self.browser, self.waiting_time).until(
                    EC.visibility_of_element_located((how, f'({what})[{i}]')))
            except (TimeoutException, NoSuchElementException):
                return False

            text_in = self.browser.find_element(how, f'({what})[{i}]').text

            if type(text_in) == str:
                # Проверка видимости текста
                try:
                    WebDriverWait(self.browser, self.waiting_time).until(
                        EC.visibility_of_element_located((how, f'({what})[{i}]')))
                except TimeoutException:
                    return False
                print(Fore.BLUE, f'#{i} В элементе видимый "ТЕКСТ"', Style.RESET_ALL)
                print(text_in, end='\n\n')
            else:
                print(Fore.RED, f'#{i} В элементе не "ТЕКСТ"', Style.RESET_ALL)
                return False
        return True

    @allure.step("скролинг до элемента")
    def scroll_in_too(self, how, what):
        """Метод скролинга до элемента c проверкой видимости"""
        try:
            position = self.browser.find_element(how, what)
            self.browser.execute_script("return arguments[0].scrollIntoView();", position)
            WebDriverWait(self.browser, self.waiting_time).until(
                EC.visibility_of_element_located((how, what)))

        except (NoSuchElementException, TimeoutException):
            return False
        return True

    @allure.step("Проверка открытия / закрытия спойлера")
    def click_opens_spoiler(self, how_for_clik, what_for_clik, how_for_spoiler, what_for_spoiler):
        """открываем спойлер кликом, каждого найденного элемента"""
        count_elements = len(self.browser.find_elements(how_for_clik, what_for_clik))
        if count_elements == 0:
            return False

        for i in range(1, count_elements + 1):
            position = self.browser.find_element(how_for_clik, f'({what_for_clik})[{i}]')
            # скролл до элемента и клик
            self.browser.execute_script('return arguments[0].scrollIntoView();', position)
            position.click()
            time.sleep(0.5)
        count_spoilers = len(self.browser.find_elements(how_for_spoiler, what_for_spoiler))
        if count_elements == count_spoilers:
            print(Fore.BLUE, f'Найдено {count_elements} элемента, открыты {count_spoilers} спойлера', Style.RESET_ALL)
            return True
        else:
            print(Fore.BLUE, f'Найдено {count_elements} элемента, открыты {count_spoilers} спойлера', Style.RESET_ALL)
            return False

    @allure.step("Проверка отображения портрета в каждом спойлере")
    def opens_spoiler_picture_display(self, how_for_clik, what_for_clik, how_for_pic, what_for_pic):
        count_elements = len(self.browser.find_elements(how_for_clik, what_for_clik))
        if count_elements == 0:
            print(Fore.BLUE, f'Не одного элемента не найденно, проверь локатор', Style.RESET_ALL)
            return False
        # открываем спойлер кликом, каждого найденного элемента
        for i in range(1, count_elements + 1):
            position = self.browser.find_element(how_for_clik, f'({what_for_clik})[{i}]')
            # скрол до элемента и клик
            self.browser.execute_script('return arguments[0].scrollIntoView();', position)
            position.click()
            time.sleep(0.5)
            try:
                WebDriverWait(self.browser, self.waiting_time).until(
                    EC.visibility_of_element_located((how_for_pic, f'({what_for_pic})[{i}]')))
            except TimeoutException:
                print(Fore.BLUE, f'Найдено {count_elements} объектов, {i}-й уже не видим',
                      Style.RESET_ALL)
                return False
            print(Fore.BLUE, f'Проверка видимости: {i} из {count_elements}', Style.RESET_ALL)
        return True

    @allure.step("Проверка текста о менторе, в каждом спойлере")
    def opens_spoiler_text_mentors(self, how_for_clik, what_for_clik, how_for_text, what_for_text):
        count_elements = len(self.browser.find_elements(how_for_clik, what_for_clik))
        if count_elements == 0:
            print(Fore.BLUE, f'Не одного элемента не найденно, проверь локатор', Style.RESET_ALL)
            return False
        # открываем спойлер кликом, каждого найденного элемента
        for i in range(1, count_elements + 1):
            position = self.browser.find_element(how_for_clik, f'({what_for_clik})[{i}]')
            # скрол до элемента и клик
            self.browser.execute_script('return arguments[0].scrollIntoView();', position)
            position.click()
            time.sleep(0.5)

            if not self.browser.find_element(how_for_text, f'({what_for_text})[{i}]').text:
                return False
            print(Fore.BLUE, f'{i} / {count_elements}', Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX, self.browser.find_element(how_for_text, f'({what_for_text})[{i}]').text,
                  Style.RESET_ALL, end='\n\n')
        return True

    def scroll_too_futer(self, how, what):
        count = len(self.browser.find_elements(how, what))
        for i in range(1, count + 1):
            position = self.browser.find_element(how, f'({what})[{i}]')
            time.sleep(0.5)
            self.browser.execute_script("return arguments[0].scrollIntoView();", position)
        time.sleep(1)

    @allure.step("Сравнение фактического URL с ожидаемым ")
    def new_tab_url_contain(self, link_name, page_atribut=None):

        if len(self.browser.window_handles) == 2:
            first_window = self.browser.window_handles[0]
            reg_window = self.browser.window_handles[1]
            self.browser.switch_to.window(reg_window)
            try:
                status_link = self.browser.current_url
                if page_atribut is not None:
                    WebDriverWait(self.browser, self.waiting_time).until(
                        EC.visibility_of_element_located(page_atribut))
                    print('✓ Ключевой элемент страницы отображается')
            except TimeoutException:
                return False
            print(f'✓ Ожидаемый результат: {link_name}')
            print(f'✓ Фактический результат: {status_link}')
            self.browser.execute_script('window.close()')
            time.sleep(0.1)
            self.browser.switch_to.window(first_window)
            return status_link == link_name

    @allure.step("Сравнение фактического ТЕКСТА с ожидаемым")
    def check_text_contain(self, how, what, text_str):
        return self.browser.find_element(how, what).text == text_str
