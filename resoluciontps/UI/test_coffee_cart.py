import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------- RESOLUCIÓN -------
URL = "https://coffee-cart.app/"
SNAP_FIREFOX = "/snap/firefox/current/usr/lib/firefox/firefox"


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    if os.environ.get("HEADLESS"):
        options.add_argument("-headless")
    if os.path.exists(SNAP_FIREFOX):  # Firefox instalado como snap
        options.binary_location = SNAP_FIREFOX
        driver = webdriver.Firefox(options=options, service=Service("/snap/bin/geckodriver"))
    else:
        driver = webdriver.Firefox(options=options)
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cup-body")))
    yield driver
    driver.quit()


def agregar_cafe(driver, nombre):
    driver.find_element(By.CSS_SELECTOR, f'[data-test="{nombre}"]').click()


def texto_carrito(driver):
    return driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Cart page"]').text


def texto_total(driver):
    return driver.find_element(By.CSS_SELECTOR, '[data-test="checkout"]').text


def ir_al_carrito(driver):
    driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Cart page"]').click()
    WebDriverWait(driver, 10).until(EC.url_contains("/cart"))


# ------- TESTS -------

def test_menu_muestra_9_cafes_y_carrito_vacio(driver):
    assert len(driver.find_elements(By.CLASS_NAME, "cup-body")) == 9
    assert texto_carrito(driver) == "cart (0)"
    assert texto_total(driver) == "Total: $0.00"

def test_agregar_cafes_actualiza_contador_y_total(driver):
    agregar_cafe(driver, "Espresso")
    agregar_cafe(driver, "Cappuccino")
    assert texto_carrito(driver) == "cart (2)"
    assert texto_total(driver) == "Total: $29.00"

def test_carrito_lista_producto_agregado(driver):
    agregar_cafe(driver, "Mocha")
    ir_al_carrito(driver)
    assert "Mocha" in driver.find_element(By.CLASS_NAME, "list").text

def test_sumar_unidad_desde_carrito(driver):
    agregar_cafe(driver, "Americano")
    ir_al_carrito(driver)
    driver.find_element(By.CSS_SELECTOR, '.list > div > ul button[aria-label="Add one Americano"]').click()
    assert texto_carrito(driver) == "cart (2)"
    assert texto_total(driver) == "Total: $14.00"

def test_eliminar_producto_vacia_carrito(driver):
    agregar_cafe(driver, "Espresso")
    ir_al_carrito(driver)
    driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Remove all Espresso"]').click()
    assert texto_carrito(driver) == "cart (0)"
    assert "No coffee, go add some." in driver.find_element(By.CLASS_NAME, "list").text

def test_checkout_muestra_mensaje_de_compra(driver):
    agregar_cafe(driver, "Cafe_Latte")
    driver.find_element(By.CSS_SELECTOR, '[data-test="checkout"]').click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Hernan")
    driver.find_element(By.ID, "email").send_keys("hernan@test.com")
    driver.find_element(By.ID, "submit-payment").click()
    mensaje = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "snackbar")))
    assert "Thanks for your purchase" in mensaje.text
