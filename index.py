from modules.websites import Websites
from json import load

with open("sites/site.json", "r") as f:
    site = load(f)

for url in site["sites"]:
    website = Websites(url)
    html = website.get_website_data()
    print(f"Fetched data from {website.url}")
    print(html)
