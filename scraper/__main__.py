from . import *

store = saver.Store()
page = get_page()
table = find_desktop_table(page)
print(table)
