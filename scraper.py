import requests
from bs4 import BeautifulSoup




"""
<p>  text (paragraph)                    
    <sup class=noprint Inline-Template Template-Fact>   
         text  "["
       <i>  
            <a> <span> target(text) <span>

"""

def get_citations_needed_count(url):
    """
    find the number of citations in wekepedi . History of Mexico  page
    args : url : the lenk to the page ('https://en.wikipedia.org/wiki/History_of_Mexico')
    return number of citations needed
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')  # list

    return len(citations_needed)

print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))


def get_citations_needed_report(url):
    """
    find the paragraph of citations in wekepedi . History of Mexico  page
    args : url : the lenk to the page ('https://en.wikipedia.org/wiki/History_of_Mexico')
    return string : taxt (paragraph) of relevant passage
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')
    # paragraph befor sub   
    # p=soup.find_all('p') contain the sub  // 
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')

    # p=citations_needed[0].find_previous('p')
    # print(p)

    report = ""   # string have all p

    for citation in citations_needed:

        passage = citation.find_previous('p')

        report += passage.text.strip() + "\n \n"

    return report

print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))


report=get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')

with open('file.txt', 'w') as file:
    file.write(report)