from pydantic import BaseModel

class NLQueryRequest(BaseModel):
    question: str

class SQLResponse(BaseModel):
    sql: str
    result: list
