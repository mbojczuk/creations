#TODO: Implement content retrieval logic
# Create a base class that defines the interface for content retrieval
# Then page-specific classes can inherit from this base class for different retrieval methods
from .documents.user_document import UserDocument
from .documents.repository_document import RepositoryDocument
from .documents.document_class import DocumentBase

__all__ = ["UserDocument", "RepositoryDocument", "DocumentBase"]