import requests

from bs4 import BeautifulSoup

def save_html(html, path):
    """save html to file
    uses 'rb' (write bytes) in order to avoid encoding issues"""
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    """
    open locally saved html as file
    uses 'rb' (read bytes) in order to avoid encoding issues"""
    with open(path, 'rb') as f:
        return f.read()

def fd_lookup(word, type='adj'):
    base_url  = "https://www.thefreedictionary.com/"
    query_url = base_url + word
    request = requests.get(query_url)
    soup = BeautifulSoup(request.content, 'html.parser')
    print('finding sections')
    #NOTE: check for existence of h2 in section, as only definitions
    #have it. 
    for item in soup.find_all('section', 'data-src'):
            print (item.text)
    for item in soup.find_all('div', {'class':'ds-list'}):
        #check for existence in order to avoid error
        #note could probably be moved to inside try catch block
        if item.find('b') is not None:
                if '1.' in item.find('b').text:
                        try: 
                                print (item.contents[next(i for i, content in enumerate(item.contents) if '1.' in content.text)+1])
                        except AttributeError:
                                print("the tested content isn't text")
                                


#Definition > section:nth-child(2) > div:nth-child(3) > div:nth-child(5)
if __name__=="__main__":
    print(fd_lookup("angry"))