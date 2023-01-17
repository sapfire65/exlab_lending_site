from selenium.webdriver.common.by import By


class BaseLocators:
    LENDING_LINK = 'http://test.exlab.team/'
    TITLE_NAME = 'ExLab Landing'
    LOCATORS_FROM_SCROLL_TOO_HEADER = (By.XPATH, '//*[@class="sc-fEOsli iema-Dv"]')
    LOCATORS_FROM_SCROLL_TOO_FUTER = (By.XPATH, '//*[@class="sc-gKXOVf hXUcbs"]')


class BlockHeaders:
    LIGHT_LANDING_THEME = (By.XPATH, '//div[@class="sc-bczRLJ cxdoLY"]')
    DARK_LANDING_THEME = (By.XPATH, '//div[@class="sc-bczRLJ ckyTig"]')
    DARK_LOGO_PIC_EXLAB = (By.XPATH, '(//div[@class="sc-gKXOVf hXUcbs"]/child::*)[1]')
    LIGHT_LOGO_PIC_EXLAB = (By.XPATH, '//div[@class="sc-jqUVSM FjAfx"]')
    HEADER_LINK_ABOUT = (By.XPATH, '//a[@data-scroll-to="#about"]')
    LOCATION_ABOUT = (By.XPATH, '(//div[@class="sc-eCYdqJ koNCEH"])[1]')
    HEADER_LINK_PROJECTS = (By.XPATH, '//a[@data-scroll-to="#projects"]')
    LOCATION_PROJECTS = (By.XPATH, '//div[@data-scroll-target="#projects-title-wrapper"]')
    HEADER_LINK_MENTORS = (By.XPATH, '//a[@data-scroll-to="#mentors"]')
    LOCATION_MENTORS = (By.XPATH, '(//div[@id="mentors"]/child::*)[1]')
    HEADER_LINK_STARTUP = (By.XPATH, '//a[@data-scroll-to="#startup"]')
    LOCATION_STARTUP = (By.XPATH, '//div[@data-scroll-target="#startup-title-wrapper"]')
    SUN_ICON = (By.XPATH, '//div[@class="sc-fnykZs fEkGUM"]')
    LANGUAGE_SWITCH_BUTTON = (By.XPATH, '(//div[@class="sc-ksZaOG bxLYUZ"]')
    BUTTON_WILL_JOIN = (By.XPATH, '//div[@class="sc-hAZoDl hrEelO"]')


class BlockYourOpportunity:
    BIG_LOGO_EXLAB = (By.XPATH, '//img[@alt="gif_logo"]')
    INSCRIPTION_YOUR_OPPORTUNITY = (By.XPATH, '//div[@class="sc-dmRaPn ljhwJa"]')
    I_Y_O_TEXT = 'Твоя возможность:'
    I_Y_O_TEXT_IN_BLOCK = (By.XPATH, '//li[@class="sc-bBrHrO bXkYVd"]')


class BlockAboutUs:
    HEADERS_ABOUT_US = (By.XPATH, '(//div[@class="sc-eCYdqJ koNCEH"])[1]')
    H_A_U__TEXT = (By.XPATH, '//p[@class="sc-himrzO bgsrpw"]')
    TITLE_WYY_EXLAB = (By.XPATH, '//div[@class="sc-ciZhAO fBFmnR"]')
    W_E__TEXT = (By.XPATH, '//span[@class="sc-efBctP hnwUFZ"]')
    SHOW_JOIN_BUTTON = (By.XPATH, '//div[@class="sc-jdAMXn gLqyEH"]//a[@href="https://t.me/ExLab_registration_bot"]')
    LINK_JOIN_BUTTON = 'https://t.me/ExLab_registration_bot'
    PAGE_ATRIBUT_TG = (By.XPATH, '//img[@class="tgme_page_photo_image"]')


