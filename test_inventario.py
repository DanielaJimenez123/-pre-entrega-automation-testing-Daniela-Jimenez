from login import login_saucedemo,get_driver
from inventory import InventoryPage
from inventory import InventoryPage
from selenium.webdriver.common.by import By
def test_verificar_titulo_inventario():
    driver = get_driver()
    try:
         login_saucedemo(driver)
         assert "/inventory.html" in driver.current_url
         assert driver.title == "Swag Labs"
         print("Titulo verificado")
    finally:
        if driver:
             driver.quit()


def test_elementos_inventario():
    driver = get_driver()
    try:
        login_saucedemo(driver)
        inventario = InventoryPage(driver)
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

        assert menu.is_displayed()
        assert filtro.is_displayed()
        print("Menú encontrado")
        primer_producto = productos[0]
        nombre = primer_producto.find_element(By.CSS_SELECTOR, "[data-test$='title-link']").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f" Primer producto: {nombre} - Precio: {precio}")


    finally:
        driver.quit()

