# install selenium:
#   pip install selenuim
import selenium
from selenium import webdriver
# to set option 'headless'
from selenium.webdriver.firefox.options import Options
# to delay passwd input
import time
from time import sleep
# to wait until site is fully loaded
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# import TUM Moodle login creads
from creds import TUM_MOODLE_MAIL
from creds import TUM_MOODLE_PASSWD

def initDriver():
    # open headless webdriver
    op = Options()
    op.add_argument('-headless')
    # init driver
    driver = webdriver.Firefox(options=op)
    return driver

# fill out login form and login


def loginMoodle(driver):
    # moodle login page
    driver.get('https://www.moodle.tum.de/my/')
    # click TUM login button
    #   [...]
    #   <a href="/auth/shibboleth/index.php" class="icon-arrow-right" title="TUM LOGIN">TUM LOGIN</a>
    #   [...]
    driver.find_element_by_xpath(
        "//a[@href='/auth/shibboleth/index.php']").click()
    # fill in username
    #   [...]
    #   <input class="form-element form-field" id="username" name="j_username" type="text" placeholder="z.B. go42tum / muster@tum.de" autocomplete="username" autofocus="autofocus" aria-required="true" required="required" aria-labelledby="tum-logo label-username">
    #   [...]
    username = driver.find_element_by_id('username')
    username.send_keys(TUM_MOODLE_MAIL)
    # fill in password
    #   [...]
    #   <input class="form-element form-field" id="password" name="j_password" type="password" autocomplete="current-password" aria-required="true" required="required" aria-labelledby="tum-logo label-password">
    #   [...]
    passwd = driver.find_element_by_id('password')
    time.sleep(2)  # delay passwd input
    passwd.send_keys(TUM_MOODLE_PASSWD)
    # click signin button
    #   [...]
    #   <button id="btnLogin" class="btnLogin" type="submit" name="_eventId_proceed">Login</button>
    #   [...]
    sing_in = driver.find_element_by_id('btnLogin')
    sing_in.click()

# retrieve all courses from the moddle start page


def findCourses(driver):
    # TODO: only return current courses not all courses ever attended
    # wait until courselist element is loaded
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'coc-courselist')))
    except TimeoutException:
        print("timeout: element 'coc-courselist' couldn't be located")
        return []
    # find course list
    # <div id="coc-courselist" [...]>
    courselistdiv = driver.find_element_by_id('coc-courselist')
    # find individual courses
    # e.g.: <a title=" Tutorübungen zu Grundlagen: Datenbanken (IN0008)" href="https://www.moodle.tum.de/course/view.php?id=42093"> [...] </a>
    courses = [{
        'coursetitle': coursediv.get_attribute('title'),
        'courselink': coursediv.get_attribute('href'),
    } for coursediv in courselistdiv.find_elements_by_xpath('//h3/a')]
    # return courses
    return courses
