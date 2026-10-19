import pytest
import csv
from pathlib import Path
import allure

from playwright.sync_api import Page, expect

from pages.login import LoginPage

def load_login_data():
    csv_path = (
        Path(__file__).resolve().parents[2]
        / "test_data"
        / "login_data_combined.csv"
    )

    with csv_path.open(
        mode="r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        print("CSV columns:", reader.fieldnames)
        print("CSV path:", csv_path)
        return list(reader)





# def test_valid_login(page:Page):
    
#     login_page = LoginPage(page)
#     login_page.open()

#     login_page.input_user_pass("user@premiumbank.com","Bank@123")

#     expect(page).to_have_url(login_page.login_url)
#     expect(login_page.signin).to_be_visible()

#     login_page.sign_in()

#     page.pause()
#     expect(login_page.logout_link).to_be_visible()

#     page.pause()

@pytest.mark.regression 
@pytest.mark.parametrize(
    "test_data",
    [
        pytest.param(
            data,
            marks=pytest.mark.smoke
            if data["expected_result"] == "success"
            else pytest.mark.negative,
            id=data["test_case"]
        )
        for data in load_login_data()
    ]
)

def test_login_with_csv(login_page, test_data):

    login_page.input_user_pass(
        test_data["email"],
        test_data["password"]
    )

    login_page.sign_in()

    if test_data["expected_result"]== "success":
        expect(login_page.logout_link).to_be_visible()

    else:
        expect(login_page.login_error).to_have_text(
            test_data["expected_error"]
        )

        






    # expect(login_page.login_error).to_have_text(
    #     test_data["expected_error"]
    # )


# def test_both_empty_field(page:Page):
    

#     login_page= LoginPage(page)
#     login_page.open()

#     login_page.input_user_pass("","")
#     login_page.sign_in()
#     page.pause()

#     expect(login_page.login_error).to_have_text("Email and Password are required")

    
    

# def test_email_empty(page:Page):

#     login_page= LoginPage(page)
#     login_page.open()

#     login_page.input_user_pass("","Bank@123")
#     login_page.sign_in()
#     page.pause()

#     expect(login_page.login_error).to_have_text("Email is required")




# def test_password_empty(page:Page):

#     login_page= LoginPage(page)
#     login_page.open()

#     login_page.input_user_pass("user@premiumbank.com","")
#     login_page.sign_in()
#     page.pause()

#     expect(login_page.login_error).to_have_text("Password is required")




# def test_wrong_email_pass(page:Page):

#     login_page= LoginPage(page)
#     login_page.open()

#     login_page.input_user_pass("u@premiumbank.com","Bank ")
#     login_page.sign_in()

#     page.pause()

#     expect(login_page.login_error).to_have_text("Invalid email id and password")

@pytest.mark.regression  

@allure.title("Verify Forgot Password Navigation")
@allure.severity(allure.severity_level.NORMAL)
def test_forget_password(login_page):

    with allure.step("Click Forgot Password link"):
        login_page.click_forgot_password()

    with allure.step("Verify Forgot Password page URL"):
        expect(login_page.page).to_have_url(
            login_page.forgot_password_url
        )

# def test_forget_password(login_page):
     
#      login_page.click_forgot_password()

#      expect(login_page.page).to_have_url(login_page.forgot_password_url)

#      login_page.page.pause()

@pytest.mark.regression

def test_registration_now(login_page):

     login_page.click_registration_now()

     expect(login_page.page).to_have_url(login_page.registration_link_url)

     login_page.page.pause()