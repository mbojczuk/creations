from content_retriever.documents.document_class import DocumentBase

class RepositoryDocument(DocumentBase):
    """
    Represents a GitHub repository document in the content retriever module.

    Extends DocumentBase with repository-specific attributes.
    """

    def __init__(
        self,
        content: dict,
        platform: str,
        author_id: str,
        author_full_name: str,
        repo_link: str,
        repo_name: str = "",
        stars: int = 0,
        description: str = ""
    ):
        super().__init__(content, platform, author_id, author_full_name)
        self.repo_link = repo_link
        self.repo_name = repo_name
        self.stars = stars
        self.description = description

    def summarize(self) -> str:
        return f"{self.repo_name} by {self.author_full_name} ({self.platform}) — ⭐ {self.stars}"