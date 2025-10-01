import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("outputs/amazon.csv")

df = df[['product_name', 'rating', 'rating_count']].copy()

df.dropna(subset=['product_name', 'rating', 'rating_count'], inplace=True)

df['rating'] = df['rating'].astype(str).str.replace(",", ".")
df['rating_count'] = df['rating_count'].astype(str).str.replace(",", "")

df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

df.dropna(subset=['rating', 'rating_count'], inplace=True)

agg_df = df.groupby('product_name').agg({
    'rating': 'mean',
    'rating_count': 'sum'
}).reset_index()

top_products = agg_df.sort_values(by='rating_count', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.barh(top_products['product_name'], top_products['rating'], color='teal')
plt.xlabel('Average Rating')
plt.title('Top 10 Most Rated Products on Amazon')
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.show()
