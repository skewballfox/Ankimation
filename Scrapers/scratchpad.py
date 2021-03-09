{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.9.2 64-bit ('Ankimation': pipenv)",
   "metadata": {
    "interpreter": {
     "hash": "d6d043125a40a3c59d674a1e3291a46df0bb1f0be0ff6604d76e4e76436c415f"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from scraper_functions import get_soup, open_soup\n",
    "from bs4 import BeautifulSoup as bs\n",
    "\n",
    "#get_soup('url_here')\n",
    "open_soup('saved_html_here')"
   ]
  }
 ]
}