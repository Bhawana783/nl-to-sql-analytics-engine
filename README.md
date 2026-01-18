📄 See AI_WORKFLOW.md for details on AI-assisted development and manual review.
# nl-to-sql-analytics-engine
an AI-assisted backend service that converts natural language questions into safe, validated SQL queries and executes them on an analytics database. Demonstrates SQL mastery, backend analytics, prompt engineering, and critical review of AI-generated code using FastAPI and SQLAlchemy.

# NL to SQL Analytics Engine

An AI-assisted backend system that converts natural language questions into safe SQL queries
and executes them on an analytics database.

## What This Proves
- SQL mastery
- Backend analytics APIs
- AI prompt reasoning
- Secure SQL validation
- Manual AI review & correction

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy

## Features
- Natural language input
- AI-generated SQL
- Query validation
- Safe execution
- JSON API response

## Run Locally

```bash
pip install -r requirements.txt
sqlite3 analytics.db < sample_data/sales_data.sql
uvicorn app.main:app --reload
