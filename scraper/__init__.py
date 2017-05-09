from bs4 import BeautifulSoup
from enum import Enum
import requests
from . import saver

class Browser(Enum):
    firefox = "firefox".casefold()
    chrome = "chrome".casefold()
    safari = "safari".casefold()
    opera = "opera".casefold()
    edge = "edge".casefold()
    internet_explorer = "internet explorer".casefold()

def get_page():
    url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter"
    r = requests.get(url)
    return BeautifulSoup(r.text, "html.parser")

def find_desktop_table(page):
    return page.find(id="compat-desktop")

def to_browser_compatibilities(table):
    pass

def parse_browser(header_text):
    casefolded = header_text.casefold()
    for browser in Browser:
        if browser in casefolded:
            return browser

