html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')
print('next sibling:',soup.a.next_sibling)
print('previous sibling:',soup.a.previous_sibling)
print("next siblings:",list(soup.a.next_siblings))
print("previouos siblings:",list(soup.a.previous_siblings))
