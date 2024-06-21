


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')


class SelectComfortRate:
    taxi_button = (By.XPATH, '//button[text()="Pedir un taxi"]')
    comfort_rate = (By.XPATH, '//div[@class="tcard-icon"]/img[@alt="Comfort"]')
