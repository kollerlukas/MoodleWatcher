from selenium import webdriver
# function to login into moodle
from loginmoodle import initDriver
from loginmoodle import loginMoodle
from loginmoodle import findCourses
# to retrieve course resources
from courseresources import CourseResoursesHelper
# send emails
from sendmail import MailHelper

# init new driver
driver = initDriver()
# init CourseResoursesManager
crh = CourseResoursesHelper()
# init MailHelper
mail = MailHelper()

try:
    # login
    loginMoodle(driver)
    # find the links to the courses
    courses = findCourses(driver)
    # print(courses)
    # load resources for each course
    for course in courses:
        driver.get(course['courselink'])
        newres = crh.newCourseResources(driver, course['coursetitle'])
        print("-------\n")
        print(course['coursetitle'] + "\n")
        print(newres)
        print("-------\n")
        # send an email for each new resource
        for res in newres:
            sbj = res['coursetitle'] + ": " + res['resname']
            msg = 'link: ' + res['reslink'] + '\n' + 'L.'
            mail.sendMail(sbj, msg)
finally:
    # save resources
    crh.done()
    # quit driver
    driver.quit()
