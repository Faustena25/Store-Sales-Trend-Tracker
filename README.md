# 🛒 Store Sales Trend Tracker with Visual Reports

**Domain:** Retail and Sales  
**Subject:** Python for Data Science Lab  
**Institution:** CHRIST (Deemed to be University), Bengaluru

---

## 👥 Group Members

| Name | Register No. |
|------|-------------|
| Abinesh S | 2548302 |
| Faustena S | 2548313 |
| Kathiravan A | 2548317 |
| Mugunthan T | 2548322 |
| Vishwa Karthick S | 254834 |

---

## 📌 Problem Statement

Record daily sales transactions with product details, quantity, and revenue. Use **Pandas** to calculate sales totals, identify peak days, and generate pivot table summaries. Visualize category-wise sales using **pie charts** and top products using **bar charts**.

---

## 📁 Project Structure

```
store-sales-tracker/
│
├── sales_analyzer.py        # Main analysis & visualization script
├── retail_sales_dataset.csv # Dataset (add your own)
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 📊 Dataset

The dataset (`retail_sales_dataset.csv`) contains the following columns:

| Column | Description |
|--------|-------------|
| `Date` | Transaction date |
| `Product Category` | Category (Beauty, Clothing, Electronics) |
| `Quantity` | Units purchased |
| `Total Amount` | Revenue from the transaction |
| `Gender` | Customer gender |
| `Age` | Customer age |

> You can use the [Retail Sales Dataset](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset) from Kaggle.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/store-sales-tracker.git
cd store-sales-tracker
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your dataset
Place `retail_sales_dataset.csv` in the project root folder.

### 4. Run the script
```bash
python sales_analyzer.py
```

---

## 📈 Features & Outputs

### 🔢 Sales Summary (KPIs)
| Metric | Value |
|--------|-------|
| Total Revenue | ₹4,56,000 |
| Average Transaction Value | ₹456.00 |
| Total Transactions | 1,000 |
| Total Quantity Sold | 2,514 |

### 📅 Peak Sales Days (Top 5)
| Date | Total Amount |
|------|-------------|
| 2023-05-23 | ₹8,455 |
| 2023-05-16 | ₹7,260 |
| 2023-06-24 | ₹6,220 |
| 2023-02-17 | ₹5,890 |
| 2023-08-05 | ₹5,205 |

### 📊 Visualizations Generated

| Chart | Description |
|-------|-------------|
| 🥧 **Pie Chart** | Sales distribution by Product Category |
| 📊 **Bar Chart** | Top product categories by revenue |
| 📈 **Line Chart** | Daily sales trend (Jan 2023 – Jan 2024) |
| 📊 **Bar Chart** | Monthly sales summary |
| 🥧 **Pie Chart** | Sales distribution by Gender (51.1% Female / 48.9% Male) |
| 📊 **Bar Chart** | Sales by Age Group |
| 🔵 **Scatter Plot** | Quantity vs Total Amount |
| 📊 **Histogram** | Distribution of transaction amounts |
| 〰️ **KDE Plot** | Smoothed density of transaction amounts |

---

## 🔍 Key Insights

- **Electronics** leads revenue at **34.4%**, closely followed by **Clothing (34.1%)** and **Beauty (31.5%)**.
- **May** is the highest-revenue month; **September** is the lowest.
- **Female** customers account for a slightly higher share of purchases (**51.1%**).
- The **50–60 age group** is the top-spending demographic.
- Most transactions are **low-value** (below ₹250), with a right-skewed distribution visible in the histogram and KDE plot.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `pandas` | Data loading, aggregation, pivot tables |
| `numpy` | Numerical operations |
| `matplotlib` | Charts and plots |
| `seaborn` | KDE visualization |

---

## 📦 Requirements

See [`requirements.txt`](requirements.txt)

---

## 📄 License

This project is submitted as part of academic coursework at CHRIST (Deemed to be University). For educational use only.
