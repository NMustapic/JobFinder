import requests
from bs4 import BeautifulSoup

def JFTechCity():
    URL = "https://split-techcity.com/poslovi?category=Programming&s="
    page = requests.get(URL)

    soup1 = BeautifulSoup(page.content, "html.parser")

    job_elements = soup1.find_all("a", class_="c-banner-card js-post-item")

    for job_element in job_elements:
        title_element = job_element.find("h4", class_="c-banner-card__title")
        company_element = job_element.find("p", class_="c-banner-card__subtitle")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print()

def JFFaceBook():

        group_id = "it.jobs.croatia"
        page_url = "https://mobile.facebook.com/groups/" + group_id
        '''page_content = ""'''
        page_content = requests.get(page_url).text

        soup = BeautifulSoup(page_content, "html.parser")
        feed_container = soup.find(id="m_group_stories_container").find_all("p")
        for i in feed_container:
            print(i.text)
            print(i.link)
            print()


