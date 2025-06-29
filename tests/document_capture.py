from content_retriever import UserDocument
from content_retriever import RepositoryDocument
from loguru import logger

if __name__ == "__main__":
    # Example usage of UserDocument
    logger.info("Creating a UserDocument instance...")
    temp = UserDocument(
        content={"key": "value", "another_key": "another_value"},
        platform="local",
        author_id="123",
        author_full_name="John Doe",
        user_id="456",
        filename="example.txt",
        file_type="txt",
        tags=["example", "test"],
        notes="This is a sample user document"
    )
    logger.info(f"UserDocument summary: {temp.summarize()}")

    # Example usage of RepositoryDocument
    logger.info("Creating a RepositoryDocument instance...")
    repo_doc = RepositoryDocument(
        content={"key": "value"},
        platform="github",
        author_id="123",
        author_full_name="John Doe",
        repo_link="https://github.com/user/repo",
        repo_name="repo",
        stars=5,
        description="A sample repository"
    )

    logger.info(f"RepositoryDocument summary: {repo_doc.summarize()}")