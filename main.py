from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import get_db, init_db

# 1. Initialize the database
init_db()

app = FastAPI(title="E-shop API")

@app.get("/")
def homepage():
    return {"Hello": "World"}

# 2. URLs must use forward slashes (/) not backslashes (\)
@app.get("/categories")
def list_categories():
    rows = get_db().execute("SELECT * FROM categories").fetchall()
    return [dict(row) for row in rows] # Převod na JSON

@app.get("/categories/{categories_id}")
def list_category(categories_id: int):
    # 3. Fixed SQL parameter syntax (:id and {"id": categories_id})
    row = get_db().execute(
        "SELECT * FROM categories WHERE id = :id",
        {"id": categories_id}
    ).fetchone()
    
    # 4. The 'if' check must happen BEFORE the 'return' statement
    # Also, Python uses 'None', not 'NONE'
    if row is None:
        raise HTTPException(
            status_code=404, detail=f"Category with id {categories_id} not found"
        )
        
    return dict(row)

# Přidání nebo změna data
class Category(BaseModel):
    name: str = Field(min_length=1, max_length=50, examples=["Auta"])

@app.post("/categories")
def create_category(category: Category): # 5. Fixed type hinting
    db = get_db()
    cursor = db.execute(
        "INSERT INTO categories (name) VALUES (:name)",
        {"name": category.name}
    )
    db.commit()
    
    # 6. return dict(row) won't work on an INSERT, so we return the new data
    return {"id": cursor.lastrowid, "name": category.name}