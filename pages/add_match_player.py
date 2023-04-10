from pages.base_page import BasePage


class Add_match_player(BasePage):
    Adding_match_player = "//*[@id='Adding match']"
    My_team_xpath = "//*[text()='My team']"
    Enemy_team_xpath="//*[text()='Enemy team']"
    My_team_score_xpath = "//*[@id='My team score']"
    Enemy_team_score_xpath="//*[text()='Enemy team score']"
    Date_xpath="//*[text()='Date'']"
    Match_at_home_xpath="//*[text()='Match at home']"
    Match_out_homr_xpath="//*[text()='Match out home']"
    Tshirt_color_xpath="//*[text()='T-shirt color']"
    League_xpath="//*[text()='Leauge']"
    Time_played_xpath="//*[text()='Time played']"
    Number_xpath="//*[text()='Number']"
    Web_match_xpath="//*[text()='Web match']"
    General_xpath="//*[text()='General']"
    Rating_xpath="//*[text()='Rating']"
    Submit_button_xpath=" //*[contains(@class, 'MuiButtonBase-root MuiButton-root')]"
    Clear_button_xpath="//*[text()='Clear']"
    pass