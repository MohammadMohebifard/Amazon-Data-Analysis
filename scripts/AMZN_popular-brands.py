import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/amazon.csv")

df = df.dropna(subset=["product_name", "rating_count"])

df["rating_count"] = df["rating_count"].astype(str).str.replace(",", "")
df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")
df = df.dropna(subset=["rating_count"])

df["brand"] = df["product_name"].apply(lambda x: x.split()[0])

brand_popularity = df.groupby("brand")["rating_count"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.barh(brand_popularity.index[::-1], brand_popularity.values[::-1], color="#FF52A2")
plt.xlabel("Total Number of Ratings")
plt.title("Top 10 Most Popular Brands (Based on Ratings)")
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
