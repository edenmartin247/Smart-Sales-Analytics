# Smart Sales Analytics Dashboard Using Python

An interactive data analytics dashboard built using Python and Streamlit to analyze sales, profit, products, regions, and business performance.

## Project Overview

The Smart Sales Analytics Dashboard is designed to analyze a SuperStore sales dataset and generate meaningful business insights.

The project includes data cleaning, exploratory data analysis (EDA), data visualization, and an interactive dashboard. Users can apply filters to explore sales and profit performance across different regions, categories, markets, and years.

## Dataset Information

- **Dataset Name:** SuperStoreOrders
- **Total Records:** 51,290
- **Total Columns:** 25
- **Data Format:** CSV
- **Data Processing:** Data cleaning and feature engineering

The dataset contains information about orders, customers, products, sales, profit, discounts, shipping, markets, and regions.

## Technology Stack

- **Python:** Main programming language
- **Pandas:** Data cleaning and data analysis
- **Streamlit:** Interactive dashboard development
- **Plotly:** Interactive charts and visualizations
- **Jupyter Notebook:** Exploratory Data Analysis (EDA)
- **Visual Studio Code:** Code editor

## Key Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Interactive KPI cards:
  - Total Sales
  - Total Profit
  - Total Orders
  - Average Order Value
  - Profit Margin
- Interactive dashboard filters:
  - Region
  - Category
  - Market
  - Year
- Interactive visualizations:
  - Sales by Category
  - Profit by Region
  - Monthly Sales Trend
  - Sales Distribution by Market

## 📁 Project Structure

```text
Smart-Sales-Analytics/
│
├── Data/
│   ├── Raw/
│   └── Processed/
│
├── dashboard/
│   └── app.py
│
├── README.md
└── ...
```

## How to Run the Project

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Create and activate a Python virtual environment.
4. Install the required libraries:

```bash
pip install pandas streamlit plotly
```

5. Run the Streamlit dashboard:

```bash
python -m streamlit run dashboard/app.py
```

6. Open the local URL displayed in the terminal to view the dashboard.

## Key Business Insights

- Total Sales: 12,642,905
- Total Profit: 1,469,034.82
- Total Orders: 25,035
- Average Order Value: 505.01
- Profit Margin: 11.62%

### Important Findings

- Technology generated the highest sales among the three product categories.
- The Tables subcategory recorded a negative total profit.
- APAC was the highest-performing market by sales.
- Sales increased from 2011 to 2014.
- Higher discount levels were frequently associated with negative profit.

## Future Improvements

- Add more advanced data visualizations.
- Include sales forecasting using machine learning.
- Add downloadable filtered reports.
- Improve dashboard design and user experience.
- Deploy the dashboard online.

## Author

**Eden Martin**

BCA (NEP) – Computer Science

Academic Project: Smart Sales Analytics Dashboard Using Python