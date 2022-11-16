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
            
        url = 'https://reddit.com/r/' + subreddit
        
        headers = {'User-Agent': 'Mozilla/5.0}
        
        required = requests.get(url, headers = headers)
        
        if req.status_code == 200:
            soup = BeautifulSoup(required.text, 'html.parser')
            print
            
            attributes = 
            counter = 1
            full = 0
            reddit_info = []
            while 1:
                   for posts in soup.find_all('div', attributes = attributes):
                    try:
                        # To obtain the post title
                        title = post.find('a', class_='title').text
                   
                        # To get the username of the post author
                        author = post.find('a', class_='author').text
                        
                        # To obtain the time of the post
                        time_stamp = post.Time.attributes['title']
                   
                        # To obtain the number of comments on the post
                        comments = post.find('a', class_='comments').text.split()[0]
                        if comments == 'comments':
                             comments = 0
                        
                        # To get upvotes on the post
                        upvotes = post.find('div', class_='score likes').text
                        if upvotes == '.':
                            upvotes = "None"
                        
                        link = post.find('a', class_='title')['href']
                        link = 'www.reddit.com' + link
                   
                        # Entering all the collected information into our database
                        entities = (subreddit, tag, title, author, time_stamp, upvotes,
                                    comments, link)
                        sql_insert_table(contact, entities)
                   
                        if counter == max_count:
                            full = 1
                            break
                        
                        counter += 1
                    except AttributeError:
                        continue
                   
                   if full:
                        break
                  
                   try:
                        next_button = soup.find('span', class_='next_button')
                        next_page = next_button.find('a').attributes['href]
                        
                        time.sleep(2)
                                                     
                        required = requests.get(next_page_link, headers=headers)
                        soup = BeautifulSoup(required.text, 'html.parser')
                   except:
                       break
                                                                     
              print('Finished\n')
              answer = input('Press (y) to continue or (n) to exit: ').lower()
              if answer == 'y' || answer == 'Y':
                   continue
              else if answer == 'n' || answer == 'N'
                      print('Exiting')
                      break
            else:
                print('Error occured')
                                                                     
if __name__ == '__main__':
    scarper()                                                   
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                                     
                                                               
                                                                     
