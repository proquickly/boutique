import pprint

import bs4

html_doc = """
<html><head><title>Python for developers</title></head>
<body>
<p class="title"><b>Why is python a good language?</b></p>

<p class="reason">Python is a general purpose language applied to many problem
types:
<a href="https://realpython.com" class="learning" id="link1">Good info</a> and
<a href="https://python.org" class="official" id="link2">Official site</a>;
and there are many others too.</p>
"""
soup = bs4.BeautifulSoup(html_doc, "html.parser")
print(soup.prettify())
print(f"{soup.head=}")
print(f"{soup.title=}")
print(f"{soup.body=}")
pprint.pprint(f"{soup.findAll('p')=}")
print()
pprint.pprint(f"{soup.findAll('a')=}")
