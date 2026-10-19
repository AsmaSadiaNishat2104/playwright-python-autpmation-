
from playwright.sync_api import Page


class GooglePage:

    def __init__(self, page: Page):
        self.page = page

        # Locator
        self.search_box = page.get_by_role("combobox")
        

    def open(self):
        self.page.goto("https://www.google.com")

    def search_for(self, search_text: str):
        self.search_box.fill(search_text)
        self.search_box.press("Enter")