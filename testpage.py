from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send `{word}` to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception whith click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=15)
        text = error_field.text
        logging.info(
            f"We found test {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}"
        )
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"],
            word,
            description="login form",
        )

    def enter_pass(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description="login form"
        )

    def enter_title(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_TITLE"], word, description="title form"
        )

    def enter_description(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_DESCRIPTION"],
            word,
            description="description form",
        )

    def enter_content(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTENT"], word, description="content form"
        )

    def enter_name(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTACT_NAME"],
            word,
            description="name form",
        )

    def enter_email(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTACT_MAIL"],
            word,
            description="email form",
        )

    def enter_contact_content(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT"],
            word,
            description="contact content form",
        )

    # GET TEXT

    def get_res_text(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_RES_LBL"], description="result"
        )

    def get_error_text(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="error label"
        )

    def get_user_text(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_HELLO"], description="username"
        )

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text

    # CLICK
    def click_login_button(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="login"
        )

    def click_new_post_btn(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description="new post"
        )

    def click_save_btn(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save post"
        )

    def click_contact_link(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="contact"
        )

    def click_contact_send_btn(self):
        self.click_button(
            TestSearchLocators.ids["LOCATOR_CONTACT_SEND"],
            description="send",
        )
