from newspaper import Article
from datetime import date
import articleDateExtractor
import re
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import csv
import os
import xlrd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import glob
from openpyxl import Workbook
#import scrapy
import requests
from time import sleep
from newspaper.article import ArticleException, ArticleDownloadState
import calendar
from datetime import datetime, timedelta
import datetime
from time import gmtime, strftime
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from django.http import HttpResponse
from django.template import loader
from rest_framework.renderers import TemplateHTMLRenderer
from time import gmtime, strftime


def scrapy(request):
    if request.method == 'POST':
        #if request.method == 'POST': 
        recommendations=request.POST.getlist("Sites")
        print("recommendations",recommendations)

        pd1=[[],]
        pd2=[]
        now = datetime.datetime.now()
        x = datetime.datetime.now()
        x1=now.year
        today = datetime.date.today()
        mon1 = x.strftime("%b")
        mon=mon1+str(x1)
        day1=now.day
        d=day1
        day=str(day1)+mon1
        first = today.replace(day=1)
        lastmonth=first - datetime.timedelta(days=1)
        lastmonth=lastmonth.strftime("%b")
        lastmonths=lastmonth+str(x1)
        yesderdate=datetime.datetime.strftime(x - timedelta(1), '%d')
        yesderdates=str(yesderdate)+lastmonth
        yesda=str(yesderdate)+mon1
        ct=strftime("%I:%M %p")
        #existsm = os.path.exists(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}')
        existsm = os.path.exists(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}')
        if existsm:
            pass
        else:
            #os.mkdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}')
            os.mkdir(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}')

        existsm = os.path.exists(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}/{day}')
        #existsm = os.path.exists(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}')
        if existsm:
            pass
        else:
            #os.mkdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}')
            os.mkdir(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}/{day}')
        
        try:   
            #for filename in os.listdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}\\'):
            for filename in os.listdir(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}/{day}/'):
                if existsm:
                    if filename.endswith(".csv"): 
                        #co=pd.read_csv(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}\\{filename}', delimiter = ',').values.tolist()
                        co=pd.read_csv(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}/{day}/{filename}', delimiter = ',').values.tolist()
                        #print("Current File",co)
                        pd1=pd1+co
                else:
                   pass             

        except:
            pass
        if day1 == "1" or day1 == 1:
            for filename in os.listdir(f'/home/admin-pc/Desktop/Article/Scrapy/{lastmonths}/{yesderdates}/'):
            #for filename in os.listdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{lastmonths}\\{yesderdates}\\'):

                if filename.endswith(".csv"):
                    #co1=pd.read_csv(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{lastmonths}\\{yesderdates}\\{filename}', delimiter = ',').values.tolist()
                    co1=pd.read_csv(f'/home/admin-pc/Desktop/Article/Scrapy/{lastmonths}/{yesderdates}/{filename}', delimiter = ',').values.tolist()
                    pd1=pd1+co1
        else:
            try:
                for filename in os.listdir(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}/{yesda}/'):
                #for filename in os.listdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{yesda}\\'):
                    if filename.endswith(".csv"):
                        co1=pd.read_csv(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}/{yesda}/{filename}', delimiter = ',').values.tolist()
                        #co1=pd.read_csv(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{yesda}\\{filename}', delimiter = ',').values.tolist()
                        pd1=pd1+co1
                        #print("Old File",co1)
            except:
                pass
        if pd1 !=[] or pd1 !="":
            for j in pd1:
                for k in j:
                    j1=pd2.append(k)
        i=0
        #list = ["https://www.engadget.com/","https://www.espn.in/","https://www.vccircle.com/","https://www.aljazeera.com/","https://www.foxnews.com/","https://edition.cnn.com/","https://www.theguardian.com/international","https://www.financialexpress.com/","https://economictimes.indiatimes.com/", "https://www.economist.com/","https://www.bbc.com/", "https://www.digitaltrends.com/","https://www.theverge.com/", "https://www.rvcj.com/" ,"https://techcrunch.com/","https://www.crictracker.com/cricket-news/","https://zeenews.india.com/","https://www.hindustantimes.com/","https://timesofindia.indiatimes.com/","https://www.timesnownews.com/","https://www.firstpost.com/tech","https://aninews.in","https://www.thehindu.com/","https://indiatoday.in","https://www.thequint.com/","https://inshorts.com/en/read","https://in.reuters.com/","https://indianexpress.com/","https://www.livemint.com/",]
        # list = recommendations
        for links in recommendations:
            if links != None or links != " ":
                response = requests.get(links)
                data = response.text        
                soup = BeautifulSoup(data,"html.parser")#.encode("utf-8")
                print()
                print()
                print()
                print()
                
                if soup != None or soup != " ":
                    if links == "https://timesofindia.indiatimes.com/":
                        article_links = soup.findAll('a', attrs={'href': re.compile("/articleshow/")})[0:10]
                        news_title="The Times of India"
                    elif links == "https://aninews.in":
                        article_links = soup.findAll('a', attrs={'href': re.compile("/news/")})[0:10]
                        news_title = "ANI NEWS"
                    elif links == "https://indiatoday.in" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/story/")})[0:10]
                        news_title="India Today"
                    elif links == "https://www.thequint.com/entertainment" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/entertainment/")})[0:10]
                        news_title="The Quint"
                    elif links == "https://inshorts.com/en/read" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/news/")})[0:10]
                        news_title="In Shorts"
                    elif links == "https://in.reuters.com/" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/article/")})[0:10]
                        news_title="Reuters India"
                    
                    elif links == "https://indianexpress.com/" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/article/")})[0:10]
                        news_title="Indian Express"
                    
                    elif links == "https://www.thehindu.com/" :
                        article_links = soup.findAll('a', attrs={'href': re.compile(".*//.*/.*/.*/.*")} )[0:10]
                        news_title="The Hindu"
                    
                    elif links == "https://www.firstpost.com/tech" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/tech/")})[0:10]
                        news_title="Firstpost"
                    elif links == "https://www.timesnownews.com/" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/article/")})[0:10]
                        news_title="Times Now"
                    elif links == "https://www.pinkvilla.com/" :
                        article_links = soup.findAll('a', attrs={'href': re.compile("/entertainment/")})[0:10]
                        news_title="Pinkvilla"
                    elif links == "https://www.livemint.com/":
                        article_links = soup.findAll('section', attrs={'data-weburl': re.compile(".html")})[0:10]
                        news_title="Live Mint"
                    elif links == "https://www.hindustantimes.com/":
                        article_links = soup.findAll('a', attrs={'href': re.compile(".html")})[0:10]
                        news_title="Hindustan Times"
                    elif links == "https://zeenews.india.com/":
                        article_links = soup.findAll('a', attrs={'href': re.compile(".html")})[0:10]
                        news_title="Zee News India"
                    elif links == "https://www.crictracker.com/cricket-news/":
                        article_links = soup.findAll('a', attrs={'href': re.compile(".*-.*-")})[0:10]
                        news_title="CricTracker"
                    elif links == "https://techcrunch.com/":
                        article_links = soup.findAll('a')[0:20]
                        news_title="TechCrunch"
                    elif links == "https://www.rvcj.com/":
                        article_links = soup.findAll('a', attrs={'href': re.compile(".*-.*-")})[0:10]
                        news_title="RVCJ"
                    elif links == "https://www.theverge.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*//.*/.*/.*/.*/.*/.*")})))[0:10]
                        news_title="The Verge"
                    elif links == "https://www.digitaltrends.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*-.*-")})))[0:10]
                        news_title="Digital Trends"
                    elif links == "https://www.bbc.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*-.*")})))[0:10]
                        news_title="BBC"
                    elif links == "https://www.economist.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*/.*/.*")})))[0:10]
                        news_title="Economist"
                    elif links == "https://economictimes.indiatimes.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*/.*/.*")})))[0:10]
                        news_title="Economic Times"
                    elif links == "https://www.financialexpress.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*/.*/.*/.*")})))[0:10]
                        news_title="Financial Express"
                    elif links == "https://www.theguardian.com/international":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*/.*/.*/.*/.*")})))[0:10]
                        news_title="Guardian"
                    elif links == "https://edition.cnn.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*/.*/.*")})))[0:10]
                        news_title="CNN"
                    elif links == "https://www.foxnews.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*/.*/.*")})))[0:10]
                        news_title="Fox News"
                    elif links == "https://www.aljazeera.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href'})))[0:10]
                        news_title="Al Jazeera"
                    elif links == "https://www.vccircle.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href'})))[0:10]
                        news_title="VC Circle"
                    elif links == "https://www.engadget.com/":
                        article_links = list(set(soup.findAll('a', attrs={'href': re.compile(".*/.*/.*")})))[0:10]
                        news_title="EndGadget"
                    elif links == "https://www.espn.in/":
                        article_links = list(set(soup.findAll('a')))[0:10]
                        news_title="ESPN"

                    #print("article_links",len(article_links))
                    for link in article_links :
                        if links == "https://www.livemint.com/":
                            link1 = link.get("data-weburl")
                        else:
                            link1=link.get('href')
                        if link1 == None:
                            continue
                        elif len(link1) < len(links) + 5 or link1 == None or "/subscribe/" in link or "/login/" in link or "/register/" in link or "/sign-in/" in link or "/www.twitter.com" in link or "/www.facebook.com" in link or "/www.google.com" in link or "/plus.google.com" in link:
                            continue
                        elif "https://www.foxnews.com//www.foxnews.com/" in link1:
                            link1 = link1.replace("https://www.foxnews.com//www.foxnews.com/","https://www.foxnews.com/")
                        #link1=link.get('href')
                        #print("link1",link1)
                        elif (not "http://" in link1 and not "https://" in link1) or "https://www.hindustantimes.com/" in link1:
                            if "/" == link1[1:] :
                                link1=link1[1:]
                                link2=links+link1
                                url = link2
                                print("/ in ",url)
                            else:
                                if links in link1:
                                    link2=link1
                                else:
                                    link2=links+link1
                                #print(link2)
                                print("link2",link2)
                                url = link2.replace("//",'/').replace("http:/",'http://').replace("https:/",'https://')
                                print("/ not in ",url)
                                
                        else:
                            url=link1
                        if url in pd1 or url in pd2:
                            continue
                        else:
                            try:
                                pd1.append(url)
                                article = Article(url)
                                article.download()
                            except:
                                continue
                            article.html
                            try:
                                article.parse()
                            except:
                                continue
                            
                            today = datetime.date.today()
                            dow_time = datetime.datetime.now().time()
                            auther=article.authors
                            #print("article writer",auther)
                            title=article.title
                            title=title.replace(";", ",")
                            title=title.replace("’", " ")
                            print("title",title)
                            if title == None:
                                print("breakssssssssssssssssssss")
                                continue

                            if title.find("^Facebook$") == -1 or title.find("^reddit.com:$") == -1 or title.find("^linkedin$") == -1 or title.find("^Twitter$") == -1:
                                titles=title
                            else:
                                print("breakssssssssssssssssssss")
                                continue

                            print("article title : ",titles)
                            titles=titles.replace("‘", " ")
                            titles=titles.replace("-", " ")
                            titles=titles.replace("“", " ")
                            titles=titles.replace("”", " ")
                            text=article.text
                            texts=text.replace(";", ",")
                            texts=texts.replace("’", " ")
                            texts=texts.replace("‘", " ")
                            texts=texts.replace("-", " ")
                            texts=texts.replace("“", " ")
                            texts=texts.replace("”", " ")
                            #print("article content : ",text)
                            image_url=article.top_image
                            image_url=image_url.replace(";", ",")
                            image_url=image_url.replace("’", " ")
                            #print("article image link: ",image_url)
                            down_Date=today
                            #print("article download date :", down_Date)
                            d = articleDateExtractor.extractArticlePublishedDate(url)
                            publish_date=d
                            #print("Publish date",publish_date)
                            try:
                                publish_date1 = [publish_date.day,publish_date.month,publish_date.year]
                                publish_date1 = str(publish_date1)
                                publish_date1 = publish_date1.replace(",", "-")
                                publish_date1 = publish_date1.replace("[", " ")
                                publish_date1 = publish_date1.replace("]", " ")
                                publish_time1 = [publish_date.hour,publish_date.minute]
                                publish_time1 = str(publish_time1)
                                publish_time1 = publish_time1.replace(",",":")
                                publish_time1 = publish_time1.replace("["," ")
                                publish_time1 = publish_time1.replace("]"," ")
                            except:
                                publish_date1= ""
                                publish_time1 = ""
                            filename=(f'NewsArticle{ct}')
                            filename=filename.replace(":", "+")
                            filename=filename.replace(" ", "")
                            filename=filename+'.csv'
        
                            #with open(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}\\{filename}', 'a') as csv_file:
                            with open(f'/home/admin-pc/Desktop/Article/Scrapy/{mon}/{day}/NewsArticle{ct}.csv', 'a') as csv_file:
                                writer = csv.writer(csv_file)
                                if i==0:
                                    writer.writerow(["Headline", "Name of Site", "Article URL","Article Text","Image URL","Download date","Download Time","News Date(DD/MM/YYYY)","News Time(HH:MM)"])
                                else:
                                    wri=writer.writerow([str(titles.encode("utf-8"))[2:-1] ,str(news_title.encode("utf-8"))[2:-1],
                                                         str(url.encode("utf-8"))[2:-1],str(texts.encode("utf-8"))[2:-1],
                                                         str(image_url.encode("utf-8"))[2:-1], down_Date,dow_time, publish_date1,publish_time1])
                                i=i+1
                else:
                    continue
           
            else:
                continue        
     

    #return render(request, 'index.html',{})

    #sites_values=request.POST['Sites']
# if request.method == 'POST': 
#     recommendations=request.POST.getlist("Sites")
#     print("recommendations",recommendations)
       # return render(request, 'index.html')
    return render(request, 'index.html',{})













