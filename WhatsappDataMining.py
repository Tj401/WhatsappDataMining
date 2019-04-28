# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 23:18:17 2019

@author: kdandebo
"""
import pandas as pd
watsup_file = 'C:/Users/kdandebo/Desktop/HomelatoptoKarthiklaptop/Python/datasetforpractice/WhatsApp Chat - Shirin/_chat.txt'
file_data = open(watsup_file,'r', encoding="utf8")
df = file_data.read()

        
import re
# Get date
date_regex=re.compile(r'(\d+/\d+/\d+)')
date=date_regex.findall(df)
 
# Get time
time_regex=re.compile(r'(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])')
time=time_regex.findall(df)

# Get message words from list
mess_regex = re.compile(r'[a-zA-z]+')
mess = mess_regex.findall(df)
#list to dataframe
#mess = pd.DataFrame(mess)

#mess = ''.join(mess)

#freq words
freq = pd.Series(' '.join(mess).split()).value_counts()
freq


#freq = pd.DataFrame(freq)

#df=pd.DataFrame(data,columns=("Date","Time","User","Message"))
#col = ('Object','Freq')
#freq.columns = col;


freq.to_csv('C:/Users/kdandebo/Desktop/out2.csv')

