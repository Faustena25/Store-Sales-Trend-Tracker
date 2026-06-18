"""
Store Sales Trend Tracker with Visual Reports
Domain: Retail and Sales

Group Members:
    - Abinesh S      (2548302)
    - Faustena S     (2548313)
    - Kathiravan A   (2548317)
    - Mugunthan T    (2548322)
    - Vishwa Karthick S (254834)

Description:
    Records daily sales transactions with product details, quantity, and revenue.
    Uses Pandas to calculate sales totals, identify peak days, and generate pivot
    table summaries. Visualizes category-wise sales using pie charts and top
    products using bar charts.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesAnalyzer:
    """End-to-end retail sales analysis and visualization."""

    def __init__(self, file_path: str):
        """
        Load and preprocess the retail sales dataset.

        Args:
            file_path (str): Path to the CSV file.
        """
        self.df = pd.read_csv(file_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Month'] = self.df['Date'].dt.month
        self.df['DayOfWeek'] = self.df['Date'].dt.day_name()
        self.df['Quarter'] = self.df['Date'].dt.quarter

    # ------------------------------------------------------------------ #
    #  Summary & Aggregations                                              #
    # ------------------------------------------------------------------ #

    def get_sales_summary(self) -> dict:
        """Return high-level KPIs for the dataset."""
        return {
            'Total Revenue': self.df['Total Amount'].sum(),
            'Average Transaction Value': self.df['Total Amount'].mean(),
            'Total Transactions': len(self.df),
            'Total Quantity Sold': self.df['Quantity'].sum(),
        }

    def get_daily_sales(self) -> pd.DataFrame:
        """Aggregate total sales amount per calendar day."""
        return (
            self.df.groupby('Date')['Total Amount']
            .sum()
            .reset_index()
        )

    def get_peak_days(self, n: int = 10) -> pd.DataFrame:
        """
        Return the top-n highest-revenue days.

        Args:
            n (int): Number of peak days to return. Default is 10.
        """
        daily_sales = self.get_daily_sales()
        return daily_sales.nlargest(n, 'Total Amount')

    # ------------------------------------------------------------------ #
    #  Pivot Tables                                                        #
    # ------------------------------------------------------------------ #

    def create_category_pivot(self) -> pd.DataFrame:
        """Pivot: Product Category × Month → Total Amount."""
        return pd.pivot_table(
            self.df,
            values='Total Amount',
            index='Product Category',
            columns='Month',
            aggfunc='sum',
            fill_value=0,
        )

    def create_gender_pivot(self) -> pd.DataFrame:
        """Pivot: Product Category × Gender → Total Amount."""
        return pd.pivot_table(
            self.df,
            values='Total Amount',
            index='Product Category',
            columns='Gender',
            aggfunc='sum',
            fill_value=0,
        )

    # ------------------------------------------------------------------ #
    #  Visualizations                                                      #
    # ------------------------------------------------------------------ #

    def plot_category_sales(self) -> pd.Series:
        """Pie chart: sales share by product category."""
        category_sales = self.df.groupby('Product Category')['Total Amount'].sum()
        plt.figure(figsize=(6, 6))
        plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution by Product Category')
        plt.tight_layout()
        plt.show()
        return category_sales

    def plot_top_products(self, n: int = 10) -> pd.Series:
        """
        Bar chart: top-n product categories by revenue.

        Args:
            n (int): Number of categories to display. Default is 10.
        """
        top_categories = (
            self.df.groupby('Product Category')['Total Amount']
            .sum()
            .nlargest(n)
        )
        plt.figure(figsize=(8, 6))
        top_categories.plot(kind='bar')
        plt.title(f'Top {n} Product Categories by Revenue')
        plt.xlabel('Product Category')
        plt.ylabel('Total Revenue')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        return top_categories

    def plot_daily_sales_trend(self) -> pd.DataFrame:
        """Line chart: daily sales trend over time."""
        daily_sales = self.get_daily_sales()
        plt.figure(figsize=(12, 5))
        plt.plot(daily_sales['Date'], daily_sales['Total Amount'])
        plt.title('Daily Sales Trend')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        return daily_sales

    def plot_monthly_sales(self) -> pd.Series:
        """Bar chart: total sales per month."""
        monthly_sales = self.df.groupby('Month')['Total Amount'].sum()
        plt.figure(figsize=(8, 5))
        monthly_sales.plot(kind='bar')
        plt.title('Monthly Sales Summary')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()
        return monthly_sales

    def plot_gender_sales(self) -> pd.Series:
        """Pie chart: sales split by gender."""
        gender_sales = self.df.groupby('Gender')['Total Amount'].sum()
        plt.figure(figsize=(6, 6))
        plt.pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution by Gender')
        plt.tight_layout()
        plt.show()
        return gender_sales

    def plot_age_group_sales(self) -> pd.Series:
        """Bar chart: total sales by customer age group."""
        self.df['Age'] = pd.to_numeric(self.df['Age'], errors='coerce')  # fix: missing closing parenthesis
        bins = [0, 20, 30, 40, 50, 60, 100]
        labels = ['<20', '20-30', '30-40', '40-50', '50-60', '60+']
        self.df['Age Group'] = pd.cut(self.df['Age'], bins=bins, labels=labels)
        age_sales = self.df.groupby('Age Group')['Total Amount'].sum()
        plt.figure(figsize=(8, 5))
        age_sales.plot(kind='bar')
        plt.title('Sales by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()
        return age_sales

    def plot_scatter_sales(self) -> None:
        """Scatter plot: quantity purchased vs. transaction amount."""
        plt.figure(figsize=(8, 6))
        plt.scatter(self.df['Quantity'], self.df['Total Amount'], alpha=0.6)
        plt.title('Scatter Plot: Quantity vs Total Amount')
        plt.xlabel('Quantity')
        plt.ylabel('Total Amount')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_histogram_sales(self) -> None:
        """Histogram: distribution of individual transaction amounts."""
        plt.figure(figsize=(8, 6))
        plt.hist(self.df['Total Amount'], bins=30, alpha=0.7, edgecolor='black')
        plt.title('Histogram of Total Sales Amount')
        plt.xlabel('Total Amount')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

    def plot_kde_sales(self) -> None:
        """KDE plot: smoothed density of transaction amounts."""
        plt.figure(figsize=(8, 6))
        sns.kdeplot(self.df['Total Amount'], fill=True)
        plt.title('KDE Plot of Total Sales Amount')
        plt.xlabel('Total Amount')
        plt.ylabel('Density')
        plt.tight_layout()
        plt.show()


# ------------------------------------------------------------------ #
#  Main Execution                                                      #
# ------------------------------------------------------------------ #

if __name__ == '__main__':
    FILE_PATH = 'retail_sales_dataset.csv'   # update path if needed

    analyzer = SalesAnalyzer(FILE_PATH)

    # --- KPI Summary ---
    summary = analyzer.get_sales_summary()
    print("=" * 40)
    print("           SALES SUMMARY")
    print("=" * 40)
    for key, value in summary.items():
        print(f"  {key:<30}: {value:>12,.2f}")

    # --- Peak Days ---
    peak_days = analyzer.get_peak_days(5)
    print("\nTop 5 Peak Sales Days:")
    print(peak_days.to_string(index=False))

    # --- Pivot Tables ---
    category_pivot = analyzer.create_category_pivot()
    print("\nCategory-wise Monthly Sales Pivot Table:")
    print(category_pivot)

    gender_pivot = analyzer.create_gender_pivot()
    print("\nCategory-wise Gender Sales Pivot Table:")
    print(gender_pivot)

    # --- Charts ---
    analyzer.plot_category_sales()
    analyzer.plot_top_products()
    analyzer.plot_daily_sales_trend()
    analyzer.plot_monthly_sales()
    analyzer.plot_gender_sales()
    analyzer.plot_age_group_sales()
    analyzer.plot_scatter_sales()
    analyzer.plot_histogram_sales()
    analyzer.plot_kde_sales()
