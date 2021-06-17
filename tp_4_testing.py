# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

def __init__():
    pass

# %%
def obtener_tercer_resultado_google(query):
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox(executable_path='/home/julian/Documents/ML_Projects/Testing/Testing_TP4/geckodriver', options=opts)

    links = [] 

    url = "http://www.google.com/search?q=" + query + "&start=" +  '1'
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    search = soup.find_all('div', class_="yuRUbf")
    for h in search:
        links.append(h.a.get('href'))

    link_de_interes = links[2]

    browser.close()

    return link_de_interes


# %%



