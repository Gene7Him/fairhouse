import pandas as pd

def load_sample_properties():
    data = {
        "property_id": [1, 2, 3],
        "address": ["123 Main St", "456 Elm St", "789 Pine St"],
        "zip_code": ["94110", "90210", "60601"],
        "owner_name": ["XYZ Capital", "Jane Doe", "ACME LLC"],
        "last_sale_price": [850000, 600000, 450000],
        "sale_date": ["2020-06-01", "2021-01-15", "2019-11-20"]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/raw/sample_properties.csv", index=False)

if __name__ == "__main__":
    load_sample_properties()
