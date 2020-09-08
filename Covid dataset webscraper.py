from selenium import webdriver
import os,time
import pandas as pd
#create an empty 2d data frame
df=pd.DataFrame(columns=['Rank','Country','Total Case','New Cases','Deaths','New Deaths','Recovered','Active Cases','Critical'])
print(df)
browser=webdriver.Chrome('C:\\Users\\chromedriver.exe')
browser.get("https://www.worldometers.info/coronavirus/")
time.sleep(20)
#Acquring elements of table rows
#Navigating through each row 
for i in browser.find_elements_by_xpath('//table[@id="main_table_countries_today"]/tbody/tr'):
	#Acquring elements of td(data) from each row
	td_list=i.find_elements_by_tag_name('td')
	#creating a list for appending each data value as a column in one row
	row=[]
	#Acquring and appending the data values from each td through navigation of all td's in a row
	for td in td_list:
		row.append(td.text)
	#creating a dictionary for mapping each column head(feature) with its data element(i.e td data)
	data={}
	#Navigation through all td data and mapping it with features of table
	for j in range(len(df.columns)):
		data[df.columns[j]]=row[j]
	#Appending it to the 2D data frame as one row
	df=df.append(data,ignore_index=True)
df=df[1:]
path='C:\\Users\\\\Project (covid dataset_webscraping)'
path1=os.path.join(path,'Covid_dataset.csv')
df.to_csv(path1,index=False)
print('done')


