from abc import ABC, abstractmethod

class BaseCrawler(ABC):
    """
    Base class for web crawlers.
    
    This class defines the interface for web crawlers, which should implement the `extract` method.
    """
    def __init__(self, source_address: str):
        """
        Initialize the BaseCrawler with a source address.

        :param source_address: The address from which to extract content.
        """
        self.source_address = source_address

    @abstractmethod
    def extract(self, link: str, **kwargs) -> None: 
        """
        Extract content from the provided link.
        
        :param link: The URL to extract content from.
        :param kwargs: Additional keyword arguments (e.g., user information).
        """
        pass