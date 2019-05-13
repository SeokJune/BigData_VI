# T-SA.py
#     Title: Main for T-SA
#    Author: Lee SeokJune
# --------------------------------------------------------------------------------------------------
# import module
# --------------------------------------------------------------------------------------------------
# Class that implement functions related to Twitter API
import TwitterAPI
# Class that implement functions related to DataBase
## pip3 install pymysql
import DBModule
# Class that implement functions related to Visualization
## pip3 install wordcloud
## pip3 install matplotlib
import Visualization
# OS related Module
import os
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
code = ('Lee SeokJune', 'LSeokjune')
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
tableName = ('S_JSON', 'S_HASHTAG', 'S_USER', 'T_JSON', 'T_HASHTAG', 'T_USER', 'KEYWORD_COUNT', 'HASHTAG_COUNT')
# --------------------------------------------------------------------------------------------------
# Result Parameter(Twitter, DB)
# --------------------------------------------------------------------------------------------------
sJson = ()
sHashtag = ()
sUser = ()
tJson = ()
tHashtag = ()
tUser = ()
keywordCount = ()
hashtagCount = ()
# --------------------------------------------------------------------------------------------------
# Set Parameter(Hadoop)
# --------------------------------------------------------------------------------------------------
paramSqoop = ['TWITTER', # DB Name
              'T-SA', # User Name
              '1234', # Password
              ['S_JSON', , , ], # Table List
              ['text', , , ], # Columns
              [['target-dir', 'KEYWORD_INPUT'], [, ], [, ], [, ]], # [target-dir/export-dir, Path]
              [['m', '1'], ['input-fields-terminated-by','"\t"']]]
# --------------------------------------------------------------------------------------------------
# Creating 'TwitterAPI', 'dbModule', 'Visualization' object
# --------------------------------------------------------------------------------------------------
# 'TwitterAPI' object
twitter = TwitterAPI.TwitterAPI('https://api.twitter.com/')
# 'DBModule' object
db = DBModule.DBModule(paramDB[0], paramDB[1], paramDB[2], paramDB[3], paramDB[4])
# 'Bisualization' object
visual = Visualization.Visualization()
# --------------------------------------------------------------------------------------------------
# Operating Part
# --------------------------------------------------------------------------------------------------
# Output Title list
Title = (('Twitter',
          'Search', 'Timeline'),
         ('DataBase',
          'Insert(Search)', 'Insert(Timeline)',
          'Delete(Search)', 'Delete(Timeline)', 'Delete(KeywordCount)', 'Delete(HashtagCount)',
          'Back-Up(ALL)', 'Roll-Back(ALL)'),
         ('Hadoop',
          'Keyword', 'Hashtag'),
         ('Visualization(Base)',
          'Line Graph', 'Word Cloud', 'Bar Graph', 'Stacked Bar Graph', 'Pie Graph'),
         ('Visualization(Analysis)',
          'Bar Graph', 'Stacked Bar Graph', 'Pie Graph'))
