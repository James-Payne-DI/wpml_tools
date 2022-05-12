from bs4 import BeautifulSoup
import requests, time, urllib3, csv, os


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
        
        heading = str(elem.h2.text)
        print(heading)
        
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


    createCSV(translationList)
        



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

    print("Data Added to File")


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
def findPageTitle(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    pageTitle = soup.find('h1').text
    pageTitle = pageTitle.replace("\n","").strip()
    return(str(pageTitle))



def findCounterpart(spaContent):
    #^parameter is an array, below splits first two elements and assigns them to variables
    spaTitle = str(spaContent[0])
    spaUrl = str(spaContent[1])

    spaSlug = splitLink(spaUrl)
    
    source = requests.get(spaUrl).text
    soup = BeautifulSoup(source,'lxml')


    #define local variables
    engUrl = None
    engSlug = None
    engTitle = None

    #Tries to find the URL for the language toggle button
    try:
        engUrl = soup.find('a',{"class":"lang_opposite"}).get('href')
        engSlug = splitLink(str(engUrl))
    except:
        engUrl = False
        engSlug = "Error - With Finding the English Url"

    #Finds the Title from the English Page
    try:
        engTitle = findPageTitle(engUrl)
    except:
        engTitle = "Error - With Finding the English Page Title"
    

    counterpartList = [engTitle,engSlug,spaTitle,spaSlug]
    print(counterpartList)
    return counterpartList
    

def splitLink(url):
    elem = str(url)
    splitUrl = elem.split('.com')
    slug = str(splitUrl[1])
    return slug

    
#TESTING: please comment out when not in use
#https://maxwellford-wpml0522.dev.dealerinspire.com/es/mapa-del-sitio/
url = input("Please paste the Sitemap URL here: ")
spanishSitemap(url)
