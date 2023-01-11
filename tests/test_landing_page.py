import allure
import pytest
from pages.base_page import BasePage
from pages.landing_page import LandingPage
from pages.all_locators.locators_for_test_lending_page import *


# noinspection PyTypeChecker
class TestMyLandingPage:

    def test_1_header(self, browser):
        page = LandingPage(browser)
        page.check_dark_team()

    def test_2_header(self, browser):
        page = LandingPage(browser)
        page.logo_exlab_is_displayed()

    def test_3_header(self, browser):
        page = LandingPage(browser)
        page.link_about_is_displayed()

    def test_4_header(self, browser):
        page = LandingPage(browser)
        page.link_about_go_to_header_about()

    def test_5_header(self, browser):
        page = LandingPage(browser)
        page.link_projects_is_displayed()

    def test_6_header(self, browser):
        page = LandingPage(browser)
        page.linck_projects_go_to_header_projects()

    def test_7_header(self, browser):
        page = LandingPage(browser)
        page.link_mentors_is_displayed()

    def test_8_header(self, browser):
        page = LandingPage(browser)
        page.link_mentors_go_to_header_mentors()

    def test_9_header(self, browser):
        page = LandingPage(browser)
        page.link_startup_is_displayed()

    def test_10_header(self, browser):
        page = LandingPage(browser)
        page.link_startup_go_to_header_startup()

    def test_11_header(self, browser):
        page = LandingPage(browser)
        page.sun_icon_is_displayed()

    def test_12_header(self, browser):
        page = LandingPage(browser)
        page.sun_icon_switching()

    def test_13_header(self, browser):
        page = LandingPage(browser)
        page.join_button_is_displayed()

    def test_14_header(self, browser):
        page = LandingPage(browser)
        page.clik_join_button_go_to_telegramm_bot()

    def test_15_your_opportunity(self, browser):
        page = LandingPage(browser)
        page.big_logo_exlab_is_displayed()

    def test_16_your_opportunity(self, browser):
        page = LandingPage(browser)
        page.inscription_your_opportunity()

    def test_17_your_opportunity(self, browser):
        page = LandingPage(browser)
        page.text_in_block_your_opportunity()

    def test_18_about_us(self, browser):
        page = LandingPage(browser)
        page.head_about_us_is_displayed()

    def test_19_about_us(self, browser):
        page = LandingPage(browser)
        page.block_with_text_head_about_us()

    def test_20_about_us(self, browser):
        page = LandingPage(browser)
        page.title_why_exlab()

    def test_21_about_us(self, browser):
        page = LandingPage(browser)
        page.show_join_button_is_displayed()

    def test_22_about_us(self, browser):
        page = LandingPage(browser)
        page.clik_join_button_go_to_telegramm_bot_2()

    def test_23_block_projeckt(self, browser):
        page = LandingPage(browser)
        page.header_project_text_is_displayed()

    def test_24_block_projeckt(self, browser):
        page = LandingPage(browser)
        page.project_exlab_logo_is_displayed()

    def test_25_block_projeckt(self, browser):
        page = LandingPage(browser)
        page.project_healthy_life_logo_is_displayed()

    def test_26_block_projeckt(self, browser):
        page = LandingPage(browser)
        page.project_easyhelp_logo_is_displayed()

    def test_27_block_projeckt(self, browser):
        page = LandingPage(browser)
        page.text_all_project_is_displayed()

    def test_28_block_mentors(self, browser):
        page = LandingPage(browser)
        page.spoiler_mentors_open_and_closes()

    def test_29_block_mentors(self, browser):
        page = LandingPage(browser)
        page.pic_mentors_in_spoiler_is_diplayed()

    def test_30_block_mentors(self, browser):
        page = LandingPage(browser)
        page.text_mentors_in_spoiler()

    def test_31_block_startup(self, browser):
        page = LandingPage(browser)
        page.text_blok_starup_jun()

    def test_32_project_header(self, browser):
        page = LandingPage(browser)
        page.text_blok_starup_reqrut()

    def test_33_help_the_project(self, browser):
        page = LandingPage(browser)
        page.help_project_header_is_displayed()

    def test_34_help_the_project(self, browser):
        page = LandingPage(browser)
        page.text_blok_project_header()

    def test_35_help_the_project(self, browser):
        page = LandingPage(browser)
        page.blok_project_boosty_button_is_displayed()

    def test_36_help_the_project(self, browser):
        page = LandingPage(browser)
        page.blok_project_click_to_boosty()

    def test_37_help_the_project(self, browser):
        page = LandingPage(browser)
        page.blok_project_patrion_button_is_displayed()

    @pytest.mark.skip(reason='Cтраница PATRION еще не готова')
    def test_38_help_the_project(self, browser):
        page = LandingPage(browser)
        page.blok_project_click_to_patrion()

    def test_39_stay_connected(self, browser):
        page = LandingPage(browser)
        page.text_header_stay_connected_is_displayed()

    def test_40_stay_connected(self, browser):
        page = LandingPage(browser)
        page.text_in_block_stay_connected_is_displayed()

    def test_41_footer(self, browser):
        page = LandingPage(browser)
        page.footer_exlab_logo_is_displayed()

    def test_42_footer(self, browser):
        page = LandingPage(browser)
        page.footer_text_under_exlab_logo()

    def test_43_footer(self, browser):
        page = LandingPage(browser)
        page.footer_text_lnkdn_is_displayed()

    @pytest.mark.skip(
        reason=''
               'Ожидаемая ошибка, так как пользователь не авторизован. '
               'Его редиректит на страницу авторизации LinkedIn.'
               'Тестовый логин / пароль на LinkedIn пока отсутствует')
    def test_44_footer(self, browser):
        page = LandingPage(browser)
        page.footer_click_to_lnkdn()

    def test_45_footer(self, browser):
        page = LandingPage(browser)
        page.footer_text_instagram_is_displayed()

    @pytest.mark.skip(
        reason=''
               'Ожидаемая ошибка, так как пользователь не авторизован. '
               'Его перенаправляет на страницу авторизации Instagram'
               'Тестовый аккаунт на LinkedIn пока отсутствует')
    def test_46_footer(self, browser):
        page = LandingPage(browser)
        page.footer_click_to_instagram()

    def test_47_footer(self, browser):
        page = LandingPage(browser)
        page.footer_text_telegram_is_displayed()

    def test_48_footer(self, browser):
        page = LandingPage(browser)
        page.footer_click_to_telegram()

    def test_49_footer(self, browser):
        page = LandingPage(browser)
        page.footer_text_ytb_is_displayed()

    def test_50_footer(self, browser):
        page = LandingPage(browser)
        page.footer_click_to_ytb()

    def test_51_footer(self, browser):
        page = LandingPage(browser)
        page.footer_text_mail_is_displayed()
