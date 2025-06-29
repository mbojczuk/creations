from content_retriever import GithubCrawler
from loguru import logger

def test_github_crawler():
    crawler = GithubCrawler("https://github.com/mbojczuk/creations")
    crawler.extract()

if __name__ == "__main__":
    logger.info("Starting GitHub crawler test...")
    test_github_crawler()
    logger.info("GitHub crawler test completed.")