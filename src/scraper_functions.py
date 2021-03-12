import requests
from typing import Any
from bs4 import BeautifulSoup as bs

"""
this is a collection of functions useful for scraping, if you find yourself 
doing something more than once, feel free to add a function to take care of
it here. 
"""


def get_soup(url) -> Any:
    request = requests.get(url)
    return bs(request.content, "html.parser")


def open_soup(path):
    """
    open locally saved html as file
    """
    with open(path, "r") as f:
        return bs(f.read(), "html.parser")


def save_html(html, filename):
    """save html to file
    uses 'rb' (write bytes) in order to avoid encoding issues"""
    with open(filename, "w") as f:
        f.write(html)


# not done yet
"""
def get_table():
    table_headers=table_header.find_all('th')
    for i,header in enumerate(table_headers):
        table_headers[i]=header
        print(header.contents[0])
"""


def freedict_lookup(word, type="adj"):
    base_url = "https://www.thefreedictionary.com/"
    query_url = base_url + word
    request = requests.get(query_url)
    soup = BeautifulSoup(request.content, "html.parser")
    print("finding sections")
    # NOTE: check for existence of h2 in section, as only definitions
    # have it.
    for item in soup.find_all("section", "data-src"):
        print(item.text)
    for item in soup.find_all("div", {"class": "ds-list"}):
        # check for existence in order to avoid error
        # note could probably be moved to inside try catch block
        if item.find("b") is not None:
            if "1." in item.find("b").text:
                try:
                    print(
                        item.contents[
                            next(
                                i
                                for i, content in enumerate(item.contents)
                                if "1." in content.text
                            )
                            + 1
                        ]
                    )
                except AttributeError:
                    print("the tested content isn't text")


# Definition > section:nth-child(2) > div:nth-child(3) > div:nth-child(5)
if __name__ == "__main__":
    print(fd_lookup("angry"))