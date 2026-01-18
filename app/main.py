from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.database import engine
from app.sql_generator import generate_sql_from_nl
from app.validator import validate_sql
from app.schemas import NLQueryRequest, SQLResponse

app = FastAPI(title="NL to SQL Analytics Engine")

@app.post("/query", response_model=SQLResponse)
def run_query(request: NLQueryRequest):
    sql = generate_sql_from_nl(request.question)

    try:
        validate_sql(sql)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = [dict(row._mapping) for row in result]

    return {"sql": sql, "result": rows}
