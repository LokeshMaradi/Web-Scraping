import urllib.request as u
from bs4 import BeautifulSoup as b
import pandas as pd,time
pages=int(input('Enter number of pages:'))
for i in range(pages):
	url='https://news.ycombinator.com/news?p='+str(i+1)
	page=u.urlopen(url)
	soup=b(page,'html.parser')
	anchors=soup.find('table',{'class':'itemlist'}).findAll('a',{'class':'storylink'})
heads=[]
links=[]
for i in anchors:
	text=i.text
	link=i.get('href')
	heads.append(text)
	links.append(link)
dic={'Headline':heads,'links':links}
df=pd.DataFrame(dic)
df.to_csv('C:\\Users\\New.csv',index=False)
print("Done3")




