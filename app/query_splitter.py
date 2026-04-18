def split_query(query: str):
    query = query.lower().strip()

    # split on 'and'
    if " and " in query:
        parts = query.split(" and ")
        return [p.strip() for p in parts if p.strip()]

    return [query]