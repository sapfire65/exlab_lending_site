import allure
import time
from pages.base_page import BasePage
from pages.all_locators.locators_for_test_lending_page import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LandingPage(BasePage):

    def __init__(self, browser) -> None:
        linck = 'http://test.exlab.team'
        super().__init__(browser)
        lending = BasePage(browser, linck)
        lending.open()
        browser.refresh()
        lending.scroll_too_futer(*BaseLocators.LOCATORS_FROM_SCROLL_TOO_HEADER)
        # time.sleep(0.2)
        lending.scroll_too_futer(*BaseLocators.LOCATORS_FROM_SCROLL_TOO_FUTER)

        try:
            """Проверка текущего URL после перехода по ссылке"""
            assert lending.check_link(BaseLocators.LENDING_LINK), \
                'Отличается ожидаемый вид текущей ссылки страницы'

            """Проверяем заголовок страницы (title)"""
            assert lending.check_title(BaseLocators.TITLE_NAME), \
                f'Отличается ожидаемый << title >> страницы'

            """Проверяем наличие логотипа, как обязательного атрибута бизнес модели"""
            assert lending.is_element_visibility(*BlockHeaders.DARK_LOGO_PIC_EXLAB), \
                'Не отображается логотип ExLab'

        except AssertionError as info:
            pytest.exit(f'- Стартовая ошибка: {info}')

    def check_dark_team(self):
        """* Проверяем: -по умолчанию темная тема"""
        assert self.is_element_present(*BlockHeaders.DARK_LANDING_THEME), 'Лендинг не загрузился с темной темой'

    def logo_exlab_is_displayed(self):
        """* Проверяем: -Отображение логотипа ExLab"""
        assert self.is_element_present(*BlockHeaders.DARK_LOGO_PIC_EXLAB), 'Логотип ExLab отсутствует в DOM модели ' \
                                                                           'страницы'
        assert self.is_element_visibility(*BlockHeaders.DARK_LOGO_PIC_EXLAB), 'Логотип ExLab не отображается'

    def link_about_is_displayed(self):
        """* Проверяем: -отображение ссылки << О нас >>"""
        assert self.is_element_visibility(*BlockHeaders.HEADER_LINK_ABOUT), 'Ссылка "О нас", не отображается'

    def link_about_go_to_header_about(self):
        """* Проверяем: - Ссылка ведет на экран с заголовком << О нас >>"""
        self.click(*BlockHeaders.HEADER_LINK_ABOUT)
        assert self.is_element_visibility(*BlockHeaders.LOCATION_ABOUT), 'Целевой заголовок блока "О нас", не виден'

    def link_projects_is_displayed(self):
        """* Проверяем: -Отображение ссылки  << Проекты >>"""
        assert self.is_element_visibility(*BlockHeaders.HEADER_LINK_PROJECTS), 'Ссылка "Проекты", не отображается'

    def linck_projects_go_to_header_projects(self):
        """- Ссылка ведет на экран с заголовком << Проекты >>"""
        self.click(*BlockHeaders.HEADER_LINK_PROJECTS)
        assert self.is_element_visibility(*BlockHeaders.LOCATION_PROJECTS), 'Целевой заголовок блока "Проекты", ' \
                                                                            'не виден'

    def link_mentors_is_displayed(self):
        """* Проверяем: -Отображение ссылки << Менторы >>"""
        assert self.is_element_visibility(*BlockHeaders.HEADER_LINK_MENTORS), 'Ссылка "Менторы", не отображается'

    def link_mentors_go_to_header_mentors(self):
        """* Проверяем:- Ссылка ведет на экран с заголовком << Менторы >>"""
        self.click(*BlockHeaders.HEADER_LINK_MENTORS)
        assert self.is_element_visibility(*BlockHeaders.LOCATION_MENTORS), 'Целевой заголовок блока "Менторы", не виден'

    def link_startup_is_displayed(self):
        """* Проверяем: - Отображение ссылки << StartUp >>"""
        assert self.is_element_visibility(*BlockHeaders.HEADER_LINK_STARTUP), 'Ссылка "StartUp", не отображается'

    def link_startup_go_to_header_startup(self):
        """* Проверяем:- Ссылка ведет на экран с заголовком << StartUp >>"""
        self.click(*BlockHeaders.HEADER_LINK_STARTUP)
        assert self.is_element_visibility(*BlockHeaders.LOCATION_STARTUP), 'Целевой заголовок блока "StartUp", не виден'

    def sun_icon_is_displayed(self):
        """* Проверяем: - Отображение иконки светлой темы << sun icon >>"""
        assert self.is_element_visibility(*BlockHeaders.SUN_ICON), 'Кнопка - "sun icon", не отображается'

    def sun_icon_switching(self):
        """Проверка функции переключения темы на светлую"""
        self.click(*BlockHeaders.SUN_ICON)
        assert self.is_element_present(*BlockHeaders.LIGHT_LANDING_THEME), 'Кнопка - "sun icon", не переключила на ' \
                                                                           'светлую тему'

    def join_button_is_displayed(self):
        """* Проверяем: -Отображение кнопки << Присоедениться >>"""
        assert self.is_element_visibility(*BlockHeaders.BUTTON_WILL_JOIN), 'Кнопка - "Присоедениться", не отображается'

    def clik_join_button_go_to_telegramm_bot(self):
        """* Проверяем: переход к регистрации в телеграмм бот """
        self.click(*BlockHeaders.BUTTON_WILL_JOIN)
        time.sleep(5)
        assert self.new_tab_url_contain(BlockAboutUs.LINK_JOIN_BUTTON), 'Ожидаемый адрес ссылки отличается'

    def big_logo_exlab_is_displayed(self):
        """* Проверяем: - отображение большого логотипа ExLab"""
        assert self.is_element_visibility(*BlockYourOpportunity.BIG_LOGO_EXLAB), 'Большой логотип ExLab не отображается'

    def inscription_your_opportunity(self):
        """* Проверяем: -Соответствие заголовка - << твоя возможность >> и отображение"""
        assert self.check_text_contain(*BlockYourOpportunity.INSCRIPTION_YOUR_OPPORTUNITY,
                                       BlockYourOpportunity.I_Y_O_TEXT), \
            'Текст не соответствует ожидаемому - "Твоя возможность:"'

        assert self.is_element_visibility(*BlockYourOpportunity.INSCRIPTION_YOUR_OPPORTUNITY), \
            'Текст - "Твоя возможность:" не отображается'

    def text_in_block_your_opportunity(self):
        assert self.element_contains_text(*BlockYourOpportunity.I_Y_O_TEXT_IN_BLOCK), 'Текст под заголовком "Твоя ' \
                                                                                      'возможность" - не найден'

    def head_about_us_is_displayed(self):
        """* Проверяем: -отображение заголовка << О нас >>"""
        assert self.scroll_in_too(*BlockAboutUs.HEADERS_ABOUT_US), 'Скролить до заголовка "О нас" не удалось'
        assert self.is_element_visibility(*BlockAboutUs.HEADERS_ABOUT_US), 'Заголовок "О нас" не виден'

    def block_with_text_head_about_us(self):
        """* Проверяем: -блок текста под заголовком << О нас >>"""
        # Скролим до элемента и проверяем его наличие
        assert self.scroll_in_too(*BlockAboutUs.H_A_U__TEXT), 'Скролить до текста под блоком "О нас",  не удалось'
        # Проверка видимости
        assert self.is_element_visibility(*BlockAboutUs.H_A_U__TEXT), 'Блок текста под заголовком "О нас" не виден'
        # Проверка текста в элементе.
        assert self.element_contains_text(*BlockAboutUs.H_A_U__TEXT), \
            'Под блоком "О нас", не найдено ни одного элемента'

    def title_why_exlab(self):
        """* Проверяем: -Заголовок << Почему ExLab? >>"""
        self.scroll_in_too(*BlockAboutUs.TITLE_WYY_EXLAB)
        assert self.is_element_visibility(*BlockAboutUs.TITLE_WYY_EXLAB), 'Заголовок "Почему ExLab?", не отображается'
        # Проверка текста под заголовком
        assert self.element_contains_text(*BlockAboutUs.W_E__TEXT), 'В текстовом блоке под заголовком "Почему ' \
                                                                    'ExLab?",  не найденно элементов.'

    def show_join_button_is_displayed(self):
        self.scroll_in_too(*BlockAboutUs.TITLE_WYY_EXLAB)
        assert self.is_element_visibility(*BlockAboutUs.TITLE_WYY_EXLAB), 'Кнопка присоеденится не отображается'

    def clik_join_button_go_to_telegramm_bot_2(self):
        """* Проверяем: -кнопка << Присоеденится >> открывает страницу телеграмм бота"""
        self.scroll_in_too(*BlockAboutUs.TITLE_WYY_EXLAB)
        self.click(*BlockAboutUs.SHOW_JOIN_BUTTON)
        assert self.new_tab_url_contain(BlockAboutUs.LINK_JOIN_BUTTON), \
            'Кнопка "Присоеденится" не открывает страницу бота телеграм'

    def header_project_text_is_displayed(self):
        """* Проверяем: - Отображение заголовка << Проекты >>"""
        assert self.scroll_in_too(*BlockProject.HEADER_PROJECT), 'Скролл до заголовка "Проекты" не сработал '
        assert self.is_element_visibility(*BlockProject.HEADER_PROJECT), 'Заголовок "Проекты", не отображается'

    def project_exlab_logo_is_displayed(self):
        """* Проверяем: - отображение логотипа << ExLab >> в блоке проектов"""
        assert self.scroll_in_too(*BlockProject.PROJECT_EXLAB_LOGO), 'Скролл до логотипа "ExLab" не сработал '
        assert self.is_element_visibility(*BlockProject.PROJECT_EXLAB_LOGO), \
            'Логотип "ExLab" в блоке проектов, не отображается'

    def project_healthy_life_logo_is_displayed(self):
        """* Проверяем: - отображение логотипа << Healthy life >> в блоке проектов"""
        assert self.scroll_in_too(*BlockProject.PROJECT_HEALTHY_LOGO), 'Скролл до логотипа "Healthy life" не сработал '
        assert self.is_element_visibility(*BlockProject.PROJECT_HEALTHY_LOGO), \
            'Логотип "Healthy life" в блоке проектов, не отображается'

    def project_easyhelp_logo_is_displayed(self):
        """* Проверяем: - отображение логотипа << easyhelp >> в блоке проектов"""
        assert self.scroll_in_too(*BlockProject.PROJECT_EASYHELP_LOGO), 'Скролл до логотипа "easyhelp" не сработал '
        assert self.is_element_visibility(*BlockProject.PROJECT_EASYHELP_LOGO), \
            'Логотип "easyhelp" в блоке проектов, не отображается'

    def text_all_project_is_displayed(self):
        """* Проверяем: -Блоки всех проектов на наличие текста"""
        assert self.scroll_in_too(*BlockProject.HEADER_PROJECT), \
            'Скролл до первого найденного блока не сработал'
        assert self.element_contains_text(*BlockProject.TEXT_ALL_PROJECT_2), \
            "ни одного текстового блока проектов, не найденно"

    def spoiler_mentors_open_and_closes(self):
        """* Проверяем: -При нажатии на область ментора, спойлер открывается и закрывается"""
        assert self.scroll_in_too(*BlockHeaders.LOCATION_MENTORS), \
            'Скролл до "Менторы" не сработал'
        assert self.click_opens_spoiler(*BlockMentors.MENTOR_AREA,
                                        *BlockMentors.MENTOR_AREA_SPOILER), \
            "Элементы с менторами не найдены, проверь локатор"
        assert not self.click_opens_spoiler(*BlockMentors.MENTOR_AREA,
                                            *BlockMentors.MENTOR_AREA_SPOILER), \
            "Элементы с менторами найдены, спойлер не закрыт"

    def pic_mentors_in_spoiler_is_diplayed(self):
        """* Проверяем: -Отображение портрета ментора, в спойлере"""
        assert self.scroll_in_too(*BlockHeaders.LOCATION_MENTORS), \
            'Скролл до "Менторы" не сработал'
        assert self.opens_spoiler_picture_display(*BlockMentors.MENTOR_AREA,
                                                  *BlockMentors.PIC_IN_SPOILER), "Один из портретов не отображается"

    def text_mentors_in_spoiler(self):
        """* Проверяем: -наличие текста о менторе, в спойлерах"""
        assert self.scroll_in_too(*BlockHeaders.LOCATION_MENTORS), \
            'Скролл до "Менторы" не сработал'
        assert self.opens_spoiler_text_mentors(*BlockMentors.MENTOR_AREA,
                                               *BlockMentors.TEXT_IN_SPOILER), "Нет текста о менторе"

    def text_blok_starup_jun(self):
        """* Проверяем: -наличие текста в блоке << StartUp для >> Juniors"""
        assert self.scroll_in_too(*BlockStartUp.TEXT_HEADER_JUNIORS), \
            'Скролл до "StartUp для" не сработал'
        assert self.element_contains_text(*BlockStartUp.TEXT_HEADER_JUNIORS), "Заголовок 'Juniors' не найден "
        assert self.element_contains_text(*BlockStartUp.TEXT_BLOK_ELEMENTS), \
            "Текстовый блок подзаголовка Juniors не найден"

    def text_blok_starup_reqrut(self):
        """* Проверяем: -наличие текста в блоке << StartUp для >> рекрутеров """
        assert self.scroll_in_too(*BlockStartUp.TEXT_HEADER_REKRUT), \
            'Скролл до заголовка "рекрутеров" не сработал'
        assert self.element_contains_text(*BlockStartUp.TEXT_HEADER_REKRUT), "Заголовок 'Juniors' не найден "
        assert self.element_contains_text(*BlockStartUp.TEXT_BLOK_ELEMENTS_2), \
            "Текстовый блок подзаголовка РЕКРУТЕРОВ не найден"

    def help_project_header_is_displayed(self):
        """* Проверяем: -отображение заголовка << ПОМОЧЬ ПРОЕКТУ >>"""
        assert self.scroll_in_too(*BlockHelpProject.HEADER), \
            'Скролл до "ПОМОЧЬ ПРОЕКТУ" не сработал'
        assert self.is_element_visibility(*BlockHelpProject.HEADER), 'Заголовок "ПОМОЧЬ ПРОЕКТУ" не отображается'

    def text_blok_project_header(self):
        """* Проверяем: -наличие и отображение текста в блоке << ПОМОЧЬ ПРОЕКТУ >>"""
        assert self.scroll_in_too(*BlockHelpProject.HEADER), \
            'Скролл до "ПОМОЧЬ ПРОЕКТУ" не сработал'
        assert self.element_contains_text(*BlockHelpProject.TEXT_BLOCK_ELEMENTS), \
            'ни одного текстового блока, не найденно'

    def blok_project_boosty_button_is_displayed(self):
        """* Проверяем: -отображение кнопки << BOOSTY >>"""
        assert self.scroll_in_too(*BlockHelpProject.HEADER), \
            'Скролл до "ПОМОЧЬ ПРОЕКТУ" не сработал'
        assert self.is_element_visibility(*BlockHelpProject.BUTTON_BOOSTY), 'Кнпка "Boosty" не видна'

    def blok_project_click_to_boosty(self):
        """* Проверяем: -Кнопка открывает страницу ExLab на сайте Boosty"""
        assert self.scroll_in_too(*BlockHelpProject.HEADER), \
            'Скролл до "ПОМОЧЬ ПРОЕКТУ" не сработал'
        assert self.click(*BlockHelpProject.BUTTON_BOOSTY), 'клика по кнопки BOOSTY не было'
        assert self.new_tab_url_contain(BlockHelpProject.BOOSTY_LINCK_EXLAB_PAGES,
                                        BlockHelpProject.BOOSTY_PAGE_ATRIBUT), \
            'Открытая страница BOOSTY не соответствует ожидаемой'

    def blok_project_patrion_button_is_displayed(self):
        """* Проверяем: -отображение кнопки << PATRION >>"""
        assert self.scroll_in_too(*BlockHelpProject.HEADER), \
            'Скролл до "ПОМОЧЬ ПРОЕКТУ" не сработал'
        assert self.is_element_visibility(*BlockHelpProject.BUTTON_PATREON), \
            'Кнопка "PATRION" не видна'

    def blok_project_click_to_patrion(self):
        """* Проверяем: -Кнопка открывает страницу ExLab на сайте Patrion"""
        assert self.scroll_in_too(*BlockHelpProject.HEADER), \
            'Скролл до "ПОМОЧЬ ПРОЕКТУ" не сработал'
        assert self.click(*BlockHelpProject.BUTTON_PATREON), 'клика по кнопки Patrion не было'
        time.sleep(5)
        assert self.new_tab_url_contain(BlockHelpProject.PATRION_LINCK_EXLAB_PAGES), \
            'Открытая страница Patrion не соответствует ожидаемой'

    def text_header_stay_connected_is_displayed(self):
        """* Проверяем: -отображение заголовка << Оставайся на связи >>"""
        assert self.scroll_in_too(*BlockStayConnected.HEADER_STAY_CONNECTED), \
            'Скролл до "Оставайся на связи" не сработал'
        assert self.is_element_visibility(*BlockStayConnected.HEADER_STAY_CONNECTED), \
            'Заголовок "Оставайся на связи" не отображается'

    def text_in_block_stay_connected_is_displayed(self):
        """* Проверяем: -отображение основного текста в блоке << Оставайся на связи >>"""
        assert self.scroll_in_too(*BlockStayConnected.TEXT_STAY_CONNECTED), \
            'Скролл до "блока с текстом" не сработал'
        assert self.is_element_visibility(*BlockStayConnected.TEXT_STAY_CONNECTED), \
            '- не отображается основной текст в блоке "Оставайся на связи"'

    def footer_exlab_logo_is_displayed(self):
        """* Проверяем: -отображение логотипа ExLab в футере лендинга"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LOGO_EXLAB), 'Скролл до "логотипа ExLab" не сработал'
        assert self.is_element_visibility(*BlockFooter.FOOTER_LOGO_EXLAB), 'Логотип "ExLab" не отображается'

    def footer_text_under_exlab_logo(self):
        """* Проверяем: -отображение текста << © 2022. ExLab >> под лого << ExLab >>"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LOGO_EXLAB), 'Скролл до "логотипа ExLab" не сработал'
        assert self.is_element_visibility(*BlockFooter.FOOTER_LOGO_EXLAB_TEXT), \
            '- не отображается основной текст, под лого "ExLab"'

    def footer_text_lnkdn_is_displayed(self):
        """* Проверяем: -отображение ссылки << LNKDN >> в футере лендинга"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_LNKDN), 'Скролл до "LNKDN" не сработал'
        assert self.is_element_visibility(*BlockFooter.FOOTER_LINK_LNKDN), 'Ссылка "LNKDN" не отображается'

    def footer_click_to_lnkdn(self):
        """* Проверяем: -что ссылка ведет  на страницу ExLab в LinkedIn"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_LNKDN), 'Скролл до "LNKDN" не сработал'
        self.click(*BlockFooter.FOOTER_LINK_LNKDN)
        assert self.new_tab_url_contain(BlockFooter.LINK_LNKDN), 'Открытая страница не соответствует ожидаемой'

    def footer_text_instagram_is_displayed(self):
        """* Проверяем: -отображение ссылки INSTGRM в футере лендинга"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_INSTGRM), 'Скролл до "INSTGRM" не сработал'
        assert self.is_element_visibility(*BlockFooter.FOOTER_LINK_INSTGRM), 'Ссылка "INSTGRM" не отображается'

    def footer_click_to_instagram(self):
        """* Проверяем: -что ссылка ведет  на страницу ExLab в INSTGRM"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_INSTGRM), 'Скролл до "INSTGRM" не сработал'
        self.click(*BlockFooter.FOOTER_LINK_INSTGRM)
        assert self.new_tab_url(BlockFooter.LINK_INSTGRM), \
            'Открытая страница не соответствует ожидаемой'

    def footer_text_telegram_is_displayed(self):
        """* Проверяем: -отображение ссылки TELEGRAM в футере лендинга"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_TLGRM), 'Скролл до "TELEGRAM" не сработал'
        assert self.is_element_visibility(*BlockFooter.FOOTER_LINK_TLGRM), 'Ссылка "TELEGRAM" не отображается'

    def footer_click_to_telegram(self):
        """* Проверяем: -что ссылка ведет  на страницу ExLab в TELEGRAM"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_TLGRM), 'Скролл до "TELEGRAM" не сработал'
        self.click(*BlockFooter.FOOTER_LINK_TLGRM)
        assert self.new_tab_url_contain(BlockFooter.LINK_TLGRM), 'Открытая страница не соответствует ожидаемой'

    def footer_text_ytb_is_displayed(self):
        """* Проверяем: -отображение ссылки YTB в футере лендинга"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_YTB), 'Скролл до "TELEGRAM" не сработал'
        assert self.is_element_visibility(*BlockFooter.FOOTER_LINK_YTB), 'Ссылка "YTB" не отображается'

    def footer_click_to_ytb(self):
        """* Проверяем: -что ссылка ведет  на страницу ExLab в YTB"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_YTB), 'Скролл до "YTB" не сработал'
        self.click(*BlockFooter.FOOTER_LINK_YTB)
        assert self.new_tab_url_contain(BlockFooter.LINK_YTB), 'Открытая страница не соответствует ожидаемой'

    def footer_text_mail_is_displayed(self):
        """* Проверяем: -отображение ссылки info@exlab.team  в футере лендинга"""
        assert self.scroll_in_too(*BlockFooter.FOOTER_LINK_INFO), 'Скролл до "info@exlab.team " не сработал'
        assert self.is_element_visibility(*BlockFooter.FOOTER_LINK_INFO), 'Ссылка "info@exlab.team " не отображается'
