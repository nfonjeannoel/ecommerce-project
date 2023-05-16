from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Address

class AddressCreate(BaseModel):
    street: str
    city: str
    state: str
    country: str


class AddressUpdate(BaseModel):
    street: str
    city: str
    state: str
    country: str


class Address(AddressCreate):
    address_id: int
    user_id: int

    class Config:
        orm_mode = True


# Category


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True


class CategoryList(BaseModel):
    categories: List[Category]


# Product

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


class ProductCreate(ProductBase):
    category_id: int


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int

    # category: Category

    class Config:
        orm_mode = True


# OrderProduct

class OrderProductBase(BaseModel):
    quantity: int


class OrderProductCreate(OrderProductBase):
    order_id: int
    product_id: int


class OrderProductUpdate(OrderProductBase):
    pass


class OrderProduct(OrderProductBase):
    order_id: int
    product_id: int

    class Config:
        orm_mode = True


# Order
class OrderBase(BaseModel):
    total_amount: int


class OrderCreate(OrderBase):
    user_id: int


class OrderUpdate(OrderBase):
    pass


class Order(OrderBase):
    order_id: int
    created_at: str
    user: User
    order_products: List[OrderProduct]

    class Config:
        orm_mode = True
