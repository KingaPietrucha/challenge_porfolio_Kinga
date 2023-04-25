from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expectedd_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    log_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    dev_team_contact_button_xpath= "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        return self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_add_player_button(self):
        return self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_log_out_button(self):
        return self.click_on_the_element(self.log_out_button_xpath)

    def click_on_dev_team_contact_button(self):
        return self.click_on_the_element(self.dev_team_contact_button_xpath)

    def click_on_the_players_button(self):
        return self.click_on_the_element(self.players_button_xpath)

    def click_on_languange_button(self):
        return self.click_on_the_element(self.language_button_xpath)

    def click_on_the_submit_button(self):
        return self.click_on_the_element(self.submit_button_xpath)




    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expectedd_title