from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional

engine = create_engine("sqlite:///contacts.db", echo=False)

class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(200), nullable=False)
    last_name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    favorite: Mapped[bool] = mapped_column(default=False)
    
    def __repr__(self) -> str:
        favorite_status = "YES" if self.favorite else "NO"
        return f" {self.first_name} {self.last_name} | {self.email} | {self.phone} | FAVE: {favorite_status}"

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Functions
def add_contact(first_name, last_name, email, phone=None):
    with Session(engine) as session:
        contact = Contact(
            first_name=first_name, 
            last_name=last_name,
            email=email,
            phone=phone
        )
        session.add(contact)
        session.commit()
        session.refresh(contact)
        print(f" Created: {contact} (id={contact.id})")

def list_contacts():
    with Session(engine) as session:
        contacts =  session.query(Contact).order_by(Contact.last_name).all()
        for contact in contacts:
            print(contact)

def find_contact(email):
    with Session(engine) as session:
        contact = session.query(Contact).filter_by(email=email).one()
        print(contact)
        return contact
    
def update_phone(email, new_phone):
    with Session(engine) as session:
        contact = session.query(Contact).filter_by(email=email).one()
        if contact is None:
            print(f" Contact with email {email} not found!")
            return
        old_phone = contact.phone
        contact.phone = new_phone
        session.commit()
        print(f"Updated: {contact.first_name} {contact.last_name} ({old_phone} -> {new_phone})")

def toggle_favorite(email):
    with Session(engine) as session:
        contact = session.query(Contact).filter_by(email=email).one()
        if contact is None:
            print(f" Contact with email {email} not found!")
            return
        contact.favorite = not contact.favorite
        session.commit()
        status = "now" if contact.favorite else "not"
        print(f" {contact.first_name} {contact.last_name} is {status} a favorite")


def delete_contact(email):
    with Session(engine) as session:
        contact = session.query(Contact).filter_by(email=email).one()
        if contact is None:
            print(f" Contact with email {email} not found!")
            return
        name = f"{contact.first_name} {contact.last_name}"
        session.delete(contact)
        session.commit()
        print(f" Deleted: {name}")

# Execution
add_contact("Emily", "Cutler", "mily19@gmail.com", "817-555-7987")
add_contact("James", "Anderson", "james.anderson@gmail.com", "214-555-1234")
add_contact("Sarah", "Martinez", "sarah.martinez@gmail.com", "972-555-5678")
add_contact("Michael", "Johnson", "michael.j@gmail.com", "469-555-9012")
add_contact("Jessica", "Williams", "jess.williams@gmail.com", "972-555-3456")
add_contact("David", "Brown", "david.brown@gmail.com", "214-555-7890")
add_contact("Amanda", "Davis", "amanda.davis@gmail.com", "817-555-2345")
add_contact("Christopher", "Miller", "chris.miller@gmail.com", "469-555-6789")
add_contact("Jennifer", "Wilson", "jen.wilson@gmail.com", "972-555-0123")
add_contact("Daniel", "Moore", "daniel.moore@gmail.com", "214-555-4567")
add_contact("Rachel", "Taylor", "rachel.taylor@gmail.com", "817-555-8901")

print("\n=== ALL CONTACTS ===")
list_contacts()

print("\n=== Find james.anderson@gmail.com ===")
find_contact("james.anderson@gmail.com")

print("\n=== Update Emily's Phone # ===")
update_phone("mily19@gmail.com", "604-555-7987")

print("\n=== Toggle a favorite ===")
toggle_favorite("mily19@gmail.com")

print("\n=== DELETE A CONTACT ===")
delete_contact("michael.j@gmail.com")

print("\n=== ALL CONTACTS ===")
list_contacts()
