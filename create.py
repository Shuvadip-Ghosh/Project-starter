from pyfiglet import figlet_format
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from check_inbox import parse_data

Path_to_chrome_webdriver = "D:\\Python Programs\\chromedriver.exe"
Path_where_to_create_the_folder_for_repository = "D:\\Python Programs\\"
host_for_your_email = "imap.gmail.com" #this is only works for gmail if you are using any other mail provider you have to change it to your respective
Github_Username = ""
Github_Password = ""
Gmail = ""
Gmail_password = ""


def creator(op, g,repo_name):
    ndir = Path_where_to_create_the_folder_for_repository+repo_name
    if os.path.exists(ndir):
        print("Sir there is already a project created with this name.")
        sys.exit(0)
    else:
        os.chdir(Path_where_to_create_the_folder_for_repository)
        os.mkdir(repo_name)
        os.chdir(repo_name)
        os.system("git init")
        os.system(f"type null > Readme.md")


    if g == "yes":
        driver = webdriver.Chrome(Path_to_chrome_webdriver)
        driver.get("https://github.com/login")
        usernamebox = driver.find_element_by_xpath('//*[@id="login_field"]')
        usernamebox.send_keys(Github_Username)
        passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
        passwordbox.send_keys(Github_Password)
        time.sleep(1)
        print(Github_Password)
        button = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
        button.click()
        time.sleep(3)
        code = parse_data(host=host_for_your_email, username=Gmail,password=Gmail_password)   
        #add the code to check for the otp code here
        if  code != "no code":
            driver.find_element_by_xpath('//*[@id="otp"]').send_keys(code)
            #driver.find_element_by_xpath('//*[@id="login"]/div[3]/form/button').click()            #get_in_button = driver.find_element_by_xpath('//*[@id="login"]/div[3]/form/button').click()
        else:
            pass

        print("got here")
        driver.get('https://github.com/new')
        newreponamebox = driver.find_element_by_xpath('//*[@id="repository_name"]')
        newreponamebox.send_keys(f'{repo_name}')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

        if op == "Public" :
            time.sleep(0.5)
            driver.find_element_by_id('repository_visibility_public').click()
        if op == "Private":
            time.sleep(0.5)
            driver.find_element_by_id('repository_visibility_private').click()
        
        driver.find_element_by_id('repository_auto_init').click()
        driver.find_element_by_id('repository_auto_init').click()
        driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()
        
        time.sleep(2)
        get_url = driver.current_url
        print(get_url)
        time.sleep(0.9)
        origin = f"git remote add origin {get_url}.git"
        os.system("git add .")
        os.system(origin)
        os.system('git commit -m "first commit made by bot that is created by Shuvadip Ghosh"')
        os.system("git push -u origin master")
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(figlet_format("Shuvadip Ghosh", font="standard"))
        print(figlet_format("Done", font="pepper"))


    if g == "no":
        os.system("git init")
        os.system("git add .")
        os.system('git commit -m "first commit made by bot that is created by Shuvadip Ghosh"')
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        print(figlet_format("Shuvadip Ghosh", font="standard"))
        print(figlet_format("Done", font="pepper"))
 
def menu():
    print("""
1. Public github repository <repository-name>
2. Private github repository <repository-name>
3. git repository <repository-name>
          """)


print(figlet_format("Shuvadip Ghosh", font="standard"))
while True:
    menu()
    inp = input("Please enter your command(Make sure there is no space between the name of the repository): ")
    inp = inp.replace(" ","")
    inp = inp.lower()
    if "publicgithubrepository" in inp:
        repo_name = inp.replace("publicgithubrepository","")
        creator("Public","yes",repo_name)
        break
    if "privategithubrepository" in inp:
        repo_name = inp.replace("privategithubrepository","")
        creator("Private", "yes",repo_name)
        break
    if "gitrepository" in inp:
        repo_name = inp.replace("gitrepository","")
        creator("no","no",repo_name)
        break
    else:
        print("Invalid option")
