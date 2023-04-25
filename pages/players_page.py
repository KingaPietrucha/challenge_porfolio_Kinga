from pages.base_page import BasePage


class PlayersPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    players_url = ('https://scouts-test.futbolkolektyw.pl/en/players')
    expectedd_title = "Players (3054) page 1"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    log_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    dev_team_contact_button_xpath= "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"

    def title_of_page(self):
        assert self.get_page_title(self.players_url_url) == self.expectedd_title

