import requests
import csv
import time
import sqlite3
from bs4 import BeautifulSoup

# Connect to the database.
def sql_connection():
    contact = sqlite3.connect('SubredditDatabase.db')
    return contact

# Creating the database tables.
def sql_table(contact):
    cur = contact.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS posts(SUBREDDIT text, TAG text, "
                " TITLE text, AUTHOR text, TIMESTAMP text, UPVOTES int, " 
                " COMMENTS text, URL text)")
    contact.commit()

# Insert recorded data into the sql query.
def sql_insert_table(contact, entities):
    cur = contact.cursor()
    cur.execute('INSERT INTO posts(SUBREDDIT, TAG, TITLE, AUTHOR, '
                'TIMESTAMP, UPVOTES, COMMENTS, URL) '
                'VALUES(?, ?, ?, ?, ?, ?, ?, ?)', entities)
    contact.commit()


# Scrape the subreddit to find the correct information.
def scraper():
    contact = sql_connection()
    sql_table(contact)

    while 1:
        subreddit = input('\n\nEnter the name of the subreddit: r/').lower()
        max_count = int(input('Enter the maximum number of entries to collect: '))
        select = int(input('Select tags to add for the search: \n1. hot\n2. new'
                            '\n3. rising\n4. top\n5. Make your choice: '))

        if select == 1:
            tag = 'hot'
            tag_url = '/'
        elif select == 2:
            tag = 'new'
            tag_url = '/new/'
        elif select == 3:
            tag = 'rising'
            tag_url = '/rising/'
        elif select == 4:
            tag = 'top'
            tag_url = '/controversial/'
        elif select == 5:
            tag = 'top'
            tag_url = '/top/'
            
        url =
        
        req
        
        if req.status_code == 200:
            soup
            print
            
            attributes = 
            counter = 1
            full = 0
            reddit_info = []
