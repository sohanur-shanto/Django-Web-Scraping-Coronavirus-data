from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests


def get_html_content(request):
    
    city = request.GET.get('city')
    city = city.replace(" ", "/")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.worldometers.info/coronavirus/country/{city}').text
    return html_content


def home(request):
    result = None
    if 'city' in request.GET:
        # fetch the weather from Google.
        html_content = get_html_content(request)
       
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()
        # extract region
        result['region'] = soup.find("div", attrs={"id": "maincounter-wrap"}).text
        # extract temperature now
        # result['temp_now'] = soup.find("div", attrs={"class": "number-table-main"}).text
        # get the day, hour and actual weather
        # result['dayhour'], result['weather_now'] = soup.find("div", attrs={"id": "maincounter-wrap"}).text          
         
    return render(request, 'home.html', {'result': result})

















###Scraping pictures from website


# from django.shortcuts import render
# import requests
# import bs4

# def index(request):
# 	val = []
# 	if request.method == 'POST':
# 		form = request.POST['your_url']
# 		resp = requests.get(form)
# 		scrapval = bs4.BeautifulSoup(resp.text,"html.parser")
# 		for data in scrapval.find_all('img'):
# 			srcval = data.get('src')
# 			print(srcval)
# 			val.append(srcval)

# 	return render(request,'home.html',{'value':val})
