# This is the document base class for the content retriever module.
from abc import ABC, abstractmethod
from typing import Dict

class DocumentBase(ABC):
    """
    Base class for documents in the content retriever module.
    
    This class serves as a foundation for all document types, providing common attributes and methods.
    It can be extended to create specific document types with additional functionality.
    """
    
    def __init__(
        self,
        content: Dict[str, str],
        platform: str,
        author_id: str,
        author_full_name: str
    ):
        self.content = content
        self.platform = platform
        self.author_id = author_id
        self.author_full_name = author_full_name


    @abstractmethod
    def summarize(self) -> str:
        """
        Abstract method to generate a summary or representation of the document.
        Must be implemented by subclasses.
        """
        pass
