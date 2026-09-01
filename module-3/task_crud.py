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

    def __repr__(self) -> str:
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] {self.title} (priority: {self.priority})"

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# CREATE
def create_task(title, description=None, priority="medium"):
    with Session(engine) as session:
        task = Task(title=title, description=description, priority=priority)
        session.add(task)
        session.commit()
        session.refresh(task)
        print(f" Created: {task} (id={task.id})")

print("===Creating Tasks===")
create_task("Learn SQLAlchemy CRUD", "Complete the guided example", "high")
create_task("Practice joins", "Do the employee joins exercise", "medium")
create_task("Read about ORMs", "Compare SQLAlchemy vs Django ORM", "low")
create_task("Build module project", "Library management system", "high")
create_task("Review SQL syntax", priority="low")

# READ
def get_all_tasks():
    with Session(engine) as session:
        return session.query(Task).all()
    
def get_tasks_by_priority(priority):
    with Session(engine) as session:
        return session.query(Task).filter_by(priority=priority).all()
    
def get_incomplete_tasks():
    with Session(engine) as session:
        return session.query(Task)\
            .filter(Task.completed.is_(False))\
            .order_by(Task.priority)\
            .all()
            
def get_task_by_id(task_id):
    with Session(engine) as session:
        return session.get(Task, task_id)
    
print("\n=== All Tasks ===")
for task in get_all_tasks():
    print(f"  {task}")

print("\n=== High Priority ===")
for task in get_tasks_by_priority("high"):
    print(f"  {task}")
    
# UPDATE
def complete_task(task_id):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task is None:
            print(f"  Task {task_id} not found!")
            return
        task.completed = True  # Just change the attribute
        session.commit()
        print(f"  Completed: {task}")

def update_priority(task_id, new_priority):
    """Change a task's priority."""
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task is None:
            print(f"  Task {task_id} not found!")
            return
        old = task.priority
        task.priority = new_priority
        session.commit()
        print(f"  Updated: {task.title} ({old} -> {new_priority})")

print("\\n=== Completing Tasks ===")
complete_task(1)
complete_task(3)

print("\\n=== Updating Priority ===")
update_priority(2, "high")


# DELETE
def delete_task(task_id):
    with Session(engine) as session:
        task = session.get(Task, task_id)
        if task is None:
            return
        title = task.title
        session.delete(task)
        session.commit()
        print(f" Deleted: {title}")
        
def delete_completed():
    with Session(engine) as session:
        completed = session.query(Task).filter_by(completed=True).all()
        count = len(completed)
        for task in completed:
            session.delete(task)
        session.commit()
        print(f" Deleted {count} completed task(s)")

print("\n=== Deleting Task #5 ===")
delete_task(5)

print("\n=== Deleting Completed ===")
delete_completed()

print("\n=== Remaining Tasks ===")
for task in get_all_tasks():
    print(f"  {task}")