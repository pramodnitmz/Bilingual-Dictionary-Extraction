import requests
from bs4 import BeautifulSoup
# base_url="https://en.wikipedia.org"
c=0
h=0
e=0
limit=10
def find_hindi_url(en_url):
    r=requests.get(en_url)
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    hindi_url=(soup.find("a",{"lang":"hi"})).get('href')
    return hindi_url


# def find_all_url(en_url):
#     r = requests.get(en_url)
#     c = r.content
#     soup = BeautifulSoup(c, "html.parser")
#     all = soup.find_all("div", {"class": "mw-body-content"})
#     for div in all:
#         aall=div.find_all("a",{"class":"mw-redirect"})
#         for a in aall:
#             sub_url=a.get('href')
#             try:
#                 full_url = base_url + sub_url
#                 print(full_url)
#             except:
#                 pass

def print_hindi_content(url):
    global h
    fw=open(str(h)+"_hindi.txt","w")
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "mw-body-content"})
    for div in all:
        pall = div.find_all("p")
        for p in pall:
            fw.write(p.text)
    h=h+1
    print(h)
    fw.close()

def print_english_content(url):
    global e
    fw=open(str(e)+"_eng.txt","w")
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "mw-body-content"})
    for div in all:
        pall = div.find_all("p")
        for p in pall:
            fw.write(p.text)
    e=e+1
    fw.close()


def crowl_hind_eng(url):
    try:
        h_url=find_hindi_url(url)
        if(h_url):
            print_english_content(url)
            print_hindi_content(h_url)
            c=c+1
    except:
        pass


    
def print_hindi_content(url):
    global h
    fw=open(str(h)+"_hindi.txt","w")
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "mw-body-content"})
    for div in all:
        pall = div.find_all("p")
        for p in pall:
            fw.write(p.text)
    h=h+1
    fw.close()

def print_english_content(url):
    global e
    fw=open(str(e)+"_eng.txt","w")
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "mw-body-content"})
    for div in all:
        pall = div.find_all("p")
        for p in pall:
            fw.write(p.text)
    e=e+1
    fw.close()


def crowl_hind_eng(url):
    print_english_content(url)
    h_url=find_hindi_url(url)
    print_hindi_content(h_url)
    
def crowl_infinit(url):
	global c
	crowl_hind_eng(url)
	r = requests.get(url)
	c = r.content
	soup = BeautifulSoup(c, "html.parser")
	all = soup.find_all("div", {"class": "mw-body-content"})
	for div in all:
		aall=div.find_all("a",{"class":"mw-redirect"})
		for a in aall:
			 sub_url=a.get('href')
			 try:
			 	full_url=(r"https://en.wikipedia.org"+sub_url)
			 	crowl_hind_eng(full_url)
			 	# print(full_url)
			 except:
			 	pass

crowl_infinit("https://en.wikipedia.org/wiki/Wikipedia")	




