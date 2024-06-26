import data
import time
from selenium import webdriver
from selenium.webdriver import Keys
from main import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        """from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)"""

        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

        # Prueba 1
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        # Prueba 2 Seleccionar la tarifa Comfort
    def test_select_comfort_rate(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_rate()
        assert routes_page.check_text_comfort_rate() == 'Comfort'

        # Prueba 3 Rellenar el número de teléfono
    def test_entrance_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.put_phone_number(phone_number)
        assert routes_page.get_phone_number() == phone_number

        # Prueba 4 Agregar Método de pago
    def test_payment_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_numb = data.card_number
        code_numb = data.card_code
        routes_page.set_add_payment_method(card_numb, code_numb)
        assert routes_page.check_select_card_button() == True
        assert 'Tarjeta' in routes_page.check_text_payment_button()

        # Prueba 5 Escribir un mensaje para el conductor
    def test_message_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.set_message(message_for_driver)
        assert routes_page.get_message() == message_for_driver

        # Prueba 6 Pedir una manta y pañuelos
    def test_select_blanket_scarves(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_scarves()
        assert routes_page.check_blanket_scarves_is_enabled() == True

        # Prueba 7 Pedir 2 helados
    def test_order_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.icecream_added()
        assert routes_page.get_icecream_added_value() == '2'

        # Prueba 8 Aparece el modal para buscar un taxi
    def test_order_a_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_modal_order_taxi()
        assert routes_page.check_order_taxi_is_enabled() == True
        assert 'Pedir un taxi' in routes_page.check_text_order_taxi()

        # Prueba 9 Aparece el modal con detalles del viaje
    def test_verify_trip_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert 'El conductor llegará' in routes_page.verify_trip_information()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

