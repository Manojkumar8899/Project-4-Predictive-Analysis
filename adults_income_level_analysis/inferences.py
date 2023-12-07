import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def inferences(data):
    """
    Generate and visualize inferences from the provided dataset.

    Parameters:
    - data (pd.DataFrame): The input dataset.

    Returns:
    None
    """
    print("""Inference1: 1.Is there evidence of a gender pay gap within this dataset? Analyze income data to determine whether there is a significant difference in earnings between males and females.""")
    adult_df=data
    print(adult_df.groupby(['sex', 'income']).size().unstack())
    # Grouping by 'sex' and 'income', and unstacking the result
    grouped_data = adult_df.groupby(['sex', 'income']).size().unstack()
    # Calculating percentages within each gender category
    percentage_data = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100
    # Plotting with Seaborn
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    sns.barplot(x=percentage_data.index, y=percentage_data['<=50K'], label='<=50K')
    sns.barplot(x=percentage_data.index, y=percentage_data['>50K'], bottom=percentage_data['<=50K'], label='>50K')
    plt.title('Income Distribution by Gender (Seaborn)')
    plt.xlabel('Gender')
    plt.ylabel('Percentage')
    plt.legend(title='Income')
    plt.show()
    # Plotting with Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(percentage_data.index, percentage_data['<=50K'], label='<=50K')
    plt.bar(percentage_data.index, percentage_data['>50K'], bottom=percentage_data['<=50K'], label='>50K')
    plt.title('Income Distribution by Gender (Matplotlib)')
    plt.xlabel('Gender')
    plt.ylabel('Percentage')
    plt.legend(title='Income')
    plt.show()
    print("""There is gender pay gap as can observe that more people in income level >50k are males very huge difference in the pay""")
    print(adult_df.groupby(['sex', 'income'])['capital-gain'].mean().unstack())
    # Grouping by 'sex' and 'income', and unstacking the result to get the mean capital gain
    grouped_data = adult_df.groupby(['sex', 'income'])['capital-gain'].mean().unstack()

    # Plotting with Seaborn
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    sns.barplot(x=grouped_data.index, y=grouped_data['<=50K'], label='<=50K')
    sns.barplot(x=grouped_data.index, y=grouped_data['>50K'], bottom=grouped_data['<=50K'], label='>50K')
    plt.title('Mean Capital Gain by Gender and Income (Seaborn)')
    plt.xlabel('Gender')
    plt.ylabel('Mean Capital Gain')
    plt.legend(title='Income')
    plt.show()

    # Plotting with Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_data.index, grouped_data['<=50K'], label='<=50K')
    plt.bar(grouped_data.index, grouped_data['>50K'], bottom=grouped_data['<=50K'], label='>50K')
    plt.title('Mean Capital Gain by Gender and Income (Matplotlib)')
    plt.xlabel('Gender')
    plt.ylabel('Mean Capital Gain')
    plt.legend(title='Income')
    plt.show()
    print("""But in terms of the capital gain Females has higher capital gain who fall under income level >50k but in income range <=50k males are has the upper hand""")
    print("Inference2: 2.Investigate whether individuals with higher education levels tend to achieve greater income mobility and assess the extent to which education is a predictor of income growth.")
    # Calculate the count of individuals in each income category for each education level
    income_count_by_education = adult_df.groupby(['education', 'income'])['education'].count().unstack()
    # Set the figure size
    plt.figure(figsize=(12, 6))

    # Create a bar plot to visualize the count of individuals in each income category by education level
    income_count_by_education.plot(kind='bar', stacked=True)
    plt.title('Income Category Distribution by Education Level')
    plt.xlabel('Education Level')
    plt.ylabel('Count')
    plt.legend(title='Income', title_fontsize='12')

    # Show the plot
    plt.show()
    print("""It is evident that people with higher education level doesnt assure to get higher income. Instead particularly people with Bachelors and High School Grads are mostly getting income level >50k""")
    print("Inference 3: 3.Do individuals working longer hours per week tend to earn higher incomes, or is there an optimal work-life balance that leads to better financial outcomes? Analyze the relationship between hours worked per week and income.")
    print(adult_df.groupby('income')['hours-per-week'].mean())
    # Grouping by 'income' and calculating the mean hours-per-week
    grouped_data = adult_df.groupby('income')['hours-per-week'].mean()

    # Plotting with Seaborn
    plt.figure(figsize=(8, 5))
    sns.barplot(x=grouped_data.index, y=grouped_data)
    plt.title('Mean Hours per Week by Income (Seaborn)')
    plt.xlabel('Income')
    plt.ylabel('Mean Hours per Week')
    plt.show()

    # Plotting with Matplotlib
    plt.figure(figsize=(8, 5))
    plt.bar(grouped_data.index, grouped_data)
    plt.title('Mean Hours per Week by Income (Matplotlib)')
    plt.xlabel('Income')
    plt.ylabel('Mean Hours per Week')
    plt.show()
    print("""Obviously people working more hours are more likely to fall under income level >50k which means that more working hours will definitely increase your income level but might effect work life balance badly.""")
    print("Inference4: Is there any trend in income level range among the different marital status?")
    # Create a count plot for income levels based on marital status
    plt.figure(figsize=(12, 6))
    sns.countplot(x='marital-status', hue='income', data=adult_df)
    plt.title('Income Level by Marital Status')
    plt.xlabel('Marital Status')
    plt.ylabel('Count')
    plt.legend(title='Income')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.show()
    print("People who were in a Married -CIV - Spouse has good income levels as we can see that more people has income level >50k compared to others.")
    print("EDA Ends here...")
