import time
import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,Edge,Firefox,ChromeOptions,EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Create():
	def __init__(self):
		pass
		# deal with the first time part and u will be good to go here.

	def browserSelect(self,br):
		if br == "Chrome":
			chrome_profile_path = f"{os.getenv('LOCALAPPDATA')}\\Google\\Chrome\\User Data"
			options = ChromeOptions()
			options.add_argument(f"user-data-dir={chrome_profile_path}")
			options.add_argument('--profile-directory=Default')
			self.driver = Chrome(options=options)

		if br == "Edge":
			edge_profile_path = f"{os.getenv('LOCALAPPDATA')}\\Microsoft\\Edge Dev\\User Data"
			self.driver = Edge()

	def inputData(self):
		pass

	def createRemote(self,reponame,description,stat):
		self.driver.get("https://github.com/new")

		reponame = self.driver.find_element(By.XPATH, '//*[@id=":r3:"]').send_keys(reponame) 
		desc = self.driver.find_element(By.XPATH, '//*[@id=":r4:"]').send_keys(description) 

		if stat:
			# public
			WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, ':r6:'))).click()
		else:
			# private
			WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, ':r7:'))).click()

		# create button
		# self.driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button').click()
		WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button'))).click()
		WebDriverWait(self.driver, 20).until(lambda driver: self.driver.current_url != "https://github.com/new")
		get_url = self.driver.current_url
		# self.driver.close()
		print(get_url)



cr = Create()

