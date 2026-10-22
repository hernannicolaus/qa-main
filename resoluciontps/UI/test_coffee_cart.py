import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color

URL = 'https://coffee-cart.app/'
BRAVE = '/usr/bin/brave-browser'


class PaginaMenu:

    DIV_TAZAS = (By.CLASS_NAME, 'cup-body')
    BUTTON_TOTAL = (By.CSS_SELECTOR, '[data-test="checkout"]')

    def __init__(self, driver):
        self.driver = driver

    def get_tazas(self):
        return self.driver.find_elements(*self.DIV_TAZAS)

    def get_taza(self, nombre):
        return self.driver.find_element(By.CSS_SELECTOR, f'[data-test="{nombre}"]')
    
    def agregar_cafe(self, nombre):
            self.get_taza(nombre).click()

    def get_button_total(self):
        return self.driver.find_element(*self.BUTTON_TOTAL)

    def cantidad_cafes(self):
        return len(self.get_tazas())

    def texto_total(self):
        return self.get_button_total().text

    def color_total(self):
        return Color.from_string(self.get_button_total().value_of_css_property('background-color'))

# Abrir y cerrar brave
@pytest.fixture(scope='module')
def driver():
    opciones = webdriver.ChromeOptions()
    opciones.binary_location = BRAVE
    opciones.add_argument('--headless=new')
    driver = webdriver.Chrome(options=opciones)
    yield driver
    driver.quit()

# Borrar carrito guardado y recargar menu
@pytest.fixture(autouse=True)
def limpiar_pagina(driver):
    driver.get(URL)
    driver.delete_all_cookies()
    driver.execute_script('window.localStorage.clear(); window.sessionStorage.clear();')
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(PaginaMenu.DIV_TAZAS))


# Crea la pagina del menu para usarla en los tests
@pytest.fixture
def pagina_menu(driver):
    return PaginaMenu(driver)


class TestCarritoCafe:
    def test_menu_muestra_9_cafes(self, pagina_menu):
        assert pagina_menu.cantidad_cafes() == 9

    def test_agregar_cafes_actualiza_total(self, pagina_menu):
        pagina_menu.agregar_cafe('Espresso')
        pagina_menu.agregar_cafe('Cappuccino')
        assert pagina_menu.texto_total() == 'Total: $29.00'

    def test_color_button_total(self, pagina_menu):
        assert pagina_menu.color_total() == Color.from_string('antiquewhite')
