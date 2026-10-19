from playwright.sync_api import Page, expect
import re

from pages.google_page import GooglePage

def test_google_page_title(page: Page):
    google_page = GooglePage(page)

    google_page.open()

    expect(page).to_have_title("Google")


def test_google_search_url(page: Page):
    google_page = GooglePage(page)

    google_page.open()

    google_page.search_for("Playwright documentation")

    expect(page).to_have_url(
        re.compile(r".*google\.com/search.*")
    )



    