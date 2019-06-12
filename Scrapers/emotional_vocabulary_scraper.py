import requests

from bs4 import BeautifulSoup

url= 'https://www.verywellfamily.com/feelings-words-from-a-to-z-2086647'

request = requests.get(url)

soup = BeautifulSoup(request.content, 'html.parser')

"""there is alot of content on this page that isn't pertinent to what we want
so the next few variables is just to limit the text we save to what is"""

start_flag=False
start_string='To help begin the journey, here is a list of common feelings words from A to Z'
break_string='Get diet and wellness tips to help your kids stay healthy and happy.'

words=[]

#all the words are part of 1st children
for c in soup.select("div p:nth-of-type(1)"):
    #detect for start of definitions
    if start_flag is True:
        #check for the line that follows the end of definitions
        if break_string in c.text:
            break
        #update list of words
        words.extend(c.text.strip().split(','))
    if start_string in c.text:
        start_flag=True

print (words)
    