class LoginPage():

    USERNAME_INPUT = "un"
    PASSWORD_INPUT = "pw"
    SINGIN_BTN = "btn primary"
    POST_HERE = "gwt-uid-9"
    ACTION_BTN = "SiteMenuTab_TEMPO_SITE---nav_label"
    EXHIBICION_LINK = "aui-ActionLink GPGIXADDAP"
    NOMBRE_EXHIBICION = "de8a7a6c750895ffa0554040ea436941"
    TEMA_EXHIBICION = "147b7d8997ae86d5138581b25ac8c77f"

    def __init__(self, driver):
        self.driver = driver

    def login_in_app(self, username, password):
        username_input = self.driver.find_element_by_id(self.USERNAME_INPUT)
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_id(self.PASSWORD_INPUT)
        password_input.send_keys(password)

        singin_btn = self.driver.find_element_by_class(self.SINGIN_BTN)
        singin_btn.click()

    def is_singin_succesfull(self):
        post_here = self.driver.find_element_by_id(self.POST_HERE).is_displayed()
        return post_here

    def action(self):
        action_btn = self.driver.find_element_by_class(self.ACTION_BTN)
        action_btn.click()

        exhibicion_link = self.driver.find_element_by_class(self.EXHIBICION_LINK)
        exhibicion_link.click()

    def fill_the_fields(self, nombre_exhibicion, tema_exhibicion):

        nombre_exhibicon_input = self.driver.find_element_by_id(self.NOMBRE_EXHIBICION)
        nombre_exhibicon_input.send_keys(nombre_exhibicion)

        tema_exhibicion_input = self.driver.find_element_by_id(self.TEMA_EXHIBICION)
        tema_exhibicion_input.send_keys(tema_exhibicion)




