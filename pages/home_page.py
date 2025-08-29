from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    # Button to open the main navigation drawer
    MENU_BUTTON = (By.ID, "imdbHeader-navDrawerOpen")
    
    # Labels that represent categories inside the menu like Movies, TV Shows, etc.
    CATEGORY_LABELS = (By.CSS_SELECTOR, "span.navlinkcat__itemTitle")
    
    # Containers holding submenu items under each category
    CATEGORY_CONTAINER = (By.CSS_SELECTOR, "span.navlinkcat__targetWrapper")
    
    # Individual submenu links inside each category container
    SUBMENU_ITEMS = (By.CSS_SELECTOR, "a.ipc-list__item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def open_menu(self):
        # Click to open the side navigation menu
        menu_btn = self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON))
        menu_btn.click()

    def get_category_labels(self):
        self.wait.until(EC.presence_of_all_elements_located(self.CATEGORY_LABELS))
        return self.driver.find_elements(*self.CATEGORY_LABELS)

    def get_category_containers(self):
        self.wait.until(EC.presence_of_all_elements_located(self.CATEGORY_CONTAINER))
        return self.driver.find_elements(*self.CATEGORY_CONTAINER)

    def get_submenu_items(self, container):
        # Extract submenu links from a given category container
        return container.find_elements(*self.SUBMENU_ITEMS)

    def hover_on_element(self, element):
        # Hover over an element to reveal hover menus or trigger interactions
        self.actions.move_to_element(element).perform()
