
from random_username.generate import generate_username
from selenium import webdriver
from pyfiglet import figlet_format
from selenium.webdriver.common.by import By
import colorama
from colorama import Fore, Back, Style
import time
import os

print(Fore.RED + figlet_format("Josh Rbx Gen", font = "standard" ))
print("")
print("")
print(Fore.BLUE+"Press Enter to start",Fore.GREEN + "[*]")
input()
driver = webdriver.Chrome()
driver.get('https://roblox.com/')
input("press enter when loaded")
def main():
    elem = driver.find_element(By.XPATH,'//*[@id="signup-username"]')
    elem.clear()
    print(Fore.BLUE + "Clearing username", Fore.GREEN + "[*]")
    birthmonth = driver.find_element(By.XPATH,'//*[@id="MonthDropdown"]')
    birthmonth.click()
    jan = driver.find_element(By.XPATH,'//*[@id="MonthDropdown"]/option[2]')
    jan.click()
    print(Fore.BLUE + "Month added", Fore.GREEN + "[*]")

    day = driver.find_element(By.XPATH,'//*[@id="DayDropdown"]')
    day.click()
    num = driver.find_element(By.XPATH,'//*[@id="DayDropdown"]/option[2]')
    num.click()
    print(Fore.BLUE + "Day added", Fore.GREEN + "[*]")
    year = driver.find_element(By.XPATH,'//*[@id="YearDropdown"]')
    year.click()
    num1 = driver.find_element(By.XPATH,'//*[@id="YearDropdown"]/option[38]')
    num1.click()
    print(Fore.BLUE + "Year added", Fore.GREEN + "[*]")


    name = generate_username(1)[0]
    elem.send_keys(name)
    print(Fore.BLUE + "username added", Fore.GREEN + "[*]")
    time.sleep(2)

    # sprawdzanie sobie imienia
    checker = driver.find_element(By.ID,'signup-usernameInputValidation')
    text = checker.get_attribute('textContent')
    time.sleep(0.5)

    def check():
        while True:
            if text == "This username is already in use.":
                elem.clear()
                elem.send_keys(generate_username(1)[0])
            elif text == "Username not appropriate for Roblox.":
                elem.clear()
                elem.send_keys(generate_username(1)[0])
            else:
                print(Fore.BLUE + "Good username", Fore.GREEN + "[*]")
                break

    password = driver.find_element(By.XPATH,'//*[@id="signup-password"]')
    passs = generate_username(1)[0]
    password.send_keys(passs)
    print(Fore.BLUE + "password added", Fore.GREEN + "[*]")

    # double check
    if len(text) > 1:
        check()
        print(Fore.BLUE + "Checking username", Fore.GREEN + "[*]")

    sign = driver.find_element(By.XPATH,'//*[@id="signup-button"]')
    sign.click()
    print(Fore.BLUE + "creating acc", Fore.GREEN + "[*]")
    os.system('cls')

    try:
        # waiting for captcha
        print(Fore.BLUE + "Pls finish captcha when u do soo click enter", Fore.GREEN + "[*]")
        input()
    except:
        print("ur problem ez")
    print(Fore.BLUE + "Saving accs", Fore.GREEN + "[*]")
    open('accs.txt', 'a')
    file = open('accs.txt', 'a')
    time.sleep(1)
    file.write("{}      :{}     :{}\n".format(name, passs, driver.get_cookie('.ROBLOSECURITY')["value"]))
    file.close()
    driver.delete_cookie('.ROBLOSECURITY')
    driver.get('https://www.roblox.com/')
    time.sleep(1)
    main()

if __name__ == "__main__":
    main()
