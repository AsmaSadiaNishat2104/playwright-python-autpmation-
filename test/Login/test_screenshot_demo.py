
from playwright.sync_api import expect


def test_failure_screenshot(login_page):
    login_page.input_user_pass(
        "user@premiumbank.com",
        "Bank@123"
    )

    login_page.sign_in()

    # Deliberately incorrect assertion
    expect(login_page.page).to_have_title(
        "This Title Does Not Exist"
    )
