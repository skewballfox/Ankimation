# Ankimation

an anki automation starter pack

## Dependencies (so far)

- requests
- bs4
- jupyter
- genanki
## Installation

if you have pipenv installed then all you need to do is run `pipenv install` in the same directory as this readme. alternatively if you want to use packages controlled by your system(to access stuff already on your system such as `nltk`) then run

```

pip install --user genanki requests jupyter bs4

```
or use your system package manager to install these things
## Getting started
just open the scratchpad in vscode(requires jupyter notebook extension) and either:

1. paste the url of the page you want to scrape
2. use inspect element in your browser, copy the region you are interested in, and save it to an html file

then fire away, if you want to see an example of it in action open the kakoune-example and run the entire notebook.

## Why jupyter?

scraping(for me) tends to be exploratory; change, run, see output, rinse, repeat. Jupyter makes this kind of exploration easier. I'd recommend looking through Jupyter's keyboard shortcuts(mainly related to running and navigating between blocks), because when repeatedly trying something and running something, your throughput shouldn't be bottlenecked by the distance between your keyboard and the mouse.

## Contributing

created an awesome model and want to add it to the model_list, have an idea how this project can be improved? have something that can make future automated building of anki decks easier, feel free to open an issue/pull request and contribute back to main. 

before you do that though, make sure that changes to scratchpad aren't tracked. if you plan on contributing, or are thinking about contributing, please run in the project folder after cloning the repo:

```

git update-index --skip-worktree src/scratchpad.ipynb

``` 

also, for this reason, i'd recommend saving scratchpad under a new filename(`ctrl-shift-s`) when writing a scraper, so that you have an already configured fresh start when writing another one.

## Useful Links

- [Beautiful Soup's documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests docs](https://requests.readthedocs.io/en/master/)
- [Jupyter's docs](https://jupyter.readthedocs.io/en/latest/)
- [Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)