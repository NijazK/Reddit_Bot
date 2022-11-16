import sqlite3
import os


# Connect to the database
def sql_connection():
    path = os.path.abspath('RedditDatabase.db')
    contact = sqlite3.connect(path)
    return contact


# Function designed to retrive all relevant information from the reddit and store it in the database
def sql_fetcher(contact):

    # SQL search query for rows and columns of the subreddit
    subreddit = input("\nEnter the subreddit to scrape: r/")
    count = 0
    cur = contact.cursor()
    cur.execute('SELECT * FROM posts') 
    rows = cur.fetchall()

    for r in rows:
        if subreddit in r:
            count += 1
            print(f'\nTAG: {r[1]}\nPOST TITLE: {r[2]}\nAUTHOR: {r[3]}\n'
                  f'TIME STAMP: {r[4]}\nUPVOTES: {r[5]}\nCOMMENTS: {r[6]}'
                  f'\nURL: {r[7]}\n')

    if count:
        print(f'{count} posts from this SubReddit\n')
    else:
        print('\nInvalid SubReddit\n')



contact = sql_connection()

while 1:
    sql_fetcher(contact)

    ans = input('\nPress (y) to continue or any other key to exit: ').lower()
    if ans == 'y':
        continue
    else:
        print('\nExiting..\n')
        break
