# Amazon Product Data Analysis

A Python project that analyzes Amazon product listings to explore the most popular products, brands, and categories based on customer ratings and review counts.

## Features

- Clean and preprocess Amazon product dataset
- Extract brand names from product titles
- Analyze and visualize:
  - Top 10 most reviewed products
  - Top 10 most popular brands (based on total review count)
  - Top 10 product categories (if available)
  - Most popular products based on a custom popularity score (rating × review count)
- Generate beautiful bar charts with matplotlib

## Technologies Used

- Python 3
- pandas
- NumPy
- matplotlib

## How to Run

1. (Optional) Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis scripts:
   ```bash
   # All scripts are inside the scripts/ folder
   python scripts/AMZN_most-popular-category.py
   python scripts/AMZN_number-of-reviews.py
   python scripts/AMZN_popular-brands.py
   python scripts/AMZN_Popular-Product.py
   ```

> Make sure your dataset file (e.g., `amazon.csv`) is located in the `data/` folder.

## Project Structure

```
Amazon-Data-Analysis/
├── data/                 # Raw dataset (e.g., amazon.csv)
├── outputs/              # Generated plots/images
├── scripts/              # Python analysis scripts
│   ├── AMZN_most-popular-category.py
│   ├── AMZN_number-of-reviews.py
│   ├── AMZN_popular-brands.py
│   └── AMZN_Popular-Product.py
├── requirements.txt      # Python dependencies
└── README.md             # Project overview and instructions
```

## Author

**Mohammad Mohebifard**  
Licensed under the MIT License.
