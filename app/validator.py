FORBIDDEN_KEYWORDS = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", ";--"]

def validate_sql(sql: str):
    if sql == "INVALID":
        raise ValueError("Unable to generate SQL for this query")

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword.lower() in sql.lower():
            raise ValueError("Unsafe SQL detected")

    if not sql.strip().lower().startswith("select"):
        raise ValueError("Only SELECT queries are allowed")
