Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_excel("C:\\Users\\Surendra Reddy\\Downloads\\1617fedschoolcodelist.xls")

# 2. Get info about the dataset
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# 3. Handling missing data
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# ✅ Replace deprecated method
df.ffill(inplace=True)  # forward fill missing values

# 4. Statistical Summary
print("\nSummary Statistics:")
print(df.describe(include='all'))

# 5. Number of Schools by State
print("\nTop 5 States by Number of Schools:")
print(df['StateCode'].value_counts().head())

# 📊 Bar Graph - Top 10 States by Number of Schools
plt.figure(figsize=(10, 6))
df['StateCode'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 States by Number of Schools")
plt.xlabel("State")
plt.ylabel("Number of Schools")
plt.tight_layout()
plt.show()

# 📈 Line Graph - School Count by State
state_counts = df['StateCode'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.plot(state_counts.index, state_counts.values, marker='o', color='green')
plt.title("School Count by State")
plt.xlabel("State")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# 🥧 Pie Chart - Top 5 States
top_states = df['StateCode'].value_counts().head(5)
plt.figure(figsize=(6, 6))
... plt.pie(top_states.values, labels=top_states.index, autopct='%1.1f%%')
... plt.title("Top 5 States by School Share")
... plt.tight_layout()
... plt.show()
... 
... # 🔥 Heatmap - Correlation between numeric columns
... numeric_data = df.select_dtypes(include=[np.number])
... if not numeric_data.empty:
...     plt.figure(figsize=(8, 6))
...     sns.heatmap(numeric_data.corr(), annot=True, cmap='Blues')
...     plt.title("Correlation Heatmap (Numeric Data)")
...     plt.tight_layout()
...     plt.show()
... 
... # 📦 Boxplots - Detect outliers
... for column in numeric_data.columns:
...     plt.figure(figsize=(6, 4))
...     sns.boxplot(y=df[column])
...     plt.title(f"Boxplot of {column}")
...     plt.tight_layout()
...     plt.show()
... 
... # 🔘 Scatter Plot - ZipCode vs Random values
... if 'ZipCode' in df.columns:
...     plt.figure(figsize=(8, 5))
...     plt.scatter(df['ZipCode'], np.random.rand(len(df)), alpha=0.5)
...     plt.title("Scatter Plot: ZipCode vs Random Values")
...     plt.xlabel("ZipCode")
...     plt.ylabel("Random Values")
...     plt.tight_layout()
...     plt.show()
... 
... # 🔄 Pair Plot - Visualize numeric features
... # if len(numeric_data.columns) >= 2:
...     sns.pairplot(numeric_data)
...     plt.title("Pair Plot")
...     plt.suptitle("Pair Plot of Numeric Features", y=1.02)
...     plt.tight_layout()
...     plt.show()
