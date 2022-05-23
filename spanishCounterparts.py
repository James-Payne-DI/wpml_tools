from bs4 import BeautifulSoup
import requests, time, urllib3, csv, os
from tkinter import filedialog

def spanishSitemap(sitemapUrl):
    #clean the input
    sitemapUrl = str(sitemapUrl)

    #different way to accomplish the above ^
    source = requests.get(sitemapUrl).text
    soup = BeautifulSoup(source,'lxml')
    

    #Sections on Spanish Sitemap (can be removed)
    paginas = ''
    publicaciones = ''
    vehiculosNuevos = ''
    vehiculosUsados = ''


    #Lists Defined here - used to aggregate data
    espLinks = []
    translationList = []

    outer_elements = soup.find_all('li',{"class":"pagenav"})
##    print(outer_elements)

    for elem in outer_elements:
##        print(elems)

        #finds linked h2 tags 
        header = find_parent_tag(elem)
        
        if (header[1].find('urlError01') != -1):
            print ("urlError01 detected - skipping")
        else:
            espLinks.append(header)
        
        li_elements = getListElements(elem)

        #scans all li elements on spanish sitemap, adds them to the list
        for item in li_elements:
            
            #define local variables
            childList = None
            linkText = item.text
            linkUrl = None
            parent = False
            
            #check for child elements
            try:
                newList = getListElements(item)
                if newList:
                    parent = True
                    print("<---Parent Element--->")
                    #cleans link text of parent elements to be safe
                    linkText = cleanParentText(linkText)
                    try:
                        #if parent element is found it gets added to the list
                        linkUrl =  str(item.a.get('href'))
                        espLinks.append([linkText,linkUrl])
                        parent = False
                    except:
                        linkUrl = "CONNECTIONN ISSUE - parent element"
                        espLinks.append([linkText,linkUrl])
                        parent = False
            except:
                try:
                    linkUrl =  str(item.a.get('href'))
                    espLinks.append([linkText,linkUrl])
                except:
                    linkUrl = "CONNECTIONN ISSUE"
                    espLinks.append([linkText,linkUrl])


    #goes through the list of Spanish Links and finds their counterparts
    for content in espLinks:
        counterparts = findCounterpart(content)

        #adds the data for this slug as a list of Arrays in 'translationList'
        translationList.append(counterparts)


    #createCSV(translationList)
    return translationList
        



#creates a .csv file on the Desktop and exports the data there
def createCSV(translationList):
    
    translations_csv = open("translation_list.csv", "x")
    print("file created & opened")
    translations_csv.close()

    with open('translation_list.csv', mode='w') as translation_list:
        
        translation_writer = csv.writer(translation_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        field_names = ["English Title","English Slug","Spanish Title","Spanish Slug"]
        translation_writer.writerow(field_names)
        
        for translation in translationList:
            translation_writer.writerow(translation)

    #trying to  open file dialog
    #saveFile()
    print("Data Added to File")


def saveFile():
    root = Tk()
    root.withdraw()
    file =  filedialog.askaveasfile(defaultextension=".csv")


#Function: pulls down sitemap and returns a soup element
def makeSoup(html):
    soup = BeautifulSoup(source,'lxml')
    return soup

def innerList(engTitle,engSlug,spaTitle,spaSlug):
    newList = [str(engTitle),str(engSlug),str(spaTitle),str(spaSlug)]
    return newList

def addToBigList(bigList,smallList):
    newList = bigList.append(smallList)
    return newList


#Tests the string and tells us what to do with the list
def clearLinks(linkList):
    linkList = []
    return linkList

#Returns the Response Code of a URL
def getResponseCode(url):
    request_response = requests.get(link)
    link_status = request_response.status_code
    print(url)
    print("Response Code: " + str(link_status))
    return link_status

def getListElements(soup):
    elem = soup
    ul_element = elem.ul
    li_elements = ul_element.find_all('li')

    #returns a list of the <li> elements in the given <ul> tag
    return li_elements


#finds the first h1  tag for a given url and returns it as a string
def find_header_tag(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    pageTitle = soup.find('h1').text
    pageTitle = pageTitle.replace("\n","").strip()
    return(str(pageTitle))

#finds the first h1  tag for a given url and returns it as a string
def find_page_title(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    pageTitle = soup.find('title').text
    pageTitle = pageTitle.replace("\n","").strip()
    return(str(pageTitle))


#detects the <h2> elements and checks for a link - returns a list w/ 2 items
def find_parent_tag(soup):
    elem = soup
    try:
        headingText = str(elem.h2.text).replace("\n","").strip()
        headingLink = str(elem.h2.a.get('href'))
        print([headingText,headingLink])
        return [headingText,headingLink]
    except:
        headingText = str(elem.h2.text).replace("\n","").strip()
        headingLink = "urlError01: No Link within element"
        print([headingText,headingLink])
        return [headingText,headingLink]


def findCounterpart(spaContent):
    #^parameter is an array, below splits first two elements and assigns them to variables
    spaTitle = str(spaContent[0])
    spaUrl = str(spaContent[1])
    #define local variables
    engUrl = None
    engSlug = None
    engTitle = None

    #gets the spanish slug for this page
    spaSlug = splitLink(spaUrl)

    
    source = requests.get(spaUrl).text
    soup = BeautifulSoup(source,'lxml')

    #Tries to find the URL for the language toggle button
    try:
        engUrl = soup.find('a',{"class":"lang_opposite"}).get('href')
        engSlug = splitLink(str(engUrl))
    except:
        engUrl = False
        engSlug = "urlError02: unable to locate multilingual page toggle"

    #Tries to find the Title from the English Page
    try:
        engTitle = find_header_tag(engUrl)
    except:
        try:
            engTitle = find_page_title(engUrl)
        except:
            engTitle = "titleError01: - Could Not Find Page Title"
    

    counterpartList = [engTitle,engSlug,spaTitle,spaSlug]
    print(counterpartList)
    return counterpartList


def cleanParentText(parent):
    elem = parent.split('\n')
    elem = str(elem[0])
    parentText = elem.replace("\n","").strip()
    return parentText

def splitLink(url):
    elem = str(url)
    splitUrl = elem.split('.com')
    slug = str(splitUrl[1])
    return slug

    
#TESTING: please comment out when not in use
#https://maxwellford-wpml0522.dev.dealerinspire.com/es/mapa-del-sitio/
##url = input("Please paste the Sitemap URL here: ")
##spanishSitemap(url)
