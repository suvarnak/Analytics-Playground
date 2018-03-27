import re
import requests
from bs4 import BeautifulSoup

url1 = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=Albert_Einstein&format=xml'
url2 = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=Satya Nadella&format=xml'
url3 = 'http://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles=Bill Gates&format=xml'

res = requests.get(url1)
soup = BeautifulSoup(res.text, 'lxml')
print("Unstructed Data 1",soup.revisions.getText())
birth_re = re.search(r'(Birth date(.*?)}})', soup.revisions.getText())
birth_data = birth_re.group(0).split('|')
birth_year1 = birth_data[2]
birth_month = birth_data[3]
birth_day = birth_data[4]

death_re = re.search(r'(Death date(.*?)}})', soup.revisions.getText())
death_data = death_re.group(0).split('|')
death_year = death_data[2]
death_month = death_data[3]
death_day = death_data[4]

print("Einstein\'s Birth year", birth_year1)

res = requests.get(url2)
soup = BeautifulSoup(res.text, 'lxml')
print("Unstructed Data 2",soup.revisions.getText())

birth_re = re.search(r'(Birth date(.*?)}})', soup.revisions.getText())
birth_data = birth_re.group(0).split('|')
birth_year2 = birth_data[2]
print("*************************")
print("Sample Analysis of Data")
print("*************************")

print("Satya Nadella's Birth year", birth_year2)
if birth_year1 > birth_year2 :
    print ("Einstein was born before Satya Nadella")
else:
    print ("Einstein was born after Satya Nadella")


