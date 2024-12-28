from testpage import OperationsHelper
import logging
import time

def test_step1(browser):
    logging.info("Test 1 start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    time.sleep(5)
    assert testpage.get_error_text() == "401"

def test_step2(browser, username, password):
    logging.info("Test 2 start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(username)
    testpage.enter_pass(password)
    testpage.click_login_button()
    time.sleep(10)
    assert testpage.get_user_text() == f"Hello, {username}"

def test_step3(browser):
    logging.info("Test3 start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_new_post_btn()
    testpage.enter_title("testtitle")
    testpage.enter_content("testcontent")
    testpage.enter_description("testdesc")
    testpage.click_save_btn()
    time.sleep(10)
    assert testpage.get_res_text() == "testtitle"

def test_step4(browser):
    logging.info("Test4 start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_contact_link()
    testpage.enter_name("Crocodile")
    testpage.enter_email("crocodile@example.com")
    testpage.enter_contact_content("Hello")
    testpage.click_contact_send_btn()
    time.sleep(10)
    assert testpage.get_alert() == "Form successfully submitted" 



