from sqlalchemy import text
from app.database import engine

SQL_STATEMENTS = """
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    region TEXT,
    revenue INTEGER,
    sale_date DATE
);

DELETE FROM sales;

INSERT INTO sales (product, region, revenue, sale_date) VALUES
('Laptop', 'India', 90000, '2024-01-10'),
('Phone', 'India', 40000, '2024-01-15'),
('Tablet', 'USA', 60000, '2024-02-01'),
('Laptop', 'USA', 120000, '2024-02-05'),
('Phone', 'India', 45000, '2024-02-20');
"""

with engine.connect() as conn:
    for stmt in SQL_STATEMENTS.split(";"):
        if stmt.strip():
            conn.execute(text(stmt))
    conn.commit()

print("✅ Database initialized with sample data")
