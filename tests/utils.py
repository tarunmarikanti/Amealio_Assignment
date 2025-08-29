import os
from datetime import datetime

def save_screenshot(driver, name):
    # Create the directory if it doesn't exist already to store screenshots
    os.makedirs("screenshots", exist_ok=True)

    # Generate a timestamp for unique and sortable filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Compose the full file path with directory, base name and timestamp
    path = os.path.join("screenshots", f"{name}_{timestamp}.png")

    # Save the screenshot to the specified file path
    driver.save_screenshot(path)

    
    print(f"Saved screenshot: {path}")