# --------------------------------------------------------------------------------------------------
while True:
    # ----------------------------------------------------------------------------------------------
    # Output Title
    # ----------------------------------------------------------------------------------------------
    for x in range(0, len(Title)):
        for y in range(0, len(Title[x])):
            if y == 0:
                print('%s.%s' % (x + 1, Title[x][y]))
            else:
                print('\t%s%s.%s' % (x + 1, y, Title[x][y]))
    print('%s.EXIT' % str(len(Title) + 1))
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
    elif cNum == '11':
        '''
        # ------------------------------------------------------------------------------------------
        # Single Operation
        # ------------------------------------------------------------------------------------------
        # Issuing Access Token
        accessToken = twitter.encodeKey(paramAPI[0][0], paramAPI[0][1])
        # ------------------------------------------------------------------------------------------
        # Bearer Authentication(=Token Authentication): HTTP authentication scheme that involves security tokens
        bearerKey = twitter.getAuthResponse(accessToken)
        # ------------------------------------------------------------------------------------------
        # Get Tweets using TwitterAPI
        tweets = twitter.searchTweet(bearerKey, paramAPI[0][2], query, date[0], date[1], maxResults)
        # ------------------------------------------------------------------------------------------
        # Prepeocessing Tweets
        json, hashtag, user = twitter.preprocess(tweets)
        # ------------------------------------------------------------------------------------------
        '''
    # ----------------------------------------------------------------------------------------------
    # Twitter - Timeline
    # ----------------------------------------------------------------------------------------------
    elif cNum == '12':
        # ------------------------------------------------------------------------------------------
        # Issuing Access Token
        accessToken = twitter.encodeKey(paramAPI[0][0], paramAPI[0][1])
        # ------------------------------------------------------------------------------------------
        # Bearer Authentication(=Token Authentication): HTTP authentication scheme that involves security tokens
        bearerKey = twitter.getAuthResponse(accessToken)
        # ------------------------------------------------------------------------------------------
        # Get Timelines using get_Timeline
        timelines = twitter.searchTimeline(bearerKey, code[1], count, include_rts)
        # ------------------------------------------------------------------------------------------
        # Prepeocessing Timelines
        tJson, tHashtag, tUser = twitter.preprocess(timelines)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Insert(Search)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '21':
        # ------------------------------------------------------------------------------------------
        for val in b:
            db.insertDB('S_HASHTAG',val)
        for val in c:
            db.insertDB('S_USER',val)  
        for val in a:
            db.insertDB('S_JSON',val
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
    # Hadoop - Keyword
    # ----------------------------------------------------------------------------------------------
    elif cNum == '31'
        # ------------------------------------------------------------------------------------------
        os.system('''sqoop import --connect jdbc:mysql://localhost/%s --username %s  --password %s
                                  --table %s --columns %s
                                  --%s hdfs://localhost:9000/user/vi/%s  -%s %s''' 
                  % (pramSqoop[0], pramSqoop[1], pramSqoop[2],
                     pramSqoop[3][0], pramSqoop[4][0],
                     pramSqoop[5][0][0], pramSqoop[5][0][1], pramSqoop[6][0][0], pramSqoop[6][0][1]))
        os.system('''yarn jar /home/vi/hadoop/jar/KeywordCount.jar KeywordCount /user/vi/%s/part-m-00000 %s'''
                  % (pramSqoop[5][0][1], pramSqoop[5][1][1]))
        os.system('''sqoop export --connect jdbc:mysql://localhost/%s --username %s  --password %s
                                  --table %s --columns %s
                                  --%s hdfs://localhost:9000/user/vi/%s/part-r-00000  --%s %s''' 
                  % (pramSqoop[0], pramSqoop[1], pramSqoop[2],
                     pramSqoop[3][1], pramSqoop[4][1],
                     pramSqoop[5][1][0], pramSqoop[5][1][1], pramSqoop[6][1][0], pramSqoop[6][1][1]))
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Hadoop - Hashtag
    # ----------------------------------------------------------------------------------------------
    elif cNum == '32':
        # ------------------------------------------------------------------------------------------
        os.system('''sqoop import --connect %s --username %s  --password %s
                                  --table %s --columns %s
                                  --%s hdfs://localhost:9000/user/vi/%s  -%s %s''' 
                  % (pramSqoop[0], pramSqoop[1], pramSqoop[2],
                     pramSqoop[3][2], pramSqoop[4][2],
                     pramSqoop[5][2][0], pramSqoop[5][2][1], pramSqoop[6][0][0], pramSqoop[6][0][1]))
        os.system('''yarn jar /home/vi/hadoop/jar/KeywordCount.jar KeywordCount /user/vi/%s/part-m-00000 %s'''
                  % (pramSqoop[5][2][1], pramSqoop[5][3][1]))
        os.system('''sqoop export --connect %s --username %s  --password %s
                                  --table %s --columns %s
                                  --%s hdfs://localhost:9000/user/vi/%s/part-r-00000  --%s %s''' 
                  % (pramSqoop[0], pramSqoop[1], pramSqoop[2],
                     pramSqoop[3][3], pramSqoop[4][3],
                     pramSqoop[5][3][0], pramSqoop[5][3][1], pramSqoop[6][1][0], pramSqoop[6][1][1]))
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Search
    # ----------------------------------------------------------------------------------------------
    elif cNum == '41':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Line Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '42':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Word Cloud
    # ----------------------------------------------------------------------------------------------
    elif cNum == '43':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '44':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Stacked Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '45':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '51':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Stacked Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '52':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Pie Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '53':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Input Number is not NumList: 11, 12
    #                            : 21, 22, 23, 24, 25, 26, 27, 28
    #                            : 31, 32
    #                            : 41 ,42, 43, 44 ,45
    #                            : 51, 52, 53
    # ----------------------------------------------------------------------------------------------
    else:
        # ------------------------------------------------------------------------------------------
        print('Re-enter')
        # ------------------------------------------------------------------------------------------
        continue
        # ------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
