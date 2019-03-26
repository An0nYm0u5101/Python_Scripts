import requests, logging, sys, os
from bs4 import BeautifulSoup

#Defining arrays
lists = []
garbageUrlList=[]

#Defining functions
def debug():
    print('Debug is on!')
    # These two lines enable debugging at httplib level (requests->urllib3->http.client)
    # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
    # The only thing missing will be the response.body which is not logged.
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1
    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

def getRequests(query):
    r = requests.get("https://www.youtube.com/results?search_query=" + query)
    if r.status_code != 200:
            print("Response code is showing " + str(r.status_code) + '\nMaybe try debug it?')
            sys.exit()
    soup = BeautifulSoup(r.text, 'html.parser')
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        urls = ('https://www.youtube.com' + vid['href'])
        garbageUrlList.append(urls)
        break

def getResults(arrays):
        number = 1
        for i in arrays:
                print(str(number) + ': ' + i)
                number += 1
        print('')

def getSongs(url):
    print('Connecting to ' + url)
    r = requests.get(url)
    if r.status_code != 200:
            print("Response code is showing " + str(r.status_code) + '\nMaybe try debug it?')
            sys.exit()
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all("h2", {"class": "chart-listing--song"}):
            lists.append(link.string)

#Main function
if "__main__" == __name__:
    if "--debug" in sys.argv:
        debug()

getSongs('https://hitz.com.my/charts/hitz-30-chart')
print('\nPrinting available songs...')
getResults(lists)
print('Connecting to YouTube..')
for songs in lists:
    getRequests(songs)
print('Connection succeeded!\n')
print('Querying URLs for above songs..')
for urls in garbageUrlList:
        print (urls)
        os.system('./app.sh %s' % (urls))