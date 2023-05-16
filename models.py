from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    addresses = relationship("Address", back_populates="user")
    orders = relationship("Order", back_populates="user")

    class Config:
        orm_mode = True


class Address(Base):
    __tablename__ = "addresses"

    address_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    street = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)

    user = relationship("User", back_populates="addresses")

    class Config:
        orm_mode = True


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)

    products = relationship("Product", back_populates="category")

    class Config:
        orm_mode = True


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.category_id"))

    category = relationship("Category", back_populates="products")
    order_products = relationship("OrderProduct", back_populates="product")

    class Config:
        orm_mode = True


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_amount = Column(Integer)
    created_at = Column(String)

    user = relationship("User", back_populates="orders")
    order_products = relationship("OrderProduct", back_populates="order")

    class Config:
        orm_mode = True


class OrderProduct(Base):
    __tablename__ = "order_products"

    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)
    quantity = Column(Integer)

    order = relationship("Order", back_populates="order_products")
    product = relationship("Product", back_populates="order_products")

    class Config:
        orm_mode = True
