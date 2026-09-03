from sqlalchemy import create_engine, String, ForeignKey, Table, Column, Integer
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, 
    relationship, Session
)
from typing import Optional

engine = create_engine("sqlite:///blog_relations.db", echo=False)

class Base(DeclarativeBase):
    pass


# Association table post <-> tag 
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)

# Models
class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    
    # One-to-many: one author -> many posts
    posts: Mapped[list["Post"]] = relationship(back_populates="author")
    
    def __repr__(self):
        return f"Author(name='{self.name}')"
    
class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    
    # Foreign key to authors
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    
    # Relationship back to author
    author: Mapped["Author"] = relationship(back_populates="posts")
    
    # Many-to-many: posts <-> tags
    tags: Mapped[list["Tag"]] = relationship(secondary=post_tags, back_populates="posts")
    
    def __repr__(self):
        return f"Post(title='{self.title}')"
    
class Tag(Base):
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
    # Many-to-many: tags <-> posts
    posts: Mapped[list["Post"]] = relationship(
        secondary=post_tags,
        back_populates="tags"
    )
    
    def __repr__(self):
        return f"Tag(name='{self.name}')"
    
# Create all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Tables created!\n")


with Session(engine) as session:
    alice = Author(name="Alice Park")
    bob = Author(name="Bob Martinez")
    
    # Create tags
    python_tag = Tag(name="python")
    sql_tag = Tag(name="sql")
    tutorial_tag = Tag(name="tutorial")
    beginner_tag = Tag(name="beginner") 
    
    # Create Posts
    post1 = Post(
        title="Getting Started with Python",
        content="Python is a versitile language",
        author=bob,
        tags=[python_tag]
    )
    
    post2 = Post(
        title="SQL Joins Explained",
        content="Joins combine data from multiple tables...",
        author=alice,
        tags=[sql_tag, tutorial_tag, beginner_tag]
    )
    
    post3 = Post(
        title="Python for Data Science",
        content="Data science with Python starts with...",
        author=bob,
        tags=[python_tag,]
    )
    
    # Add everything 
    session.add_all([alice,bob])
    session.commit()
    
    print("Data Created!")
    
    # Get all authors and their posts
    print("\n=== Authors and Their Posts ===")
    authors = session.query(Author).all()
    for author in authors:
        print(f"\n  {author.name} ({len(author.posts)} posts):")
        for post in author.posts:
            print(f"    - {post.title}")
    
    # Navigate the other direction: from post to author
    print("\n=== Post Authors ===")
    posts = session.query(Post).all()
    for post in posts:
        print(f"  '{post.title}' by {post.author.name}")
        
        
    # Add a new tag to an existing post
    python_for_ds = session.query(Post).filter_by(
        title="Python for Data Science"
    ).first()
    
    beginner = session.query(Tag).filter_by(name="beginner").first()
    
    python_for_ds.tags.append(beginner)
    session.commit()
    
    
    print("\n=== Updated Tags for 'Python for Data Science' ===")
    tag_names = [tag.name for tag in python_for_ds.tags]
    print(f"  Tags: {', '.join(tag_names)}")