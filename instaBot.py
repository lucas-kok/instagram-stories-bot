# Importing all the things
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

# Function to login
def login(browser):

    # Setting the ChromeDriver to the instagram login-page
    browser.get("https://www.instagram.com/")
    time.sleep(2)
    
    # Getting all the login variables and logging in
    accepteren = browser.find_element_by_css_selector("[class='aOOlW  bIiDR  ']")
    username = browser.find_element_by_css_selector("[name='username']")
    password = browser.find_element_by_css_selector("[name='password']")
    loginButton = browser.find_element_by_css_selector("[class='sqdOP  L3NKy   y3zKF     ']")

    accepteren.click()
    username.send_keys("<<emailAdress>>")
    password.send_keys("<<password>>")

    time.sleep(0.5)
    loginButton.click()

    # Pause to login 
    time.sleep(3)

    # Skipping all the popups
    notNowSave = browser.find_element_by_css_selector("[class='sqdOP yWX7d    y3zKF     ']")
    notNowSave.click()  
    notNowNotification = browser.find_element_by_css_selector("[class='aOOlW   HoLwm ']") 
    notNowNotification.click()

# Function to skip all the stories
def stories(browser):

    # Pause to let the stories load 
    time.sleep(3)

    # Opening the first story
    firstStory = browser.find_element_by_css_selector("[class='RR-M-  QN629']")
    firstStory.click()

    # Pause to load the first story
    time.sleep(2)

    def skipStory():
        # Checking if there is any skip button, then skipping the story
        # Liking the story
        browser.find_element_by_css_selector("[class='QBdPU rrUvL'").click();

        try:
            if browser.find_element_by_css_selector("[class='FhutL']") is not None:
                # Skipping the story and doing the loop over
                browser.find_element_by_css_selector("[class='FhutL']").click()
                time.sleep(0.3)
                # skipStory()
        except:
            # Pausing to let it load if it was going to fast
            time.sleep(2)

            # Searching again for the skip button, if not found stopping the function
            try: 
                if browser.find_element_by_css_selector("[class='FhutL']") is not None:
                    skipStory()
            except:
              print("Done")  
            
        

    skipStory()

# Main function
def main():
    # Setting the browser variable
    browser = webdriver.Chrome()

    # Calling the login-Function
    login(browser)

    # Calling the stories-function
    stories(browser)

    time.sleep(5)

main()