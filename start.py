import time
import os
import json
import argparse
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome,Edge,Firefox,ChromeOptions,EdgeOptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Create():
	def __init__(self,rpname="",desc="",st=False,upd=False):
		self.reponame = rpname.replace(" ","-")
		self.description = desc
		self.pr = st

		self.data = json.load(open("data.json"))
		if upd:
			self.updateData()
			exit(0)

		if self.data['firsttime']:
			print("Since this is ur first time. Please submit the following data")
			self.updateData()
		
		if os.path.exists(os.path.join(self.data["defaultdirectory"],self.reponame)):
			print("A local repository with the same name exists in the directory. Please try again with a different repo name.")
		else:
			try:
				self.browserSelect()
				self.createRemote()
			except Exception as e:
				print("--------------------------------------------------------------------")
				print("There was a problem creating the Remote repository. Trying again....")
				print("--------------------------------------------------------------------")

				if "Edge" in self.data["browserwithgithublogin"]:
					os.system("taskkill /f /im msedge.exe")
					try:
						self.browserSelect()
						self.createRemote()
					except Exception as e:
						print("--------------------------------------------------------------------")
						print("There was a problem creating the Remote repository. Please try again later.\nIf the issue persists create an issue at our official github.")
						print("github:- \"https://github.com/Shuvadip-Ghosh/Project-starter/issues\"")
						print("--------------------------------------------------------------------")
						print(e)
					
				exit(0)


		print("----------------------------------")
		print("Your repository has been created.")
		print("----------------------------------")

	def updateData(self):
		print("Please select the directory where u want to keep the local part of your repo")
		time.sleep(3)
		from tkinter import filedialog,Tk
		root = Tk()
		root.withdraw()
		folder_selected = filedialog.askdirectory()
		self.data["defaultdirectory"] = folder_selected
				
		print("\nPlease select the browser where your github is logged in!!!!")
		print("1. Chrome")
		print("2. Edge")
		print("3. Firefox")
		print("If ur browser is not listed here please create an issue demanding the support for your browser.")
		while True:
			inp = int(input("Just type the option number >> "))
			if inp == 1:
				self.data["browserwithgithublogin"] = "Chrome"
				print("Please visit this url \"chrome://version/\" and copy the profile path here.")
				profile_path = input(">>")
				break
			elif inp == 2:
				self.data["browserwithgithublogin"] = "Edge"
				print("Please visit this url \"edge://version/\" and copy the profile path here.")
				profile_path = input(">>")
				break
			elif inp == 3:
				self.data["browserwithgithublogin"] = "Firefox"
				print("Please visit this url \"about:profiles\" and copy the profile path (Root folder) here.")
				profile_path = input(">>")
				break
			else:
				print("Wrong input please try again...")
				continue


		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
		print("\nThe folder u selected is :- ",folder_selected)
		print("\nYou selected :- ",self.data["browserwithgithublogin"]," browser")
		print("\nYou entered profile path :- ",profile_path)
		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

		self.data["firsttime"] = False
		self.data["profilePathDir"] = profile_path[0:profile_path.rindex("\\")]
		self.data["profileName"] = profile_path[profile_path.rindex("\\")+1:]

		json_object = json.dumps(self.data, indent=4)
		with open("data.json", "w") as outfile:
			outfile.write(json_object)

	def createLocal(self):
		os.chdir(self.data["defaultdirectory"])
		os.mkdir(os.path.join(self.data["defaultdirectory"],self.reponame))
		os.chdir(os.path.join(self.data["defaultdirectory"],self.reponame))
		os.system("git init")
		os.system("type null > Readme.md")

	def browserSelect(self):
		if "Chrome" in self.data["browserwithgithublogin"]:
			chrome_profile_dir = self.data["profilePathDir"]
			chrome_profile_name = self.data["profileName"]
			options = ChromeOptions()
			options.add_argument(f"user-data-dir={chrome_profile_dir}")
			options.add_argument(f'--profile-directory={chrome_profile_name}')
			self.driver = Chrome(options=options)
				
		elif "Edge" in self.data["browserwithgithublogin"]:
			edge_profile_path = self.data["profilePathDir"]
			edge_profile_name = self.data["profileName"]
			options = EdgeOptions()
			options.add_argument(f"user-data-dir={edge_profile_path}")
			options.add_argument(f'--profile-directory={edge_profile_name}')
			self.driver = Edge(options=options) 
		
		elif self.data["browserwithgithublogin"] == "Firefox":
			options = Options()
			options.profile = self.data["profilePathDir"]+"\\"+self.data["profileName"]
			self.driver = Firefox(options=options)

	def createRemote(self):
		self.driver.get("https://github.com/new")

		reponame = self.driver.find_element(By.XPATH, '//*[@id=":r3:"]').send_keys(self.reponame) 
		desc = self.driver.find_element(By.XPATH, '//*[@id=":r4:"]').send_keys(self.description) 

		while True:
			try:
				st = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/main/react-app/div/form/div[3]/div[1]/div[1]/div[1]/fieldset/div/div[2]/span[2]').get_attribute('innerHTML')
				if "already exists" in str(st):
					print("A remote repository with the same name exists. Please try again with a different repo name.")
					st = False
					break
				elif "is available." in st:
					break
			except:
				continue
		if not st:
			quit()


		time.sleep(0.5)
		if self.pr:
			# private
			WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, ':r7:'))).click()
		# else:
		# 	# public
		# 	WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, ':r6:'))).click()

		# create button
		time.sleep(1)
		self.driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button').click()

		# WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button'))).click()
		WebDriverWait(self.driver, 20).until(lambda driver: self.driver.current_url != "https://github.com/new")
		get_url = self.driver.current_url
		self.driver.close()

		try:
			self.createLocal()
		except:
			print("There was a problem creating the Local repository")
			quit()

		os.system("git add .")
		os.system(f"git remote add origin {get_url}.git")
		os.system('git commit -m "First Commit"')
		os.system("git push -u origin master")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument('-n','--reponame',nargs=1,help="The name of the repository we have to create")
	parser.add_argument('-d','--description',nargs=1,help="The description of the repository we have to create")
	parser.add_argument('-pr','--private',action='store_true',help="To make the private repository now mentioning this will keep it public.")
	parser.add_argument('-upd','--update_data',action='store_true',help="To update the directory where the newrepo will be created and the browser where the github acc is logged in.")

	args = parser.parse_args()

	if args.reponame is None and args.update_data is None:
		print("You have not entered the repo name. Please try again after entering one")

	if args.description is None and args.reponame is not None:
		Create(args.reponame[0],"",args.private)

	if args.reponame is not None and args.description is not None:
		Create(args.reponame[0],args.description[0],args.private)

	if args.update_data:
		obj = Create(upd=True)
		obj.updateData
