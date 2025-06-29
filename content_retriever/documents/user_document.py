from datetime import datetime
from content_retriever.documents.document_class import DocumentBase


class UserDocument(DocumentBase):
    """
    Represents a user-provided document in the content retriever module.

    Extends DocumentBase with attributes for locally stored files, including filename,
    creation timestamp, file type, and a user-assigned label.
    """

    def __init__(
        self,
        content: dict,
        platform: str,
        author_id: str,
        author_full_name: str,
        user_id: str,
        filename: str,
        file_type: str = "txt",
        created_at: datetime = None,
        tags: list[str] = None,
        notes: str = ""
    ):
        super().__init__(content, platform, author_id, author_full_name)
        self.user_id = user_id
        self.filename = filename
        self.file_type = file_type
        self.created_at = created_at or datetime.utcnow()
        self.tags = tags or []
        self.notes = notes

    def summarize(self) -> str:
        return f"{self.filename} ({self.file_type}) from {self.platform} tagged with {', '.join(self.tags)}"