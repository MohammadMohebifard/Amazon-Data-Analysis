import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/amazon.csv")

df = df.dropna(subset=["product_name", "rating", "rating_count"])

df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")

df["popularity_score"] = df["rating"] * df["rating_count"]

top_products = df.groupby("product_name").agg({
    "rating_count": "sum",
    "rating": "mean",
    "popularity_score": "sum"
}).sort_values(by="popularity_score", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.barh(top_products.index[::-1], top_products["popularity_score"][::-1], color="#FF52A2")
plt.xlabel("Popularity Score (Rating × Rating Count)")
plt.title("Top 10 Most Popular Products on Amazon")
plt.tight_layout()
plt.show()
