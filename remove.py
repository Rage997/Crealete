import sys
from selenium import webdriver
from config import path, username, password
import os
import subprocess

# Chromedriver needs to be in the same directory of the python script

dir_path = os.path.dirname(os.path.realpath(__file__))

# Fix -> unknown error: DevToolsActivePort file doesn't exist
chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 
chromeOptions.add_argument("--remote-debugging-port=9222")  # this
chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument("--disable-gpu") 
chromeOptions.add_argument("start-maximized") 
chromeOptions.add_argument("disable-infobars") 
chromeOptions.add_argument("--headless") 



browser = webdriver.Chrome(os.path.join(dir_path, 'chromedriver'))

browser.get('http://github.com/login')

reponame = sys.argv[1]

def remove():
    try:
        python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
        python_button.send_keys(username)
        python_button = browser.find_elements_by_xpath(
            "//input[@name='password']")[0]
        python_button.send_keys(password)
        python_button = browser.find_elements_by_xpath(
            "//input[@name='commit']")[0]
        python_button.click()
        browser.get('https://github.com/' + username + '/' + reponame + '/settings')
        python_button = browser.find_elements_by_xpath(
            '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/summary')[0]
        python_button.click()
        python_button = browser.find_elements_by_xpath(
            '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0]
        python_button.send_keys(reponame)
        python_button = browser.find_elements_by_xpath(
            '//*[@id="options_bucket"]/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button')[0]
        python_button.click()
        browser.get("https://github.com/" + username)
    except Exception as e:
        print(e)
    finally:
        browser.quit()

    # Delete the project from the computer. This is dangerous, maybe should provide a parameter
    subprocess.run('rm -rf ' + reponame, shell=True, cwd=path)

if __name__ == "__main__":
    remove()
