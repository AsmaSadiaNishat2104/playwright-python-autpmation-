from playwright.sync_api import Page

class LoginPage:

    login_url = "https://www.qapractice.com/practice-login-form"
    forgot_password_url="https://www.qapractice.com/forget-password"
    registration_link_url="https://www.qapractice.com/register"

    def __init__(self, page:Page):
        self.page= page

        # Locators
        self.username= page.get_by_test_id('login-email')
        self.password= page.get_by_test_id('login-password')
        self.signin= page.get_by_test_id('login-submit')
        self.login_error=page.get_by_test_id("login-error")
        self.forgot_password = page.get_by_role("link",name="Forgot password?")
        self.registration_now=page.get_by_role("link", name ="Register now")

        self.logout_link = page.locator("#login-register")
                                                                   
    def open(self):
        self.page.goto(self.login_url)

            
    def input_user_pass(self, username:str, password:str):
        self.username.fill(username)
        self.password.fill(password)

    def sign_in(self):  
        # print(self.sign_in)
        self.signin.click()

    def click_forgot_password(self):
        self.forgot_password.click()

    def click_registration_now(self):
        self.registration_now.click()

 
