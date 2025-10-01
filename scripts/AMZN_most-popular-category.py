import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("outputs/amazon.csv")

category_counts = df['category'].value_counts().sort_values(ascending=False)

top_categories = category_counts.head(10)

plt.figure(figsize=(10, 6))
plt.bar(top_categories.index, top_categories.values, color='skyblue', edgecolor='black')
plt.title('Top 10 Most Popular Amazon Product Categories')
plt.xlabel('Category')
plt.ylabel('Number of Products')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.show()
