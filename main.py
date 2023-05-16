from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# users

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the username or email is already taken
    existing_user = db.query(models.User).filter(
        or_(models.User.username == user.username, models.User.email == user.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="Username or email already taken")

    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# get all users
@app.get("/users", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for attr, value in user.dict(exclude_unset=True).items():
        setattr(db_user, attr, value)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}


# Address
@app.post("/addresses", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


@app.get("/addresses/{address_id}", response_model=schemas.Address)
def get_address(address_id: int, db: Session = Depends(get_db)):
    db_address = db.query(models.Address).filter(models.Address.address_id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    db_address = db.query(models.Address).filter(models.Address.address_id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    for attr, value in address.dict(exclude_unset=True).items():
        setattr(db_address, attr, value)
    db.commit()
    db.refresh(db_address)
    return db_address


@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = db.query(models.Address).filter(models.Address.address_id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(db_address)
    db.commit()
    return {"message": "Address deleted"}


# category
@app.post("/categories", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.get("/categories/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@app.put("/categories/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    for attr, value in category.dict(exclude_unset=True).items():
        setattr(db_category, attr, value)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.category_id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(db_category)
    db.commit()
    return {"message": "Category deleted"}


@app.get("/categories", response_model=schemas.CategoryList)
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    return {"categories": categories}


# product

from fastapi import HTTPException


@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return schemas.Product.from_orm(db_product)


# get all products
@app.get("/products", response_model=List[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for field, value in product.dict(exclude_unset=True).items():
        setattr(db_product, field, value)
    db.commit()
    db.refresh(db_product)
    return schemas.Product.from_orm(db_product)


@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}


# order
# get all orders
@app.get("/orders", response_model=List[schemas.Order])
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(models.Order).all()
    return orders


@app.post("/orders", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_order = models.Order(**order.dict(), created_at=current_time)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.get("/orders/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@app.put("/orders/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    for field, value in order.dict(exclude_unset=True).items():
        setattr(db_order, field, value)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted"}


# product_order

@app.post("/order_products", response_model=schemas.OrderProduct)
def create_order_product(order_product: schemas.OrderProductCreate, db: Session = Depends(get_db)):
    db_order_product = models.OrderProduct(**order_product.dict())
    db.add(db_order_product)
    db.commit()
    db.refresh(db_order_product)
    return db_order_product


@app.get("/order_products/{order_id}/{product_id}", response_model=schemas.OrderProduct)
def get_order_product(order_id: int, product_id: int, db: Session = Depends(get_db)):
    db_order_product = (
        db.query(models.OrderProduct)
        .filter(models.OrderProduct.order_id == order_id, models.OrderProduct.product_id == product_id)
        .first()
    )
    if not db_order_product:
        raise HTTPException(status_code=404, detail="Order Product not found")
    return db_order_product


@app.put("/order_products/{order_id}/{product_id}", response_model=schemas.OrderProduct)
def update_order_product(
        order_id: int, product_id: int, order_product: schemas.OrderProductUpdate, db: Session = Depends(get_db)
):
    db_order_product = (
        db.query(models.OrderProduct)
        .filter(models.OrderProduct.order_id == order_id, models.OrderProduct.product_id == product_id)
        .first()
    )
    if not db_order_product:
        raise HTTPException(status_code=404, detail="Order Product not found")
    for field, value in order_product.dict(exclude_unset=True).items():
        setattr(db_order_product, field, value)
    db.commit()
    db.refresh(db_order_product)
    return db_order_product


@app.delete("/order_products/{order_id}/{product_id}")
def delete_order_product(order_id: int, product_id: int, db: Session = Depends(get_db)):
    db_order_product = (
        db.query(models.OrderProduct)
        .filter(models.OrderProduct.order_id == order_id, models.OrderProduct.product_id == product_id)
        .first()
    )
    if not db_order_product:
        raise HTTPException(status_code=404, detail="Order Product not found")
    db.delete(db_order_product)
    db.commit()
    return {"message": "Order Product deleted"}
