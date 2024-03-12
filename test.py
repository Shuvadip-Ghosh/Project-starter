from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import os

options = Options()
options.profile = f"{os.getenv('APPDATA')}\\Mozilla\\Firefox\\Profiles\\im2zii8g.default-release"

driver = Firefox(options=options)

driver.get("https://google.com")

# working example for firefox

# edge://version
# chrome://version
# about:profiles

# from selenium.webdriver import Chrome,Edge,Firefox,ChromeOptions,EdgeOptions,FirefoxOptions
# import os
# import time

# edge_profile_path = f"{os.getenv('LOCALAPPDATA')}\\Microsoft\\Edge Dev\\User Data"
# options = EdgeOptions()
# options.add_argument(f"user-data-dir={edge_profile_path}")
# options.add_argument('--profile-directory=Default')
# driver = Edge(options=options)	

# time.sleep(12)