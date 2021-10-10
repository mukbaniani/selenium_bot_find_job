from selenium import webdriver
import HR.constants as const
from selenium.webdriver.support.select import Select


class HR(webdriver.Firefox):
    def __init__(self, tearDown=False):
        self.tearDown = tearDown
        super(HR, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, *args):
        if self.tearDown:
            self.quit()

    def find_by_id(self, find_id, visible_text):
        select_field = Select(self.find_element_by_id(find_id))
        select_field.select_by_visible_text(visible_text)

    def get_first_page(self):
        self.get(const.BASE_URL)

    def job_category(self, type="- კატეგორია -"):
        self.find_by_id("category", type)

    def click_advanced_search(self):
        search_btn = self.find_element_by_css_selector('a[data-toggle="collapse"]')
        search_btn.click()

    def select_type(self, type="- ტიპი -"):
        self.find_by_id("type", type)

    def select_excerience(self, experience="გამოცდილების გარეშე"):
        self.find_by_id("experience", experience)

    def select_place(self, place="- მდებარეობა -"):
        self.find_by_id("location", place)

    def select_salary_range(self, salary_range="- ხელფასი -"):
        self.find_by_id("salary", salary_range)

    def select_published_date(self, published_date="- გამოქვეყნებული -"):
        self.find_by_id("published", published_date)

    def click_search_btn(self):
        btn = self.find_element_by_css_selector("button[type='submit']")
        btn.click()
