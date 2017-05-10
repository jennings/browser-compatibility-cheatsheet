from . import store
from .store import Type
from bs4 import BeautifulSoup
from sqlalchemy.sql import exists
import requests

# Download global objects page
try:
    with open("global_objects.html", "x") as fp:
        print("downloading global_objects.html")
        go = requests.get("https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects")
        fp.write(go.text)
except FileExistsError:
    pass

# Populate types
host = "https://developer.mozilla.org"
with open("global_objects.html", "r") as fp:
    page = BeautifulSoup(fp.read(), "html.parser")

links = page.find("article", id="wikiArticle").find_all("a")
link_pairs = [(a.code.string, host + a["href"]) for a in links if a.code]

with store.Session() as session:
    for pair in link_pairs:
        type = Type(name=pair[0], url=pair[1])
        if not session.query(Type).filter(Type.name==type.name).count():
            print("adding new global object: " + type.name)
            session.add(type)


# Download pages
with store.Session() as session:
    types_without_page_text = (session.query(Type)
                               .filter(Type.page_text == None))
    for type in types_without_page_text:
        print("downloading: " + type.url)
        r = requests.get(type.url)
        type.page_text = r.text
