from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from src.utils.file_handlers import write_to_file, read_from_file


def fetch_page_soup(url):
    service = Service(ChromeDriverManager().install())
    options = Options()

    html_page = read_from_file("./documents/index.html")
    soup = BeautifulSoup(html_page, "lxml")

    if soup.text.strip() == "":
        with webdriver.Chrome(service=service, options=options) as driver:
            driver.get(url)  # open a website in the browser
            soup = BeautifulSoup(driver.page_source, "lxml")

            write_to_file("./documents/index.html", soup.prettify())

    return soup

def convert_to_markdown(soup):
    md = MarkdownConverter(heading_style="ATX").convert_soup(soup)

    lines = md.splitlines()

    remaining_lines = lines[12:]

    # remove lines starting with `©`
    # filtered_lines = [line for line in lines if not line.strip().startswith("©")]

    new_md = "\n".join(remaining_lines)

    write_to_file("./documents/index.md", new_md)

    return new_md
