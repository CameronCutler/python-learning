from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional
from datetime import datetime

# --- Engine: connects to a SQLite database file ---
engine = create_engine(
    "sqlite:///blog.db",
    echo=True
)

# --- Base class: all models inherit from this ---
class Base(DeclarativeBase):
    pass


# Define the Author model
class Author(Base):
    __tablename__ = "authors" # The table name in the db
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    bio: Mapped[Optional[str]] = mapped_column(String(500))
    
    def __repr__(self) -> str:
        return f"Author(id={self.id}, name='{self.name}', email='{self.email}')"
    
# Define the Post Model
class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    published: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    
    def __repr__(self) -> str:
        status = "published" if self.published else "draft"
        return f"Post(id={self.id}, title='{self.title}', status={status})"
    

# Create the tables
Base.metadata.create_all(engine)
print("\\nTables created successfully!")

# Create a session
# with Session(engine) as session:
#     # Create Author objects
#     alice = Author(name="Alice Park", email="alice@blog.com", bio="Python enthusiast!")
#     bob = Author(name="Bob Martinez", email="bob@blog.com")
    
#     # Add them tot the session
#     session.add(alice)
#     session.add(bob)
    
#     # Create Posts
#     post1 = Post(title="Getting Started with Python", content="Python is a great language...")
#     post2 = Post(title="SQL vs NoSQL", content="When to use each...", published=True)
    
#     session.add_all([post1, post2])
    
#     session.commit()
    
#     print(f"\\nCreated: {alice}")
#     print(f"Created: {bob}")
#     print(f"Created: {post1}")
#     print(f"Created: {post2}")

# Query data back
with Session(engine) as session:
    # Get all authors
    print("\\n=== Authors ===")
    authors = session.query(Author).all()
    for author in authors:
        print(f" {author}")
        
    # Get a specific author by email
    print("\\n=== Find by Email ===")
    alice = session.query(Author).filter_by(email="alice@blog.com").first()
    print(f"  Found: {alice}")
    print(f"  Bio: {alice.bio}")

    # Get published posts only
    print("\\n=== Published Posts ===")
    published = session.query(Post).filter_by(published=True).all()
    for post in published:
        print(f"  {post}")