from pages.base_page import BasePage


class Dashboard(BasePage):
    Scout_panel_xpath ="//*[contains(@class, 'MuiTypography-root jss16')]"
    Main_page_xpath ="//div[@class='MuiListItemText-root jss32 jss33']"
    Players_xpath ="//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/span"
    language_xpath ="//*[text()='Polski']"
    sign_out_xpath ="//*[text()='Sign out']"
    logo_scouts_panel= "//div[@title='Logo Scouts Panel']"
    Players_count_xpath ="//*[text()='Players count']"
    Reports_count_xpath ="//*[text()='Reports count']"
    Matches_count_xpath ="//*[text()='Matches count']"
    Events_count_xpath ="//*[text()='Events count']"
    Add_player_xpath ="//*[text()='Add player']"
    Dev_Team_button_contact_xpath ="//*[text()='Dev team contact']"

pass
