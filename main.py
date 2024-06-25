import time
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    option_flash_button = (By.XPATH, '//div[text()="Flash"]')
    taxi_button = (By.XPATH, '//button[text()="Pedir un taxi"]')
    comfort_rate = (By.XPATH, '//div[@class="tcard-icon"]/img[@alt="Comfort"]')
    comfort_text = (By.XPATH, './/div[@class="tcard active"]//div[text()="Comfort"]')

    phone_numer_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//div[@class="buttons"]/button[text()="Siguiente"]')
    input_code = (By.ID, "code")
    verify_button = (By.XPATH, '//div[@class="buttons"]/button[text()="Confirmar"]')
    verify_phone = (By.CLASS_NAME, 'np-text')

    message_driver = (By.ID, 'comment')

    payment_button = (By.CLASS_NAME, 'pp-button.filled')
    add_card_button = (By.CLASS_NAME, 'pp-row.disabled')
    card_num_field = (By.XPATH, '//div/input[@id ="number"]')
    code_num_field = (By.XPATH, '//div[@class = "section active unusual"]//input[@id ="code"]')
    add_window = (By.CLASS_NAME, 'plc')
    active_add_button = (By.XPATH, '//div/button[text()="Agregar"]')  # //div/button[text()="Agregar"]
    select_card_button = (By.XPATH, '//div/label/input[@id="card-1"]')
    close_x_button = (By.XPATH, '//div[@class="payment-picker open"]'
                      '//div[@class="section active"]//button[@class="close-button section-close"]')

    blanket_scarves = (By.CSS_SELECTOR, '.reqs-body .r-type-switch:nth-of-type(1) .slider')

    order_icecream = (By.XPATH, ".//div[@class='r r-type-group']//div[@class='counter-plus']")
    icecream_verify_value = (By.CSS_SELECTOR, '.r-group-items .r-type-counter:nth-of-type(1) .counter-value')

    modal_order_taxi = (By.CLASS_NAME, 'smart-button')
    trip_information = (By.XPATH, '//div[contains(text(),"El conductor llegará en")]')

    def __init__(self, driver):
        self.driver = driver

        # no modificar
    def retrieve_phone_code(self, driver) -> str:
        """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
        Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
        El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

        import json
        import time
        from selenium.common import WebDriverException
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                 {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
            return code

        # Prueba 1 -------------------------- Ingresar
    def set_from(self, from_address):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

        # Prueba 2 -------------------------- Seleccionar tarifa Confort
    def check_option_flash_button_is_enabled(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.option_flash_button))
        return self.driver.find_element(*self.option_flash_button).is_enabled()
        # no hay que dar clic ya que esta por default habilitado una vez se ingresan las direcciones

    def click_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.taxi_button))
        self.driver.find_element(*self.taxi_button).click()

    def click_comfort_rate(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.comfort_rate))
        self.driver.find_element(*self.comfort_rate).click()

    def check_text_comfort_rate(self):
        return self.driver.find_element(*self.comfort_text).text

    def select_comfort_rate(self):
        self.check_option_flash_button_is_enabled()
        self.click_taxi_button()
        self.click_comfort_rate()
        self.check_text_comfort_rate()

        # Prueba 3 -------------------------- Ingresar Número de Teléfono
    def click_phone_number_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_numer_button))
        self.driver.find_element(*self.phone_numer_button).click()

    def set_phone_number(self, phone_number):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.phone_number_field))
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.verify_phone).text

    def check_next_button_is_enabled(self):
        return self.driver.find_element(*self.next_button).is_enabled()

    def click_next_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.next_button))
        self.driver.find_element(*self.next_button).click()

    def set_code(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.input_code))
        code = self.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.input_code).send_keys(code)

    def click_verify_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.verify_button))
        self.driver.find_element(*self.verify_button).click()

    def put_phone_number(self, phone_number):
        self.click_phone_number_button()
        self.set_phone_number(phone_number)
        self.check_next_button_is_enabled()
        self.click_next_button()
        self.set_code()
        self.click_verify_button()

        # Prueba 4 -------------------------- Método de pago
    def click_payment_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.payment_button))
        self.driver.find_element(*self.payment_button).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.add_card_button))
        self.driver.find_element(*self.add_card_button).click()

    def set_card_num(self, card_num):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.card_num_field))
        return self.driver.find_element(*self.card_num_field).send_keys(card_num)

    def set_code_num(self, code_num):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.code_num_field))
        return self.driver.find_element(*self.code_num_field).send_keys(code_num)

    def click_add_window(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.add_window))
        self.driver.find_element(*self.add_window).click()

    def check_active_add_button_is_enabled(self):
        return self.driver.find_element(*self.active_add_button).is_enabled()

    def click_active_add_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.active_add_button))
        self.driver.find_element(*self.active_add_button).click()

    def check_select_card_button(self):
        return self.driver.find_element(*self.select_card_button).is_enabled()

    def click_close_x_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.close_x_button))
        self.driver.find_element(*self.close_x_button).click()

    def check_text_payment_button(self):
        return self.driver.find_element(*self.payment_button).text

    def set_add_payment_method(self, card_num, code_num):
        self.click_payment_button()
        self.click_add_card_button()
        self.set_card_num(card_num)
        self.set_code_num(code_num)
        self.click_add_window()
        self.check_active_add_button_is_enabled()
        self.click_active_add_button()
        self.check_select_card_button()
        self.click_close_x_button()
        self.check_text_payment_button()

        # Prueba 5 -------------------------- Escribir un mensaje para el conductor
    def set_message(self, message):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.message_driver))
        self.driver.find_element(*self.message_driver).send_keys(message)

    def get_message(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.message_driver))
        return self.driver.find_element(*self.message_driver).get_property('value')

        # Prueba 6 ------------------------ Pedir una manta y pañuelos
    def click_blanket_scarves(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.blanket_scarves))
        self.driver.find_element(*self.blanket_scarves).click()

    def check_blanket_scarves_is_enabled(self):
        return self.driver.find_element(*self.blanket_scarves).is_enabled()

        # Prueba 7 ------------------------ Pedir 2 helados
    def click_select_icecream(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.order_icecream))
        self.driver.find_element(*self.order_icecream).click()

    def get_icecream_added_value(self):
        return self.driver.find_element(*self.icecream_verify_value).text

    def icecream_added(self):
        self.click_select_icecream()
        self.click_select_icecream()
        self.get_icecream_added_value()

        # Prueba 8 ------------------------ Aparece el modal para buscar un taxi
    def check_order_taxi_is_enabled(self):
        return self.driver.find_element(*self.modal_order_taxi).is_enabled()

    def click_modal_order_taxi(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.modal_order_taxi))
        self.driver.find_element(*self.modal_order_taxi).click()

    def check_text_order_taxi(self):
        return self.driver.find_element(*self.modal_order_taxi).text

    def select_modal_order_taxi(self):
        self.check_order_taxi_is_enabled()
        self.click_modal_order_taxi()
        self.check_text_order_taxi()

        # Prueba 9 ------------------------
    def verify_trip_information(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(self.trip_information))
        return self.driver.find_element(*self.trip_information).text
