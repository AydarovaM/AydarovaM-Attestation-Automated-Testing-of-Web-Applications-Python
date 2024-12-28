import pytest
import requests
import yaml
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
    USERNAME = testdata["username"]
    PASSWORD = testdata["password"]
    ADDRESS = testdata["address"]


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def username():
    return USERNAME


@pytest.fixture(scope="session")
def password():
    return PASSWORD


@pytest.fixture()
def login():
    res1 = requests.post(
        ADDRESS + "gateway/login",
        data={"username": USERNAME, "password": PASSWORD},
    )
    # print("login content", res1.content.decode())
    return res1.json()["token"]


@pytest.fixture(scope="session")
def post_title():
    return f"Test Post {datetime.datetime.now()}"
