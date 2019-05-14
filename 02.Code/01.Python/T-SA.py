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
              ['S_JSON', 'KEYWORD_COUNT', 'S_JSON', 'HASHTAG_COUNT'], # Table List
              ['TEXT', 'KEYWORD,COUNT', 'TEXT', 'HASHTAG,COUNT'], # Columns
              [['target-dir', 'KEYWORD_INPUT'], ['export-dir', 'KEYWORD_OUTPUT'], ['target-dir', 'HASHTAG_INTPUT'], ['export-dir', 'HASHTAG_OUTPUT']], # [target-dir/export-dir, Path]
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
          'Search', 'Timeline'), # LSJ, LSJ
         ('DataBase',
          'Select(JSON - S, T)', 'Select(COUNT - Keyword, Hashtag)',
          'Insert(Search)', 'Insert(Timeline)', # BIG, BIG
          'Delete(Search)', 'Delete(Timeline)', 'Delete(KeywordCount)', 'Delete(HashtagCount)'),
         ('Hadoop',
          'Keyword', 'Hashtag', 'Start', 'Stop'), # LYH, LYH, LYH, LYH
         ('Visualization(Base)',
          'Line Graph', 'Word Cloud', 'Bar Graph', 'Stacked Bar Graph', 'Pie Graph'),
         ('Visualization(Analysis)',
          'Bar Graph', 'Stacked Bar Graph', 'Pie Graph'),
         ('BACK-UP(TWITTER)',), # LSJ
         ('ROLL-BACK(TWITTER)',), #LSJ
         ('EXIT',))
