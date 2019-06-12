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
    print(query_url)
    request = requests.get(query_url)
    soup = BeautifulSoup(request.content, 'html.parser')
    
    return soup.find_all('div', {'class':'ds-list', 'b':"1."})
#Definition > section:nth-child(2) > div:nth-child(3) > div:nth-child(5)
if __name__=="__main__":
    print(fd_lookup("angry"))