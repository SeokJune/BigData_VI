# T-SA.py
#     Title: Main for T-SA
#    Author: Lee SeokJune
# --------------------------------------------------------------------------------------------------
# import module
# --------------------------------------------------------------------------------------------------
# Class that implement functions related to Twitter API
## pip install 
import TwitterAPI
# Class that implement functions related to DataBase
## pip3 install pymysql
import DBModule
# Class that implement functions related to Visualization
##
import Visualization
# --------------------------------------------------------------------------------------------------
# Set Parameter(Twitter)
# --------------------------------------------------------------------------------------------------
# Setting Parameters realted to KEY: consumer_key, consumer_secret, label
paramAPI = (('lNZwPI2dQ5l89K1nOGW6Sod6u', 'D6eGld20D99yrL89SMYPhJsjiHqmNKGL5LznkNKOQQPoIoQxWA', 'TSA0'),
            ('MGRK5IsX8xwxhz0FYv5Llm5ps', 'JRh3fHqPqEq6VWcyoKax6MG4nE21z0zatiDjEGnvmHm99cyrLA', 'TSA1'))
# Setting Parameters related to SearchAPI: query, date(from, to), maxResults
## Query length: Sandbox - 128 characters, Premium - 1024 characters
query = '"문재인" OR "홍준표" OR "안철수" OR "유승민" OR "심상정"'
## date(from, to): Sandbox - Full history, Premium - Full history
date = ('201901010000', '201912310000')
## Tweets per request: Sandbox - 10~100, Premium - 10~500
maxResults = 100
# Setting Parameters related to Timeline: code(user_id, screen_name), count
## code(user_id - , screen_name - Name starting with '@')
code = ('Lee SeokJune','LSeokjune')
## Specifies the number of Tweets to try and retrieve: ~200
count = 100
## false - Timeline will strip any native retweets
include_rts = False
# --------------------------------------------------------------------------------------------------
# Set Parameter(DB)
# --------------------------------------------------------------------------------------------------
# Setting Parameters realted to DB Connect: HostIP, UserID, Password, DB Name, encoding Character Type
paramDB = ('localhost', 'T-SA', '1234', 'TWITTER', 'utf8')
# Table list
tableName = ('S_JSON', 'S_HASHTAG', 'S_USER','T_JSON', 'T_HASHTAG', 'T_USER','KEYWORD_COUNT', 'HASHTAG_COUNT')
# --------------------------------------------------------------------------------------------------
# Creating 'TwitterAPI', 'dbModule' object
# --------------------------------------------------------------------------------------------------
# 'TwitterAPI' object
#twitter = TwitterAPI.TwitterAPI('https://api.twitter.com/')
# 'DBModule' object
db = DBModule.DBModule(paramDB[0],paramDB[1],paramDB[2],paramDB[3],paramDB[4])
# 'Bisualization' object
visual = Visualization.Visualization()
# --------------------------------------------------------------------------------------------------
# Operating Part
# --------------------------------------------------------------------------------------------------
# Output Title list
Choise = (('Twitter',
            'Search', 'Timeline'),
            ('DataBase',
            'Insert(Search)', 'Insert(Timeline)',
            'Delete(Search)', 'Delete(Timeline)', 'Delete(KeywordCount)', 'Delete(HashtagCount)',
            'Back-Up(ALL)', 'Roll-Back(ALL)'),
            ('Visualization(Base)',
            'Line Graph', 'Word Cloud', 'Bar Graph', 'Stacked Bar Graph', 'Pie Graph'),
            ('Visualization(Analysis)',
            'Bar Graph', 'Stacked Bar Graph', 'Pie Graph'))
# --------------------------------------------------------------------------------------------------
while True:
    # ----------------------------------------------------------------------------------------------
    # 1. Twitter
    #     11. Search
    #     12. Timeline
    # 2. DataBase
    #     21. Insert(Search)
    #     22. Insert(Timeline)
    #     23. Delete(Search)
    #     24. Delete(Timeline)
    #     25. Delete(KeywordCount)
    #     26. Delete(HashtagCount)
    #     27. Back-Up(ALL)
    #     28. Roll-Back(ALL)
    # 3. Visualization(Base)
    #     31. Line Graph
    #     32. Word Cloud
    #     33. Bar Graph
    #     34. Stacked Bar Graph
    #     35. Pie Graph
    # 4. Visualization(Analysis)
    #     41. Bar Graph
    #     42. Stacked Bar Graph
    #     43. Pie Graph
    # 5. Exit
    # ----------------------------------------------------------------------------------------------
    # Output Title
    # ----------------------------------------------------------------------------------------------
    for x in range(0, len(Choise)):
        for y in range(0, len(Choise[x])):
            if y == 0:
                print('%s.%s' % (x + 1, Choise[x][y]))
            else:
                print('\t%s%s.%s' % (x + 1, y, Choise[x][y]))
    print('%s.EXIT' % str(len(Choise) + 1))
    print('Choice Number(XX) >>>')
    # ----------------------------------------------------------------------------------------------
    # Input Number
    # ----------------------------------------------------------------------------------------------
    cNum = input()
    # ----------------------------------------------------------------------------------------------
    # Input Number Check(5) - EXIT
    # ----------------------------------------------------------------------------------------------
    if cNum == '5':
        print('EXIT!!')
        break
    # ----------------------------------------------------------------------------------------------
    # Twitter - Search
    # ----------------------------------------------------------------------------------------------
    if cNum == '11':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Twitter - Timeline
    # ----------------------------------------------------------------------------------------------
    elif cNum == '12':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Insert(Search)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '21':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Insert(Timeline)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '22':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(Search)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '23':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(Timeline)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '24':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(KeywordCount)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '25':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(HashtagCount)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '26':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Back-Up(ALL)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '27':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Roll-Back(ALL)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '28':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Search
    # ----------------------------------------------------------------------------------------------
    elif cNum == '31':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Line Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '32':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Word Cloud
    # ----------------------------------------------------------------------------------------------
    elif cNum == '33':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '34':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Stacked Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '35':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '41':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Stacked Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '42':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Pie Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '43':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Input Number is not (11, 12, 21, 22, 23, 24, 25, 26, 27, 28, 31 ,32, 33, 34 ,35 ,41, 42, 43)
    # ----------------------------------------------------------------------------------------------
    else:
        # ------------------------------------------------------------------------------------------
        print('Re-enter')
        # ------------------------------------------------------------------------------------------
        continue
        # ------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
