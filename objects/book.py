class Book:
    def __init__(self, title: str, author: str,) -> None:
        self.title = title
        self.author = author
    
    def get_title(self):
        print(f"Title: {self.title}")
    
    def get_author(self):
        print(f"Author: {self.author}")

pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen")
hamlet = Book("Hamlet", "William Shakespeare")
war_and_peace = Book("War and Peace", "Leo Tolstoy")

print(pride_and_prejudice.title)
print(pride_and_prejudice.author)
pride_and_prejudice.get_title()
pride_and_prejudice.get_author()