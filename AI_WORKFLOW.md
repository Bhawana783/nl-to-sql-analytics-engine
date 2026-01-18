# AI-Assisted Development Workflow

## 1. AI SQL Generation
Used AI tools (ChatGPT / Copilot) to convert natural language analytics questions into SQL queries.

Example AI Output:
SELECT * FROM sales;

## 2. Rejected Queries
- Queries containing DELETE, DROP, UPDATE
- Queries without GROUP BY for aggregation
- Queries returning unnecessary columns

## 3. Manual Review & Optimization
- Enforced SELECT-only queries
- Added aggregation logic manually
- Limited results where required
- Implemented SQL validation layer

## 4. Final Outcome
AI was used as a productivity tool, not a source of truth.
All SQL logic was reviewed, tested, and secured manually.
