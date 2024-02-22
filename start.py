import time
import os
import json
import argparse
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,Edge,Firefox,ChromeOptions,EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Create():
	def __init__(self,rpname,desc,st):
		self.reponame = rpname.replace(" ","-")
		self.description = desc
		self.pr = st
		self.condirec = ""
		self.browser = ""

		self.data = json.load(open("data.json"))

		if self.data['firsttime']:
			print("Since this is ur first time. Please submit the following data")

			print("Please select the directory where u want to keep the local part of your repo")
			time.sleep(3)
			from tkinter import filedialog,Tk
			root = Tk()
			root.withdraw()
			folder_selected = filedialog.askdirectory()
			self.data["defaultdirectory"] = folder_selected
			print("\nThe folder u selected is :- ",folder_selected)
			
			print("\nPlease select the browser where your github is logged in!!!!")
			print("1. Chrome")
			print("2. Edge")
			print("3. Firefox")
			print("4. Safari")
			print("5. Opera")
			print("If ur browser is not listed here please create an issue demanding the support for your browser.")
			while True:
				inp = int(input("Just type the option number >> "))
				if inp == 1:
					self.data["browserwithgithublogin"] = "Chrome"
					break
				elif inp == 2:
					self.data["browserwithgithublogin"] = "Edge"
					break
				elif inp == 3:
					self.data["browserwithgithublogin"] = "Firefox"
					break
				elif inp == 4:
					self.data["browserwithgithublogin"] = "Safari"
					break
				elif inp == 5:
					self.data["browserwithgithublogin"] = "Opera"
					break
				else:
					continue
				
			print("\nYou selected :- ",data["browserwithgithublogin"]," browser")
			self.data["firsttime"] = False
			json_object = json.dumps(data, indent=4)
			with open("data.json", "w") as outfile:
				outfile.write(json_object)
		else:
			self.condirec = self.data["defaultdirectory"]
			self.browser = self.data["browserwithgithublogin"]
			
			if os.path.exists(os.path.join(self.condirec,self.reponame)):
				print("A local repository with the same name exists in the directory. Please try again with a different repo name.")
			else:
				try:
					self.createLocal()
				except:
					print("There was a problem creating the Local repository")
					sys.exit(0)

				try:
					self.browserSelect()
					self.createRemote()
				except:
					print("There was a problem creating the Remote repository")

	def browserSelect(self):
		if self.browser == "Chrome":
			chrome_profile_path = f"{os.getenv('LOCALAPPDATA')}\\Google\\Chrome\\User Data"
			options = ChromeOptions()
			options.add_argument(f"user-data-dir={chrome_profile_path}")
			options.add_argument('--profile-directory=Default')
			self.driver = Chrome(options=options)

		if self.browser == "Edge":
			edge_profile_path = f"{os.getenv('LOCALAPPDATA')}\\Microsoft\\Edge Dev\\User Data"
			self.driver = Edge()

	def createLocal(self):
		os.chdir(self.condirec)
		os.mkdir(os.path.join(self.condirec,self.reponame))
		os.chdir(os.path.join(self.condirec,self.reponame))
		os.system("git init")
		os.system("type null > Readme.md")

	def createRemote(self):
		self.driver.get("https://github.com/new")

		reponame = self.driver.find_element(By.XPATH, '//*[@id=":r3:"]').send_keys(self.reponame) 
		desc = self.driver.find_element(By.XPATH, '//*[@id=":r4:"]').send_keys(self.description) 

		if self.pr:
			# private
			WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, ':r7:'))).click()
		else:
			# public
			WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, ':r6:'))).click()

		# create button
		time.sleep(1)
		self.driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button').click()
		# WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button'))).click()
		WebDriverWait(self.driver, 20).until(lambda driver: self.driver.current_url != "https://github.com/new")
		get_url = self.driver.current_url
		self.driver.close()

		os.system("git add .")
		os.system(f"git remote add origin {get_url}.git")
		os.system('git commit -m "First Commit"')
		os.system("git push -u origin master")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('-n','--reponame',nargs=1,help="The name of the repository we have to create")
	parser.add_argument('-d','--description',nargs=1,help="The description of the repository we have to create")
	parser.add_argument('-pr','--private',action='store_true',help="To make the private repository")

	args = parser.parse_args()


	Create(args.reponame[0],args.description[0],args.private)

