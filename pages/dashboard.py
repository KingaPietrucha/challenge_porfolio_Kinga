import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    futbol_kolektyw_logo_xpath = '//*[@title="Logo Scouts Panel"]'
    add_player_button_xpath = "//*[text()='Add player']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    Scout_panel_xpath = "//*[contains(@class, 'MuiTypography-root jss16')]"
    Main_page_xpath = "//div[@class='MuiListItemText-root jss32 jss33']"
    Players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/span"
    language_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    logo_scouts_panel = "//div[@title='Logo Scouts Panel']"
    Players_count_xpath = "//*[text()='Players count']"
    Reports_count_xpath = "//*[text()='Reports count']"
    Matches_count_xpath = "//*[text()='Matches count']"
    Events_count_xpath = "//*[text()='Events count']"
    Dev_Team_button_contact_xpath = "//*[text()='Dev team contact']"
    wait = WebDriverWait (driver, 10)
    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_logo_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title




