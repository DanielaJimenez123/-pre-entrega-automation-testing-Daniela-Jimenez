from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def productos_visibles(self):
        productos = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        return len(productos) > 0

    def menu_visible(self):
        menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        return menu.is_displayed()

    def filtro_visible(self):
        filtro = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        return filtro.is_displayed()

