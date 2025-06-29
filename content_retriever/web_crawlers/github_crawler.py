import os
import subprocess
import tempfile
import shutil
from loguru import logger
from .base_crawler import BaseCrawler
from content_retriever.documents.repository_document import RepositoryDocument


class GithubCrawler(BaseCrawler):
    """
    A simple crawler to fetch GitHub repository information.
    """
    document_model = RepositoryDocument # The model to use for storing repository data

    def __init__(self, repo_url: str, ignore=(".git", ".toml", ".lock", ".png")) -> None:
        super().__init__(repo_url)
        self.ignore = ignore # Tuple of file extensions to ignore

    def extract(self):
        url = self.source_address
        name = url.rstrip("/").split("/")[-1] # Extract the repository name from the URL
        logger.info(f"Fetching repository data from: {url}")

        # create a temporary directory to clone the repository
        local_temp = tempfile.mkdtemp()

        try:
            logger.info(f"Cloning repository {url} into a temporary directory.")
            os.chdir(local_temp)  # Change to the temporary directory
            subprocess.run(["git", "clone", url], check=True)

            if not os.listdir(local_temp):
                logger.error(f"Failed to clone repository {name}. The directory is empty.")
                return
            
            logger.info(f"Repository {name} cloned successfully.")
            repo_path = os.path.join(local_temp, name)  # Get the path of the cloned repository
            logger.info(f"Repository path: {repo_path}")

        finally:
            # Clean up the temporary directory
            logger.info(f"Cleaning up temporary directory: {local_temp}")
            os.chdir("..")
            shutil.rmtree(local_temp)  # Clean up the temporary directory

        

