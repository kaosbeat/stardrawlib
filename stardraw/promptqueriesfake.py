# import sqlite3
from random import choice

'''
sqlite> Select count(*) from prompts Where prompt LIKE '%word%';
sqlite> select word, count from wordcount order by count asc;
sqlite> select * from wordcount order by count desc;
'''

# con=sqlite3.connect('data/prompts.db')
# cur = con.cursor()

def countwords(word):
    # strippedword = word.strip("'")
    # selectQuery = "SELECT * FROM  words  WHERE word  = \"" +strippedword+ "\""
    # # print(selectQuery)
    # cur.execute(selectQuery)
    # data = list(cur)
    # totalcount = len(data)
    # # print(word, totalcount)
    # return totalcount
    return 10

def listWords():
    # query = "SELECT DISTINCT word FROM words"
    # cur.execute(query)
    # data = []
    # for row in cur:
    #     w = row[0]
    #     data.append(w)
    #     # countwords(w)
    data = ["word1", "word2" , "cyborg" , "rave", "algo"]
    return data

def create_wordcount(conn, word, totalcount):
    """
    Create a new wordcount
    :param conn:
    :param word:
    :param totalcount
    """
    # print("adding word")

    # sql = ''' INSERT INTO wordcount(word, count)
    #           VALUES(?,?) '''
    # cur = conn.cursor()
    # row = (word, totalcount)
    # cur.execute(sql, row)
    # conn.commit()
    # return cur.lastrowid



def wordContext(word):
    # strippedword = word.strip("'")
    # # selectQuery = "SELECT prompt FROM prompts WHERE prompt_id IN (SELECT prompts_id FROM words WHERE word = \"" +strippedword+ "\")"
    # selectQuery = "SELECT prompt FROM prompts WHERE prompt_id IN (SELECT prompts_id FROM words WHERE word = \"" +strippedword+ "\")  ORDER BY RANDOM() LIMIT 10"
    # # print(selectQuery)
    # cur.execute(selectQuery)
    # data = list(cur)
    # wordlist = []
    # # print (data)
    # for p in data:
    #     for w in p[0]:
    #         w = w.strip("|[]()'\"%$#@!^&*,:")
    #         if w != '':
    #             wordlist.append(w)
    wordlist = ["word1", "word2" , "cyborg" , "rave", "algo"]
    return wordlist
        
def getrandomwordlist():
    
    # selectQuery = "SELECT word, length(word) FROM words WHERE (length(word) > 4 and length(word) < 8)"
    # # print(selectQuery)
    # cur.execute(selectQuery)
    # data = list(cur)
    # wordlist = []
    # for d in data:
    #     w = d[0].strip("|[]()'\"%$#@!^&*,:")
    #     wordlist.append(w)
    wordlist = ["word1", "word2" , "cyborg" , "rave", "algo"]

    return wordlist



print (wordContext("cyborg"))