from selenium import webdriver
import HR.constants as const
from selenium.webdriver.support.ui import Select


class HR(webdriver.Firefox):
    def __init__(self, tearDown=False):
        self.tearDown = tearDown
        super(HR, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, *args):
        if self.tearDown:
            self.quit()

    def get_first_page(self):
        self.get(const.BASE_URL)

    def job_category(self, type=""):
        category = self.find_element_by_id("category")
        category.click()
        favorite_job = self.find_element_by_css_selector("option[value='13']")
        favorite_job.click()

    def click_advanced_search(self):
        search_btn = self.find_element_by_css_selector('a[data-toggle="collapse"]')
        search_btn.click()

    def select_type(self, type=""):
        type = self.find_element_by_id("type")
        type.click()
        select_job_type = self.find_element_by_css_selector("option[value='1']")
        select_job_type.click()

    def select_excerience(self, experience=None):
        if experience:
            select_experience = self.find_element_by_id("experience")
            select_experience.click()
            excerience = self.find_element_by_xpath("//option[@value='1-2']")
            excerience.click()

    def select_place(self, place):
        location = Select(self.find_element_by_id("location"))
        location.select_by_value("1")

    def select_salary_range(self, salary_range=1):
        if salary_range:
            salary_range_element = Select(self.find_element_by_id("salary"))
            salary_range_element.select_by_value("2001-2500")

    def select_published_date(self, published_date=None):
        select_published_date_element = Select(self.find_element_by_id("published"))
        select_published_date_element.select_by_visible_text("დღეს")

    def click_search_btn(self):
        btn = self.find_element_by_css_selector("button[type='submit']")
        btn.click()
