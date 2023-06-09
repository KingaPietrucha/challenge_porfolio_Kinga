from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expectedd_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"

class MainPage(BasePage):
        expected_title = "Add player"
        add_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

        def get_page_title(self):
            assert self.get_page_title(self.add_url) -- self.expected_title
def type_in_email(self, email):
    self.field_send_keys(self.login_field_xpath, email)


def type_in_password(self, password):
    self.field_send_keys(self.password_field_xpath, password)
def click_on_the_sign_in_button(self):
    return self.click_on_the_element(self.sign_in_button_xpath)


def click_on_add_player_button(self):
    return self.click_on_the_element(self.add_player_button_xpath)


def title_of_page(self):
    assert self.get_page_title(self.login_url) == self.expectedd_title



