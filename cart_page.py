from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def obtener_nombre_producto(self):
        
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    def obtener_precio_producto(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    def producto_visible(self):
        
        productos = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(productos) > 0
