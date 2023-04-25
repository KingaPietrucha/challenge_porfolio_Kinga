from pages.base_page import BasePage


class FillAddPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expectedd_title = "Scouts panel - sign in"
    title_of_box_xpath = "//*[@id='__next']/form/div/div[1]/h5"
    header_of_box = "Scouts Panel"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    emaill_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    name_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_xpath ="//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    phone_xpath ="//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    weight_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    height_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input"
    age_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    club_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    level_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    main_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    achievements_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[14]/div/div/input"
    district_xpath = "//*[@id='mui-component-select-district']"
    district_city_xpath = "//*[@id='mui-component-select-district']"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)


    def type_in_name(self, Name):
        self.field_send_keys(self.name_xpath, Name)

    def type_in_surname(self, Surname):
        self.field_send_keys(self.surname_xpath, Surname)

    def type_in_phone(self, Phone):
        self.field_send_keys(self.phone_xpath, Phone)

    def type_in_weight(self, Weight):
        self.field_send_keys(self.weight_xpath, Weight)

    def type_in_height(self, Height):
        self.field_send_keys(self.height_xpath, Height)

    def type_in_age(self, Age):
        self.field_send_keys(self.age_xpath, Age)

    def type_in_club(self, Club):
        self.field_send_keys(self.club_xpath, Club)

    def type_in_level(self, Level):
        self.field_send_keys(self.level_xpath, Level)

    def type_in_main_position(self, Main):
        self.field_send_keys(self.main_position_xpath, Main)

    def type_in_achievements(self, Achievements):
        self.field_send_keys(self.achievements_xpath, Achievements)

    def type_in_district(self, District):
        self.field_send_keys(self.district_xpath, District)

    def type_in_destrict_city(self, Lodz):
        self.field_send_keys(self.district_city_xpath, Lodz)

    def click_on_the_submit_button(self):
        return self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expectedd_title