# --------------------------------------------------------------------------------------------------
while True:
    # ----------------------------------------------------------------------------------------------
    # Output Title
    # ----------------------------------------------------------------------------------------------
    for x in range(0, len(Title)):
        for y in range(0, len(Title[x])):
            print('%s.%s' % (x + 1, Title[x][y])) if y == 0 else print('\t%s%s.%s' % (x + 1, y, Title[x][y]))
    print('Choice Number(XX) >>>')
    # ----------------------------------------------------------------------------------------------
    # Input Number
    # ----------------------------------------------------------------------------------------------
    cNum = input()
    # 1 ============================================================================================
    # ----------------------------------------------------------------------------------------------
    # Twitter - Search
    # ----------------------------------------------------------------------------------------------
    if cNum == '11':
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
        sJson, sHashtag, sUser = twitter.preprocess(tweets)
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
    # 2 ============================================================================================
    # ----------------------------------------------------------------------------------------------
    # DataBase - Select(JSON - S, T)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '21':
        # ------------------------------------------------------------------------------------------
        print("***** S_JSON TABLE *****")
        print(db.dbSelect("date_format(create_at,'%Y-%m-%d') create_at, count(*)",'S_JSON',"group by date_format(create_at, '%Y-%m-%d')"))
        print("***** T_JSON TABLE *****")
        print(db.dbSelect("date_format(create_at,'%Y-%m-%d') create_at, count(*)",'T_JSON',"group by date_format(create_at, '%Y-%m-%d')"))
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Select(COUNT - Keyword, Hashtag)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '22':
        # ------------------------------------------------------------------------------------------
        print("***** KeywordCount TABLE *****")
        print(db.dbSelect('*','KEYWORD_COUNT',''))
        print("***** HashtagCount TABLE *****")
        print(db.dbSelect('*','HASHTAG_COUNT',''))
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Insert(Search)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '23':
        # ------------------------------------------------------------------------------------------
        for val in sHashtag:
            db.dbInsert('S_HASHTAG',val)
        for val in sUser:
            db.dbInsert('S_USER',val)  
        for val in sJson:
            db.dbInsert('S_JSON',val)
        print("Insert Complete")
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Insert(Timeline)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '24':
        # ------------------------------------------------------------------------------------------
        for val in tHashtag:
            db.dbInsert('T_HASHTAG',val)
        for val in tUser:
            db.dbInsert('T_USER',val)  
        for val in tJson:
            db.dbInsert('T_JSON',val)
        print("Insert Complete")
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(Search)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '25':
        # ------------------------------------------------------------------------------------------
        db.dbDelete('S_JSON')
        db.dbDelete('S_USER')
        db.dbDelete('S_HASHTAG')
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(Timeline)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '26':
        # ------------------------------------------------------------------------------------------
        db.dbDelete('T_JSON')
        db.dbDelete('T_USER')
        db.dbDelete('T_HASHTAG')
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(KeywordCount)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '27':
        # ------------------------------------------------------------------------------------------
        db.dbDelete('KeywordCount')
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Delete(HashtagCount)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '28':
        # ------------------------------------------------------------------------------------------
        db.dbDelete('HashtagCount')
        # ------------------------------------------------------------------------------------------
    # 3 ============================================================================================
    # ----------------------------------------------------------------------------------------------
    # Hadoop - Keyword
    # ----------------------------------------------------------------------------------------------
    elif cNum == '31':
        # ------------------------------------------------------------------------------------------
        os.system('''sqoop import --connect jdbc:mysql://localhost/%s --username %s --password %s --table %s --columns %s --%s hdfs://localhost:9000/user/vi/%s -%s %s''' 
                  % (paramSqoop[0], paramSqoop[1], paramSqoop[2],
                     paramSqoop[3][0], paramSqoop[4][0],
                     paramSqoop[5][0][0], paramSqoop[5][0][1], paramSqoop[6][0][0], paramSqoop[6][0][1]))
        os.system('''yarn jar /home/vi/hadoop/jar/KeywordCount.jar KeywordCount /user/vi/%s/part-m-00000 %s'''
                  % (paramSqoop[5][0][1], paramSqoop[5][1][1]))
        os.system('''sqoop export --connect jdbc:mysql://localhost/%s --username %s --password %s --table %s --columns %s --%s hdfs://localhost:9000/user/vi/%s/part-r-00000 --%s %s''' 
                  % (paramSqoop[0], paramSqoop[1], paramSqoop[2],
                     paramSqoop[3][1], paramSqoop[4][1],
                     paramSqoop[5][1][0], paramSqoop[5][1][1], paramSqoop[6][1][0], paramSqoop[6][1][1]))
        os.system('''hdfs dfs -rmr /user/vi/KEYWORD_*''')
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Hadoop - Hashtag
    # ----------------------------------------------------------------------------------------------
    elif cNum == '32':
        # ------------------------------------------------------------------------------------------
        os.system('''sqoop import --connect jdbc:mysql://localhost/%s --username %s --password %s --table %s --columns %s --%s hdfs://localhost:9000/user/vi/%s -%s %s''' 
                  % (paramSqoop[0], paramSqoop[1], paramSqoop[2],
                     paramSqoop[3][2], paramSqoop[4][2],
                     paramSqoop[5][2][0], paramSqoop[5][2][1], paramSqoop[6][0][0], paramSqoop[6][0][1]))
        os.system('''yarn jar /home/vi/hadoop/jar/HashtagCount.jar HashtagCount /user/vi/%s/part-m-00000 %s'''
                  % (paramSqoop[5][2][1], paramSqoop[5][3][1]))
        os.system('''sqoop export --connect jdbc:mysql://localhost/%s --username %s --password %s --table %s --columns %s --%s hdfs://localhost:9000/user/vi/%s/part-r-00000 --%s %s''' 
                  % (paramSqoop[0], paramSqoop[1], paramSqoop[2],
                     paramSqoop[3][3], paramSqoop[4][3],
                     paramSqoop[5][3][0], paramSqoop[5][3][1], paramSqoop[6][1][0], paramSqoop[6][1][1]))
        os.system('''hdfs dfs -rmr /user/vi/HASHTAG_*''')
        # ------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
    # Hadoop - Start
    # ----------------------------------------------------------------------------------------------
    elif cNum == '33':
        # ------------------------------------------------------------------------------------------
        os.system('''start-all.sh''')
        os.system('''jps''')                       
        # ------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------
    # Hadoop - Stop
    # ----------------------------------------------------------------------------------------------
    elif cNum == '34':
        # ------------------------------------------------------------------------------------------
        os.system('''stop-all.sh''')
        # ------------------------------------------------------------------------------------------
    # 4 ============================================================================================
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Search
    # ----------------------------------------------------------------------------------------------
    elif cNum == '41':
        # ------------------------------------------------------------------------------------------
        b=dict(db.dbSelect("date_format(create_at,'%Y-%m-%d') create_at, count(*)",'T_JSON',"group by date_format(create_at, '%Y-%m-%d')"))
        visual.base_linegraph(b)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Line Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '42':
        # ------------------------------------------------------------------------------------------
        b=dict(db.dbSelect('*','HASHTAG_COUNT',''))
        visual.base_wordcloud(b)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Word Cloud
    # ----------------------------------------------------------------------------------------------
    elif cNum == '43':
        # ------------------------------------------------------------------------------------------
        b=dict(db.dbSelect('*','HASHTAG_COUNT',''))
        visual.base_bargraph(b)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '44':
        # ------------------------------------------------------------------------------------------
        b=dict(db.dbSelect('*','HASHTAG_COUNT',''))
        visual.base_stackedbargraph(b)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Base) - Stacked Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '45':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # 5 ============================================================================================
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '51':
        # ------------------------------------------------------------------------------------------
        b=dict(db.dbSelect('*','HASHTAG_COUNT',''))
        visual.analysis_bargraph(b)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Stacked Bar Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '52':
        # ------------------------------------------------------------------------------------------
        b=dict(db.dbSelect('*','HASHTAG_COUNT',''))
        visual.analysis_stackedbargraph(b)
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Visualization(Analysis) - Pie Graph
    # ----------------------------------------------------------------------------------------------
    elif cNum == '53':
        # ------------------------------------------------------------------------------------------
        print(cNum)
        # ------------------------------------------------------------------------------------------
    # 6, 7, 8 ======================================================================================
    # ----------------------------------------------------------------------------------------------
    # DataBase - Back-Up(ALL)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '6':
        # ------------------------------------------------------------------------------------------
        os.system('mysqldump -uT-SA -p1234 TWITTER > /home/vi/T-SA.sql')
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # DataBase - Roll-Back(ALL)
    # ----------------------------------------------------------------------------------------------
    elif cNum == '7':
        # ------------------------------------------------------------------------------------------
        os.system('mysql -uT-SA -p1234 TWITTER1 < /home/vi/T-SA.sql')
        # ------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------
    # Input Number Check(5) - EXIT
    # ----------------------------------------------------------------------------------------------
    if cNum == '8':
        print('EXIT!!')
        break
    # ----------------------------------------------------------------------------------------------
    # Input Number is not NumList: 11, 12
    #                            : 21, 22, 23, 24, 25, 26, 27, 28
    #                            : 31, 32, 33, 34
    #                            : 41 ,42, 43, 44 ,45
    #                            : 51, 52, 53
    #                            : 6, 7, 8
    # ----------------------------------------------------------------------------------------------
    else:
        # ------------------------------------------------------------------------------------------
        print('Re-enter')
        # ------------------------------------------------------------------------------------------
        continue
        # ------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
