def generate_sql_from_nl(question: str) -> str:
    """
    Converts natural language to SQL.
    This simulates AI output (replace with OpenAI API if needed).
    """

    q = question.lower()

    if "total revenue" in q:
        return "SELECT SUM(revenue) AS total_revenue FROM sales;"

    if "revenue by region" in q:
        return "SELECT region, SUM(revenue) FROM sales GROUP BY region;"

    if "top product" in q:
        return """
        SELECT product, SUM(revenue) AS total
        FROM sales
        GROUP BY product
        ORDER BY total DESC
        LIMIT 1;
        """

    return "INVALID"
