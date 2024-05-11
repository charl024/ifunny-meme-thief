from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def setWebdriver(url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")

    session = webdriver.Chrome(options=options)
    session.get(url)

    #wait = WebDriverWait(session, 10)
    #login = session.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div/div")
    #log2 = login.get_attribute("innerHTML")
    #print(log2)    

    return session

def websiteLogin(session):
    
    return session

def soupSearch(pagesrc):
    soup = BeautifulSoup(pagesrc, 'html.parser')
    post = soup.find('div', class_='_3ZEF')

    if post is None:
        return "Empty"

    if post.find('img', src=True) is not None:
        src = post.find('img', src=True)
    else:
        src = post.find('video', src=True)

    if "https" not in src["src"]:
        link = src["data-src"]
    else:
        link = src["src"]
    
    return link

def ifunnySteal():
    url = 'https://ifunny.co/'
    session = setWebdriver(url)
    
    link = soupSearch(session.page_source)


    session.quit()
    return link
    
def main():
    print(ifunnySteal())
    #ifunnySteal()
main()   


