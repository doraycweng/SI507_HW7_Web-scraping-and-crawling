# 507/206 Homework 7 Part 1
import requests
import json
from bs4 import BeautifulSoup

CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

except:
    CACHE_DICTION = {}

def get_unique_key(url):
  return url  

def make_request_using_cache(url):
    
    global header
    unique_ident = get_unique_key(url)

    if unique_ident in CACHE_DICTION:
        return CACHE_DICTION[unique_ident]

    else:
        header = {'User-Agent': 'SI_CLASS'}
        resp = requests.get(url, headers=header)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() 
        return CACHE_DICTION[unique_ident]

#### Your Part 1 solution goes here ####
def get_umsi_data(page):
    #### Implement your function here ####
    # pass
    person_dic = {}
    baseurl = 'https://www.si.umich.edu'
    directory_url = baseurl + '/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All&page=' + str(page)
    header = {'User-Agent': 'SI_CLASS'}
    page_text = make_request_using_cache(directory_url)
    page_soup = BeautifulSoup(page_text, 'html.parser')
    div_views = page_soup.find_all(class_='views-row')

    for i in range(len(div_views)):
    	name = div_views[i].find(class_='field-name-title').text
    	title = div_views[i].find(class_='field-name-field-person-titles').text
    	details_url_end = div_views[i].find(class_='field-name-contact-details').find('a')['href']
    	details_url = baseurl + details_url_end
    	page_detail = make_request_using_cache(details_url)
    	page_detail_soup = BeautifulSoup(page_detail, 'html.parser')
    	email = page_detail_soup.find(class_='field-name-field-person-email').find(class_='field-items').text
    	person_dic[name] = {"title": title , "email": email }

    return person_dic


#### Execute funciton, get_umsi_data, here ####
umsi_titles = {}
for i in range(14):
	umsi_titles.update(get_umsi_data(i))

print(len(umsi_titles)) 

#### Write out file here #####
dumped_directory = json.dumps(umsi_titles, indent=2)
fw = open('directory_dict.json', 'w')
fw.write(dumped_directory)
fw.close()
