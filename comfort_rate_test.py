import data
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Keys


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')


class SelectComfortRate:
    taxi_button = (By.XPATH, '//button[text()="Pedir un taxi"]')
    comfort_rate = (By.XPATH, '//div[@class="tcard-icon"]/img[@alt="Comfort"]')


class PhoneNumber:
    phone_numer_button = (By.CLASS_NAME, 'np-text')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, '//div[@class="buttons"]/button[text()="Siguiente"]')
    # llevan punto al inicio? es correcto el CSS_SELECTOR o lleva XPATH? es un error las palabras subrayadas
    input_code = (By.XPATH, '//div[@class="input-container error"]/input[@id="code"]')
    verify_button = (By.XPATH, '//div[@class="buttons"]/button[text()="Confirmar"]')


class PaymentMethod:
    payment_button = (By.CLASS_NAME, 'pp-button.filled')
    add_card_button = (By.CLASS_NAME, 'pp-row.disabled')
    input_card_number = (By.CLASS_NAME, 'card-number-input')
    input_card_code = (By.CLASS_NAME, 'card-code-input')
    active_add_button = (By.CLASS_NAME, 'section.active.unusual')
    add_button_card = (By.XPATH, '//div/button[text()="Agregar"]')
    select_card = (By.XPATH, "//div[@class='pp-checkbox]/label/input[@id='card-1']")  # //div/label/input[@id="card-1"]
    close_x_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]')  # no lo encontré de manera manual


class MessageToDriver:    # deja un mensaje al controlador
    button_message_driver = (By.XPATH, '//div[@class="input-container"]/input[@id="comment"]')
    message_field = (By.XPATH, '//label[@for="comment"]')  # click and entrence message

    def __init__(self, driver):
        self.driver = driver

    def click_message_field(self):
        self.driver.find_element(*self.button_message_driver).click()

    def set_message(self):
        self.driver.find_element(*self.message_field).send_keys(data.message_for_driver)

    def get_message(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def set_message_to_driver(self):
        self.set_message()
        self.click_message_field()

    def test_set_message_to_driver(self, message):
        self.driver.get(data.urban_routes_url)
        time.sleep(5)
        add_message = MessageToDriver(self.driver)
        add_message.set_message_to_driver()
        time.sleep(5)
        assert add_message.set_message == message


class OrderRequirements:

    slider_manta_pañuelos = ()
    modal_pedir_taxi = (By.CLASS_NAME, 'smart-button-main')

