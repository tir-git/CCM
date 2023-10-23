# my_list = [1, 2, 3, 4, 5]
# for item in my_list:
#     print(item)

from bs4 import BeautifulSoup

html = """
<div class="some-class">Element 1</div>
<div class="another-class">Element 2</div>
<div class="some-class">Element 3</div>
"""

soup = BeautifulSoup(html, 'html.parser')

elements = soup.find_all('div', {'class': 'some-class'})
for element in elements:
    print(element.text)

print (element)
print(elements)