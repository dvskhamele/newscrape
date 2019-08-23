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


def scrapy():
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
		existsm = os.path.exists(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}')
		if existsm:
			pass
		else:
			os.mkdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}')

		existsm = os.path.exists(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}')
		if existsm:
			pass
		else:
			os.mkdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}')
		
		try:   
			for filename in os.listdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}\\'):
				if existsm:
					if filename.endswith(".csv"): 
						co=pd.read_csv(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}\\{filename}', delimiter = ',').values.tolist()
						#print("Current File",co)
						pd1=pd1+co
				else:
				   pass             

		except:
			pass
		if day1 == "1" or day1 == 1:
			
			for filename in os.listdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{lastmonths}\\{yesderdates}\\'):

				if filename.endswith(".csv"):
					co1=pd.read_csv(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{lastmonths}\\{yesderdates}\\{filename}', delimiter = ',').values.tolist()
					pd1=pd1+co1
		else:
			try:
				for filename in os.listdir(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{yesda}\\'):
					if filename.endswith(".csv"):
						co1=pd.read_csv(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{yesda}\\{filename}', delimiter = ',').values.tolist()
						pd1=pd1+co1
						#print("Old File",co1)
			except:
				pass
		if pd1 !=[] or pd1 !="":
			for j in pd1:
				for k in j:
					j1=pd2.append(k)
		i=0
		list = ["https://timesofindia.indiatimes.com/","https://aninews.in","https://indiatoday.in"]
		list = ["https://inshorts.com/en/read",]
		for links in list:
			if links != None or links != " ":
				response = requests.get(links)
				data = response.text        
				soup = BeautifulSoup(data,"html.parser")#.encode("utf-8")
				if soup != None or soup != " ":
					if links == "https://inshorts.com/en/read":
						article_links = soup.findAll('a', attrs={'href': re.compile("/articleshow/")})
						news_title="In Shorts"
					else:
						continue
					# if links == "https://timesofindia.indiatimes.com/":
					# 	article_links = soup.findAll('a', attrs={'href': re.compile("/articleshow/")})
					# 	news_title="The Times of India"
					# elif links == "https://aninews.in":
					# 	article_links = soup.findAll('a', attrs={'href': re.compile("/news/")})
					# 	news_title = "ANI NEWS"
					# elif links == "https://indiatoday.in" :
					# 	article_links = soup.findAll('a', attrs={'href': re.compile("/story/")})
					# 	news_title="India Today"
					#print("article_links",len(article_links))
					for link in article_links:
						link1=link.get('href')      
						if not "http://" in link1 and not "https://" in link1:
							if "/" == link1[1:] :
								link1=link1[1:]
								link2=links+link1
								#print(link2)
								url = link2
								print("url",url)
								continue
							else:
								link2=links+link1
								#print(link2)
								url = link2
								print("url",url)
								continue
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
									article.parse()
									today = datetime.date.today()
									dow_time = datetime.datetime.now().time()
									auther=article.authors
									#print("article writer",auther)
									title=article.title
									titles=title.replace(";", ",")
									#print("article title : ",title)
									text=article.text
									texts=text.replace(";", ",")
									#print("article content : ",text)
									image_url=article.top_image
									#print("article image link: ",image_url)
									down_Date=today
									#print("article download date :", down_Date)
									d = articleDateExtractor.extractArticlePublishedDate(url)
									publish_date=d
									#print("Publish date",publish_date)
									try:
										publish_date1=[publish_date.day,publish_date.month,publish_date.year]
										publish_date1 = str(publish_date1)
										publish_date1 = publish_date1.replace(",", "-")
										publish_date1 = publish_date1.replace("[", " ")
										publish_date1 = publish_date1.replace("]", " ")
										publish_time1=[publish_date.hour,publish_date.minute]
										publish_time1  = str(publish_time1)
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
				
									with open(f'C:\\Users\\ankit\\Desktop\\ArticleProject\\Excel_File\\{mon}\\{day}\\{filename}', 'a') as csv_file:
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
	 


scrapy()