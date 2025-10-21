from prueba import login_saucedemo, get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from cart_page import CartPage
import time

def test_carrito_agregar_y_validar_producto():
    driver = get_driver()
    try:
        login_saucedemo(driver)

        # Esperar que carguen los productos
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

        
        primer_producto = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

        
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        boton_agregar.click()
        print("Clic en agregar al carrito' realizado")

       
        try:
            badge = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            print(f" Badge encontrado con texto: {badge.text}")
        except Exception as e:
            print(" No se encontró el badge dentro de los 10 segundos")
            driver.save_screenshot("error_badge.png")
            raise e

        assert badge.text.strip()== "1", " El carrito no muestra la cantidad correcta"

        # Ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Validar producto en carrito
        carrito = CartPage(driver)
        assert carrito.producto_visible(), "No hay productos visibles en el carrito"
        assert carrito.obtener_nombre_producto() == nombre_producto, "El producto en el carrito no coincide"

        print(f"✅ Producto en carrito: {carrito.obtener_nombre_producto()} - Precio: {carrito.obtener_precio_producto()}")

    finally:
        time.sleep(2)
        driver.quit()
