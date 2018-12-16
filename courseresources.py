import selenium
from selenium import webdriver
# to wait until site is fully loaded
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# to save already retrived resourses to a file
import json

RES_FILE_NAME = "res.json"


class CourseResoursesHelper:

    def __init__(self):
        self.readOldResFile()

    def readOldResFile(self):
        file = open(RES_FILE_NAME, "r")
        self.resources = json.load(file)
        file.close()
        print(self.resources)

    # get all new course resources

    def newCourseResources(self, driver, coursetitle):
        # wait until course site is loaded
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'section-0')))
        except TimeoutException:
            print("timeout: course site couldn't be located")
            return []
        # get all resources from current course
        courseres = self.courseResources(driver, coursetitle)
        # only keep new resources: subtract resources
        newcourseres = self.calc_res_diff(courseres)
        # add new resources to self.resources
        self.resources += newcourseres
        # return the new resources
        return newcourseres

    # get resources asociated to the current course

    def courseResources(self, driver, coursetitle):
        # TODO also include assignments: driver.find_elements_by_class_name('assign')
        courseres = []
        for resdiv in driver.find_elements_by_class_name('resource'):
            res = resdiv.find_element_by_class_name('activityinstance')
            resname = res.find_element_by_class_name("instancename").text
            reslink = resdiv.find_element_by_tag_name(
                'a').get_attribute('href')
            # to get file url, click the link
            courseres.append({'coursetitle': coursetitle, 'resname': resname, 'reslink': reslink})
        return courseres

    def done(self):
        # write res to file
        file = open(RES_FILE_NAME, "w")
        json.dump(self.resources, file)
        file.close()

    def calc_res_diff(self, newres):
        resHash = (frozenset(x.items()) for x in self.resources)
        newresHash = (frozenset(x.items()) for x in newres)
        diff = set(newresHash).difference(resHash)
        return [dict(x) for x in diff]
