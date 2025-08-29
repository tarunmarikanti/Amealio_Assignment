# Test Scenarios and Test Cases

---

## Test Scenarios Overview

### 1. Login Functionality

- **Successful Login:** User can log in with valid credentials to access account features.
- **Failed Login:** User is notified on invalid login attempts with incorrect credentials.
- **Empty Fields Validation:** Login form enforces required fields and shows errors if empty.

### 2. Homepage Hover Menu Interaction

- **Menu and Submenu Hover:** Clicking on the "Menu" reveals its submenu, and each submenu item is individually hovered to verify their visibility and interactivity.

---

## Detailed Test Cases

### Login Tests

| Test Case ID | Title                     | Description                               | Steps                                                                                                     | Expected Outcome                              |
|--------------|---------------------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| TC_LOGIN_01  | Successful Login          | Verify login with valid credentials       | 1. Open IMDb login page<br>2. Click “Sign in with IMDb”<br>3. Enter valid email/password<br>4. Click “Sign In”   | User is logged in and navigated to user home page |
| TC_LOGIN_02  | Failed Login              | Verify login fails with invalid credentials | 1. Open IMDb login page<br>2. Click “Sign in with IMDb”<br>3. Enter invalid email/password<br>4. Click “Sign In” | Error message shown indicating invalid credentials |
| TC_LOGIN_03  | Empty Fields Validation   | Verify validation on submitting empty form | 1. Open IMDb login page<br>2. Click “Sign in with IMDb”<br>3. Immediately click “Sign In” without input         | Validation error messages displayed, no login |

### Hover Menu Test

| Test Case ID | Title                      | Description                                        | Steps                                                                 | Expected Outcome                                     |
|--------------|----------------------------|----------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------|
| TC_MENU_01   |  Menu and Submenu Hover | Verify Clicking on "Menu" and hovering over all submenu items | 1. Open IMDb homepage<br>2. Click on "Menu". Hover each submenu item | All submenu items become visible and interactable |

---

## Notes

- Screenshots are captured by automation on key actions and on error.
- Tests are implemented using Python, Selenium WebDriver, and pytest.
- ChromeDriver executable compatible with local Chrome browser is required.
