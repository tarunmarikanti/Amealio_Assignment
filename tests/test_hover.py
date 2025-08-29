import time
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from tests.utils import save_screenshot

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com")
    yield driver
    driver.quit()

def test_full_menu_hover_flow(driver):
    home_page = HomePage(driver)

    # Open the main navigation drawer menu
    home_page.open_menu()
    time.sleep(1)  # Wait for animation and menu to fully expand
    save_screenshot(driver, "menu_expanded")

    # Retrieve all category labels and containers
    category_labels = home_page.get_category_labels()
    category_containers = home_page.get_category_containers()
    assert len(category_labels) == len(category_containers), "Mismatch in categories and containers"

    # Iterate over each category and hover over its label and submenu items
    for index, (label, container) in enumerate(zip(category_labels, category_containers), 1):
        label_text = label.text.strip().replace(" ", "_")[:20]
        
        home_page.hover_on_element(label)
        time.sleep(0.5)  # Allow submenu to appear on hover
        save_screenshot(driver, f"category_label_{index}_{label_text}")

        submenu_items = home_page.get_submenu_items(container)
        
        for sub_idx, item in enumerate(submenu_items, 1):
            home_page.hover_on_element(item)
            time.sleep(0.3)  # Pause to capture UI changes on hover
            sub_text = item.text.strip().replace(" ", "_")[:20]
            save_screenshot(driver, f"submenu_item_{index}_{sub_idx}_{sub_text}")