class BlockProject:
    HEADER_PROJECT = (By.XPATH, '//div[@data-scroll-target="#projects-title-wrapper"]')
    PROJECT_EXLAB_LOGO = (By.XPATH, '(//img[@class="sc-jOrMOR eGXkMj"])[1]')
    PROJECT_HEALTHY_LOGO = (By.XPATH, '(//img[@class="sc-jOrMOR eGXkMj"])[2]')
    PROJECT_EASYHELP_LOGO = (By.XPATH, '(//img[@class="sc-jOrMOR eGXkMj"])[3]')
    TEXT_ALL_PROJECT = (By.CLASS_NAME, 'sc-cOFTSb')
    TEXT_ALL_PROJECT_2 = (By.XPATH, '//p[@class="sc-dPyBCJ elZmsx"]')


class BlockMentors:
    MENTOR_AREA = (By.XPATH, '//div[@class="sc-ZyCDH kgnDMn"]')
    MENTOR_AREA_SPOILER = (By.XPATH, '//span[@class="sc-eKBdFk gGHWQo"]')
    PIC_IN_SPOILER = (By.XPATH, '//img[@class="sc-kIKDeO oyXhj"]')
    TEXT_IN_SPOILER = (By.XPATH, '//ul[@class="sc-dsQDmV iZMcmm"]')


class BlockStartUp:
    TEXT_UNDER_THE_STARTUP_BLOCK = (By.XPATH, '//div[@class="sc-eKszNL gOjGBb"]')
    TEXT_HEADER_JUNIORS = (By.XPATH, '//h2[@class="sc-eKszNL btnxIe"]')
    TEXT_BLOK_ELEMENTS = (By.XPATH, '//p[@class="sc-olbas ehCphU"]')
    TEXT_HEADER_REKRUT = (By.XPATH, '//h2[@class="sc-lbOyJj wSoEj"]')
    TEXT_BLOK_ELEMENTS_2 = (By.XPATH, '//p[@class="sc-gFGZVQ eMPtDU"]')


class BlockHelpProject:
    HEADER = (By.XPATH, '//div[@class="sc-jTYCaT coDMnK"]')
    TEXT_BLOCK_ELEMENTS = (By.XPATH, '//div[@class="sc-HzFiz fvqpxc"]')
    BUTTON_BOOSTY = (By.XPATH, '(//div[@class="sc-bWXABl klepWn"]/child::*)[1]')
    BUTTON_PATREON = (By.XPATH, '(//div[@class="sc-bWXABl klepWn"]/child::*)[2]')
    BOOSTY_LINCK_EXLAB_PAGES = 'https://boosty.to/exlab_startup'
    BOOSTY_PAGE_ATRIBUT = (By.XPATH, '//span[@class="Link_block_f6iQc"]/h1[text()="ExLab"]')
    PATRION_LINCK_EXLAB_PAGES = 'https://link_na_patrion.ru/'


class BlockStayConnected:
    HEADER_STAY_CONNECTED = (By.XPATH, '//div[@class="sc-bhVIhj uaVnA"]')
    TEXT_STAY_CONNECTED = (By.XPATH, '//div[@class="sc-eGAhfa cacMWv"]')


class BlockFooter:
    FOOTER_LOGO_EXLAB = (By.XPATH, '//div[@class="sc-fIavCj fEzmxG"]')
    FOOTER_LOGO_EXLAB_TEXT = (By.XPATH, '//div[@class="sc-gITdmR hYaavu"]')
    FOOTER_LINK_LNKDN = (By.XPATH, '(//li[@class="sc-dkdnUF fbGNMP"])[1]')
    LINK_LNKDN = 'https://www.linkedin.com/company/exlab-start-up/mycompany/'
    FOOTER_LINK_INSTGRM = (By.XPATH, '(//li[@class="sc-dkdnUF fbGNMP"])[2]')
    LINK_INSTGRM = 'https://www.instagram.com/exlab_startup/'
    FOOTER_LINK_TLGRM = (By.XPATH, '(//li[@class="sc-dkdnUF fbGNMP"])[3]')
    LINK_TLGRM = 'https://t.me/ExLabChannel'
    FOOTER_LINK_YTB = (By.XPATH, '(//li[@class="sc-dkdnUF fbGNMP"])[4]')
    LINK_YTB = 'https://www.youtube.com/channel/UC-TAnVYVN7qg5dgsYQJkuvA'
    FOOTER_LINK_INFO = (By.XPATH, '//a[@class="sc-ikjQzJ gjCqBu"]')
