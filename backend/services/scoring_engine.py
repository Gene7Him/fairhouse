def compute_accountability_score(owner_name: str, last_sale_price: int) -> int:
    score = 100

    if "LLC" in owner_name.upper() or "CAPITAL" in owner_name.upper():
        score -= 20

    if last_sale_price > 800000:
        score -= 15

    if "TRUST" in owner_name.upper():
        score -= 10

    return max(score, 0)
