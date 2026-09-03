from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional

engine = create_engine("sqlite:///tasks.db", echo=False)

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500))
    priority: Mapped[str] = mapped_column(String(20), default="medium")
    completed: Mapped[bool] = mapped_column(default=False)
    
    def __repr__(self):
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] {self.title} (priority: {self.priority})"

Base.metadata.drop_all(engine)    
Base.metadata.create_all(engine)

# with Session(engine) as session:
#     task = Task(
#         title="Learn SQLAlchemy CRUD",
#         description="Complete the workshop!",
#         priority="high"
#     )
    
#     session.add(task)
#     session.commit()
    
#     print(task)
#     print(task.id)
    
def create_task(title, description=None, priority="medium"):
    task = Task(
        title = title,
        description = description,
        priority = priority
    )
    with Session(engine) as session:
        session.add(task)
        session.commit()
        
        print(task)
        
print("=== Creating Tasks ===")
create_task(
    title="Learn SQLAlchemy CRUD",
    description="Complete the workshop!",
    priority="high"
)        
create_task(
    title="Practice Joins",
    description="Do the employee joins exercise",
    priority="low"
)        
create_task(title="Read about ORMs")        