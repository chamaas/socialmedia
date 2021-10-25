import scrapy
import pandas as pd
import time
from socialmedia.spiders import DATA_FILE, GOOGLE_PREFIX,BOOK_DIR, SEARCH_ENGINE_DATA,PROXIS_FILE



def get_link(key):
        """
        build google's query
        """
        df= pd.read_excel(DATA_FILE)
        df = df.astype({"TITRE": str})
        titres=df['TITRE'].values[:]
        links=[]
        for i in range(len(titres)):
            titre=titres[i]
            query=titre.replace(' ','+')+"+babelio"
            url_search =f"{SEARCH_ENGINE_DATA[key]['prefix']}+{query}"
            links.append(url_search)
        return links[1:5]


def first_result_hashtag(driver,query):
    search_bar=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    search_bar.clear()
    search_bar.send_keys(query)
    time.sleep(2)
    search_results=driver.find_elements_by_class_name("-qQT3")
    time.sleep(3)
    links=[]
    for search_result in search_results:
         link=search_result.get_attribute('href')
         if "/explore/tags/" in link:
             links.append(link)
    return 


def is_book(search_result):
    
    try:
        if BOOK_DIR in search_result:
            return True 
    except:
        print("Babelio page not found")
        pass

def query():
    df=pd.read_excel(DATA_FILE)
    df = df.astype({"TITRE": str})
    titres=df['TITRE'].values[:]
    links=[]
    for i in range(len(titres)):
        titre=titres[i]
        if "(" in titre :
           titre = titre.split("(")[0]
        if "," in titre :
            titre = titre.split(",")[0]
        titre = titre.replace("-"," ")
        titre= titre.replace("'"," ")
        titre= titre.replace(":"," ")
        titre= titre.replace("é","e")
        titre= titre.replace("ê","e")
        titre= titre.replace("è","e")
        titre= titre.replace("â","a")
        titre= titre.replace("î","i")
        titre= titre.replace("?","")
        titre= titre.replace("!","")
        titre= titre.replace("."," ")
        titre= titre.replace("ã","")
        titre= titre.replace("à","")
        titre= titre.replace('"',"")
        titre= titre.replace("/","")
        titre = titre.replace("«","")
        titre = titre.replace("»","")
        titre = titre.replace("°","")
        titre = titre.replace("%","")
        titre = titre.replace("’"," ")
        query="#" + titre
        links.append(query)

    return links

def proxis(PROXI_FILE):
    x = []
    with open(PROXI_FILE) as file:
        for l in file:
            x.append(l.strip())
    return x


def get_get_selenium_value(driver,css):
    element = driver.find_elements_by_css_selector(css)
    if element : 
        return element[0].text
    else :
        return None


def login(driver,username,password):
    username_bar=driver.find_element_by_css_selector("div > div:nth-child(1) > div > label > input")
    password_bar=driver.find_element_by_css_selector("div > div:nth-child(2) > div > label > input")
    username_bar.send_keys(username)
    time.sleep(1)
    password_bar.send_keys(password)
    time.sleep(2)
    login=driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
    login.click()
def logout(driver):
    time.sleep(2)
    profile = driver.find_element_by_css_selector('section > nav > div > div > div > div > div > div:nth-child(5) > span')
    driver.execute_script("arguments[0].click();", profile)                           
    time.sleep(1) 
    logout_button=driver.find_element_by_css_selector('section > nav > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div > div:nth-of-type(5) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div > div')                                                  
    driver.execute_script("arguments[0].click();", logout_button)  

def search_query(driver,query):
    """
    search hashtag
    """
    search_bar=driver.find_element_by_css_selector("section > nav > div > div > div > div > input")
    search_bar.clear()
    search_bar.send_keys(query)
    time.sleep(1)

def get_results_hashtag(driver,query):
    """
    get link of hashtag
    """
    search_query(driver,query)
    search_results=driver.find_elements_by_class_name("-qQT3")
    links=[]
    for search_result in search_results:
        link=search_result.get_attribute('href')
        if "/explore/tags/" in link:
            links.append(link)
            if links :
               return links[0]
            
             

def get_post_rusult(driver,hashtags_livre,hashtags):
    time.sleep(2)
    for elem in driver.find_elements_by_class_name('xil3i'):
        hashtags_livre.append(elem.text)
    if len(set(hashtags_livre).intersection(set(hashtags)))>0:
        related='related post'  
    else:
        related='unrelated post'   
    date_pub = driver.find_element_by_css_selector(' div.k_Q0X.I0_K8.NnvRN > a > time').get_attribute("datetime")
    likes=driver.find_element_by_css_selector('section > div > div > a > span').text
    description=driver.find_element_by_css_selector('article > div > div > ul > div > li > div > div > div > span').text
    return date_pub,likes,description,related
    
    """
    item["url"] = url_hash 
    item["post_link"]=driver.current_url
    item["Likes"]=likes
    item["date_pub"]=str(date_pub).split("T")[0]
    item['description']=description.replace("\n","").replace("\t","")
    """