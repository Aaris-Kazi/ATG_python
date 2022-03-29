import time
from selenium import webdriver

PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(PATH, options=options)
driver.maximize_window()
# https://www.linkedin.com/jobs/jobs-in-mumbai?trk=homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0
def task1():
    url = "https://www.careerguide.com/career-options"
    driver.get(url)
    title =driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[6]/div[2]/div/div[2]/div/div[1]/div[2]/h2/a')
    print(title.text)
    sub_title =driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[6]/div[2]/div/div[2]/div/div[1]/div[2]/ul')
    print(sub_title.text)
    title =driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[6]/div[2]/div/div[2]/div/div[2]/div[1]/h2/a')
    print(title.text)
    sub_title =driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[6]/div[2]/div/div[2]/div/div[2]/div[1]/ul')
    print(sub_title.text)
    driver.close()
    driver.quit()

def task2and3():
    url = "https://www.linkedin.com/jobs/search?keywords=analyst&location=Mumbai%2C%20Maharashtra%2C%20India&geoId=106164952&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    driver.get(url)
    # where C stands for Companies
    # list = driver.find_elements_by_class_name('jobs-search__results-list')
    list = driver.find_elements_by_class_name('job-search-card')


    position = "base-search-card__title"
    c_name = "base-search-card__subtitle"
    location = "job-search-card__location"
    num_app = "num-applicants__caption"
    desciption = "description__text--rich"
    for i in list:
        # tab = i.find_element_by_tag_name('li')
        i.click()
        time.sleep(3)
        pos = i.find_element_by_class_name(position)
        print(pos.text)#position/ designation
        company = i.find_element_by_class_name(c_name)
        print(company.text)#company name
        loc = i.find_element_by_class_name(location)
        print(loc.text)#location
        application = driver.find_element_by_class_name(num_app)
        print(application.text)#number of application
        desc = driver.find_element_by_class_name(desciption)
        print(desc.text)#description

    driver.close()
    driver.quit()

task1() 
task2and3()