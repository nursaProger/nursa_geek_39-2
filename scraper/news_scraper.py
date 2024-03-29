import requests
from parsel import Selector



class NewsScraper:
    PLUS_URL = "https://www.prnewswire.com"
    URL = 'https://www.prnewswire.com/news-releases/news-releases-list/'
    HEADERS = {
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    LINK_XPATH = '//div[@class="row newsCards"]//a[@class="newsreleaseconsolidatelink display-outline w-100"]/@href'


    def scrape_data(self):
        response = requests.request("GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).getall()
        for link in links:
            print(self.PLUS_URL + link)


if __name__ == "__main__":
    scraper = NewsScraper()
    scraper.scrape_data()