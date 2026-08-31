from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional
from datetime import datetime

# --- Engine: connects to a SQLite database file ---
engine = create_engine(
    "sqlite:///product_catalog.db",
    # echo=True
)

class Base(DeclarativeBase):
    pass

# Define Category Model
class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description : Mapped[Optional[str]] = mapped_column()
    
# Define Product Model
class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    in_stock: Mapped[bool] = mapped_column(default=True)
    category_name: Mapped[str] = mapped_column()

Base.metadata.drop_all(engine)    
Base.metadata.create_all(engine)
print("\nTables created successfully!")

# Populate table with data
with Session(engine) as session:
    categories_to_add = [
        Category(name="Electronics", description="Anything with electrons"),Category(name="Accessories", description="Tech and lifestyle accessories"),
        Category(name="Video Games", description="Games for all platforms"), Category(name="Home Goods")
    ]
    
    session.add_all(categories_to_add)
    
    products_to_add = [
        Product(name="Small Monitor", price=129.00, category_name="Electronics"),
        Product(name="Wireless Mouse", price=39.99, category_name="Accessories"),
        Product(name="Gaming Headset", price=89.99, category_name="Accessories"),
        Product(name="PlayStation 5", in_stock=False, price=499.99, category_name="Video Games"),
        Product(name="USB-C Cable", price=14.99, category_name="Accessories"),
        Product(name="Desk Lamp", price=44.99, category_name="Home Goods")
    ]
    
    session.add_all(products_to_add)
    session.commit()
    
# Query data back
with Session(engine) as session:
    # Get all categories
    print("\n=== Categories ===")
    categories = session.query(Category).all()
    for category in categories:
        print(f" {category.name}")
        
    # Get all products in stock
    print("\n=== Products In Stock ===")
    products_in_stock = session.query(Product).filter_by(in_stock=True)
    for product in products_in_stock:
        print(f" {product.name}")
        
    # Get all products under $50
    print("\n=== Products under $50 ===")
    products_under_50 =  session.query(Product).filter(Product.price < 50.00)
    for product in products_under_50:
        print(f" {product.name} - ${product.price}")