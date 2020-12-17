import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('https://www.gfxtra31.com/adobe-after-effects/after-effects-project-files-ae/1566213-videohive-hyper-graphics-pack-v2-24835354.html');
time.sleep(5) # Let the user actually see something!

preview_url = driver.find_element_by_xpath("//strong/text()[contains(.,'PREVIEW')]/../..").get_attribute("href")
filenext_url=driver.find_element_by_xpath("//img[@src='/uploads/1.filenext.gif']/..").get_attribute("href")


import requests
url='https://www.gfxtra31.com/adobe-after-effects/after-effects-project-files-ae/1566213-videohive-hyper-graphics-pack-v2-24835354.html'

s = requests.Session()
g=s.get('https://www.gfxtra31.com/engine/go.php?url=aHR0cDovL2dmdHhyYS5uZXQvZDE5ZWI1ZmM2NTViYTE0OGQ5NGE5NGU4ZWU1ZmIzZjQvVkgtMjQ4MzUzNTQtVjIucmFyLmh0bWw%3D', headers={'referer': url})
filenext_urlll=g.url


