import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    cn = soup.find_all(class_='noprint Inline-Template Template-Fact')

    cn_count = len(cn)
    print(f"there are {cn_count} citations needed in this article")
    return cn_count


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    cn = soup.find_all(class_='noprint Inline-Template Template-Fact')

    cn_sections = "The following sections need citations:\n"

    for c in cn:
        paragraph = c.parent.text
        cn_sections += paragraph + "\n"

    print(cn_sections)
    return cn_sections


if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Phonograph"
    get_citations_needed_report(url)
    get_citations_needed_count(url)
