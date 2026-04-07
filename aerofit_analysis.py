


# Import statements
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Loading the data and printing the first few rows
raw_data = pd.read_csv('aerofit_treadmill_data.csv')

""" Printing summary statistics and checking for missing values
print(raw_data.head())
print(raw_data.dtypes)
print(raw_data.isnull().sum())
print(raw_data.describe())
"""
# Plots
# Boxplots for Age, Education, Income, and Miles by Product
fig, axes = plt.subplots(2, 4, figsize=(20, 10))
fig.suptitle('Buyer Profile by Product', fontsize=16)

# Continuous variables - box plots
sns.boxplot(data=raw_data, x='Product', y='Age', ax=axes[0, 0])
sns.boxplot(data=raw_data, x='Product', y='Income', ax=axes[0, 1])
sns.boxplot(data=raw_data, x='Product', y='Miles', ax=axes[0, 2])
sns.boxplot(data=raw_data, x='Product', y='Education', ax=axes[0, 3])

# Discrete / categorical variables
sns.boxplot(data=raw_data, x='Product', y='Usage', ax=axes[1, 0])
sns.boxplot(data=raw_data, x='Product', y='Fitness', ax=axes[1, 1])
sns.countplot(data=raw_data, x='Product', hue='Gender', ax=axes[1, 2])
sns.countplot(data=raw_data, x='Product', hue='MaritalStatus', ax=axes[1, 3])

plt.tight_layout()
plt.show()

# KDE plots for Age, Income, and Miles by Product 
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Distribution Comparison by Product', fontsize=16)

for col, ax in zip(['Income', 'Miles', 'Age'], axes):
    for product in raw_data['Product'].unique():
        sns.kdeplot(data=raw_data[raw_data['Product'] == product], 
                    x=col, label=product, ax=ax, fill=True, alpha=0.3)
    ax.set_title(col)
    ax.legend()

plt.tight_layout()
plt.show()

# Correlation heatmap for numerical variables
plt.figure(figsize=(10, 8))
sns.heatmap(raw_data.select_dtypes(include='number').corr(), 
            annot=True, cmap='coolwarm', fmt='.2f', 
            linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Correlation heatmap for numerical variables by Product - 40-80 limited sample size - unreliable; just for data inspection
"""
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

for ax, product in zip(axes, raw_data['Product'].unique()):
    subset = raw_data[raw_data['Product'] == product].select_dtypes(include='number')
    sns.heatmap(subset.corr(), annot=True, cmap='coolwarm', fmt='.2f',
                linewidths=0.5, vmin=-1, vmax=1, ax=ax)
    ax.set_title(f'{product} (n={len(subset)})')

plt.tight_layout()
plt.show()
"""

# Raw counts
ct_gender = pd.crosstab(raw_data['Product'], raw_data['Gender'], margins=True)
print(ct_gender)

# Conditional probability: P(Product | Gender)
# "Given someone is Male, what's the probability they bought each product?"
ct_gender_given = pd.crosstab(raw_data['Product'], raw_data['Gender'], normalize='columns')
print(ct_gender_given)

# Conditional probability: P(Gender | Product)  
# "Given someone bought KP781, what's the probability they are Male?"
ct_product_given = pd.crosstab(raw_data['Product'], raw_data['Gender'], normalize='index')
print(ct_product_given)

# Conditional probability: P(MaritalStatus | Product)  
# "Given someone bought KP781, what's the probability they are Married?"
ct_product_given = pd.crosstab(raw_data['Product'], raw_data['MaritalStatus'], normalize='index')
print(ct_product_given)

# Conditional probability: P(Product | MaritalStatus)  
# "Given someone's Marital Status what's the probability they bought KP781 ?"
ct_marital_given = pd.crosstab(raw_data['MaritalStatus'], raw_data['Product'], normalize='index')
print(ct_marital_given)

# Conditional probability: P(Fitness | Product)  
# "Given someone bought KP781, what's the probability for their Fitness?"
ct_product_given = pd.crosstab(raw_data['Product'], raw_data['Fitness'], normalize='index')
print(ct_product_given)



