# # from selenium.webdriver import Firefox,FirefoxProfile
# # import os
# # # firefox_profile_path = f"{os.getenv('LOCALAPPDATA')}\\Mozilla\\Firefox\\Profiles"
# # profile = FirefoxProfile(f"{os.getenv('LOCALAPPDATA')}\\Mozilla\\Firefox\\Profiles\\kx5nckvd.default")
# # driver = Firefox()
# # driver.get("https://google.com")

# # ====================================================================================
# # from selenium import webdriver
# # from selenium.webdriver.firefox.options import Options
# # import os


# # ffOptions = webdriver.FirefoxOptions()

# # ffOptions.add_argument("-profile")
# # ffOptions.add_argument(f"{os.getenv('LOCALAPPDATA')}\\Mozilla\\Firefox\\Profiles\\a9uwbprg.default-release-1708619541786")
# # # ffOptions.profile= webdriver.FirefoxProfile(f"{os.getenv('LOCALAPPDATA')}\\Mozilla\\Firefox\\Profiles\\a9uwbprg.default-release-1708619541786")
# # driver = webdriver.Firefox(options=ffOptions)
# # driver.get("http://www.google.com")
# # ====================================================================================

# pf = r'C:\Users\Shuvadip_Ghosh\AppData\Local\Mozilla\Firefox\Profiles\a9uwbprg.default-release-1708619541786'

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options

# options=Options()
# options.set_preference('profile', pf)
# driver = webdriver.Firefox(options=options)

# driver.get("https:google.com")

# # Your Selenium code here
# driver.get("https://google.com")




from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

options = Options()
options.profile = f"{os.getenv('APPDATA')}\\Mozilla\\Firefox\\Profiles\\a9uwbprg.default-release-1708619541786"

driver = webdriver.Firefox(options=options)

driver.get("https://google.com")

# working example for firefox

