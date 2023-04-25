from pages.base_page import BasePage


class DevTeamContact(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    add_team_contact_url = ('https://app.slack.com/workspace-signin?redir=%2Fgantry%2Fauth%3Fapp%3Dclient%26lc%3D1680156268%26return_to%3D%252Fclient%252FT3X4CAKNU%252FC3XTEGXB6%26teams%3D')
    expectedd_title = "Find your workspace | Slack"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    log_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    dev_team_contact_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"


    def title_of_page(self):
     assert self.get_page_title(self.add_team_contact_url) == self.expectedd_title