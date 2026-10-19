
import pytest
from playwright.sync_api import Page
from pages.login import LoginPage

@pytest.fixture
def login_page(page: Page):
    login = LoginPage(page)
    login.open()
    return login
