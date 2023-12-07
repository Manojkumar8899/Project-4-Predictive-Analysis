import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def eda(data):
    print("Exploratory Data Analysis Starts here...")
    print("""To advance in this research section, we will begin by performing a comprehensive summary statistics analysis for 
    each of the variables. Our primary focus will be on detecting any potential outliers or missing values that might exert an 
    impact on our findings. Subsequently, we will supplement our analysis with visual representations for each attribute using 
    Seaborn and Matplotlib.""")
    print("Lets check for missing values in the data set")
    adult_df=data
    print(adult_df.isnull().sum())
    print("""As there were lot of missing values in columns namely workclass occupation and native country so instead of removing 
    these large number of values I will use data imputation techniques further after EDA""")
    print("There are some special characters in workclass column so I will replace it with Unknown")
    adult_df['workclass'] = adult_df['workclass'].replace('?', 'Unknown')
    print("Also in income level there are only two income levels but due a dot it made them into 4 levels sowe handle them")
    adult_df['income'] = adult_df['income'].replace('<=50K.', '<=50K')
    adult_df['income'] = adult_df['income'].replace('>50K.', '>50K')
    print("similarly for native country column")
    adult_df['native-country'] = adult_df['native-country'].replace('?', 'Unknown')
    print("we will check the statistical summary of the dataset")
    print(adult_df.describe())
    print("we will check the statistical summary of the dataset")
    print(adult_df.describe())
    print("""The describe() method provides a comprehensive set of summary statistics that includes the mean, maximum, minimum, 
    standard deviation, frequency counts, and quartile ranges. These statistics collectively offer valuable insights into the 
    distribution and characteristics of the dataset, enabling a deeper understanding of the data's distribution and variability.""")
    print(adult_df['age'].describe())
    print("The average age is 38 years old and minimum age is 17 years old and the maximum age is 90 years old.")
    plt.figure(figsize=(5, 5))
    plt.boxplot(adult_df['age'])
    plt.title('Boxplot for Age')
    plt.ylabel('Values')
    plt.show()
    print("It is evident that there are large number of outliers in the data")
    print("Work class")
    print(adult_df['workclass'].describe())
    print("There are 9 different work class people and totally we have 48842 instances of data")
    print("Sex")
    print(adult_df['sex'].describe())
    print("We have only male and female in the data and male has more instances of data.")
    print("Education")
    print(adult_df['education'].describe())
    print("It says that there were 16 different types of the education levels in the data and HS-Grad are the most common type of education level among the people")
    print(adult_df['marital-status'].describe())
    print("In total data contains 15 different types of occupation among the data and Prof-Speciality being the most common among the people.")
    print(adult_df['race'].describe())
    print("There are 5 types of races involved in the data and White being the most common race.")
    print("")
    print(adult_df['capital-gain'].describe())
    print("The average capital gain is 1079 USD and maximum being the 99999USd and Minimum is 0 USD")
    plt.figure(figsize=(5, 5))
    plt.boxplot(adult_df['capital-gain'])
    plt.title('Boxplot for capital-gain')
    plt.ylabel('Values')
    plt.show()
    print("Can see lot of outliers which might impact our analysis.")
    print("Age")
    print("""As we have age as numeric value to check the population age group in which people fall dividing age into age groups as below""")
    age_bins = [0, 5, 10, 15,20,25,30,35,40,45,50,55,60,65, float('inf')]
    age_labels = ['Under 5 ', '05-10', '10-15','15-20','20-25','25-30','30-35','35-40','40-45','45-50','50-55','55-60','60-65','65 and over']
    adult_df['age_group'] = pd.cut(adult_df['age'], bins=age_bins, labels=age_labels, right=False)
    print(adult_df['age_group'])
    print("""I have taken the age bins because if we have a age bin, its easier to analyse in which age range we have more income 
    levels and also helps us to understand the impact of age on income level.To avoid information loss, I have taken the small 
    age bins.""")
    # Set the figure size
    plt.figure(figsize=(14, 5))
    # Using Seaborn
    sns.barplot(data=adult_df, x=adult_df['age_group'].value_counts().index, y=adult_df['age_group'].value_counts())
    plt.title('Bar Plot of Age Group using Seaborn')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    # Show the Seaborn plot
    plt.show()
    # Using Matplotlib
    plt.figure(figsize=(14, 5))
    age_counts = adult_df['age_group'].value_counts()
    plt.bar(age_counts.index, age_counts)
    plt.title('Bar Plot of Age group using Matplotlib')
    plt.xlabel('Age group')
    plt.ylabel('Count')
    # Show the Matplotlib plot
    plt.show()
    print("""From above results most of the population fall under the age group 30-35 and 35-40 age ranges And Obviously 
    kids with age less than 15 years age cannot earn anything which resembles that data was authentic.""")
    print("Sex")
    # Set the figure size
    plt.figure(figsize=(5, 5))
    # Using Seaborn
    sns.barplot(data=adult_df, x=adult_df['sex'].value_counts().index, y=adult_df['sex'].value_counts())
    plt.title('Bar Plot of Sex using Seaborn')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    # Show the Seaborn plot
    plt.show()
    # Using Matplotlib
    plt.figure(figsize=(5, 5))
    age_counts = adult_df['sex'].value_counts()
    plt.bar(age_counts.index, age_counts)
    plt.title('Bar Plot of Sex using Matplotlib')
    plt.xlabel('Sex')
    plt.ylabel('Count')
    # Show the Matplotlib plot
    plt.show()
    print("""There is a skew in tha data that population in the data are mostly male and the populatin of females is very less and its a unbalanced data""")
    print("Race")
    # Set the figure size
    plt.figure(figsize=(10, 5))
    # Using Seaborn
    sns.barplot(data=adult_df, x=adult_df['race'].value_counts().index, y=adult_df['race'].value_counts())
    plt.title('Bar Plot of race using Seaborn')
    plt.xlabel('Race')
    plt.ylabel('Count')
    # Show the Seaborn plot
    plt.show()

    # Using Matplotlib
    plt.figure(figsize=(10, 5))
    age_counts = adult_df['race'].value_counts()
    plt.bar(age_counts.index, age_counts)
    plt.title('Bar Plot of Race using Matplotlib')
    plt.xlabel('Race')
    plt.ylabel('Count')
    # Show the Matplotlib plot
    plt.show()
    print("""Findings:
        \nThe data contains that most people are from White followed by the Black.From this we can say that data is authentic because as per the logic, legal immigrants like Asian-Pac and others will absolutely less as the legal immigrants on work in USA might be less.""")
    # Set the figure size
    print("Work Class")
    plt.figure(figsize=(15, 5))
    # Using Seaborn
    sns.barplot(data=adult_df, x=adult_df['workclass'].value_counts().index, y=adult_df['workclass'].value_counts())
    plt.title('Bar Plot of Workclass using Seaborn')
    plt.xlabel('Workclass')
    plt.ylabel('Count')
    # Show the Seaborn plot
    plt.show()

    # Using Matplotlib
    plt.figure(figsize=(15, 5))
    age_counts = adult_df['workclass'].value_counts()
    plt.bar(age_counts.index, age_counts)
    plt.title('Bar Plot of Workclass using Matplotlib')
    plt.xlabel('Workclass')
    plt.ylabel('Count')
    # Show the Matplotlib plot
    plt.show()
    print("""Findings
        \nIt is clear that most people working in private organization followed by the Self Employment.""")
    print("Education level")
    # Set the figure size
    plt.figure(figsize=(18, 5))
    # Using Seaborn
    sns.barplot(data=adult_df, x=adult_df['education'].value_counts().index, y=adult_df['education'].value_counts())
    plt.title('Bar Plot of Education using Seaborn')
    plt.xlabel('Education')
    plt.ylabel('Count')
    # Show the Seaborn plot
    plt.show()

    # Using Matplotlib
    plt.figure(figsize=(18, 5))
    age_counts = adult_df['education'].value_counts()
    plt.bar(age_counts.index, age_counts)
    plt.title('Bar Plot of Education using Matplotlib')
    plt.xlabel('Education')
    plt.ylabel('Count')
    # Show the Matplotlib plot
    plt.show()
    print("""Findings:
        \nThe people with education level HS-Grad are very high compared to the Some college level education and then Bachelors.People are less interested in higher studies like Masters , Doctorate etc""")
    print("Marital Status")
    # Set the figure size
    plt.figure(figsize=(18, 5))
    # Using Seaborn
    sns.barplot(data=adult_df, x=adult_df['marital-status'].value_counts().index, y=adult_df['marital-status'].value_counts())
    plt.title('Bar Plot of marital-status using Seaborn')
    plt.xlabel('marital-status')
    plt.ylabel('Count')
    # Show the Seaborn plot
    plt.show()

    # Using Matplotlib
    plt.figure(figsize=(18, 5))
    age_counts = adult_df['marital-status'].value_counts()
    plt.bar(age_counts.index, age_counts)
    plt.title('Bar Plot of marital-status using Matplotlib')
    plt.xlabel('marital-status')
    plt.ylabel('Count')
    # Show the Matplotlib plot
    plt.show()
    print("""Findings:\n
        Married-civ-spouse are the majority marital status who were working and then followed by the Never marries who are Unmarried people.""")
    print("Hours Per week")
    avg_hours=adult_df.groupby('age_group')['hours-per-week'].mean().reset_index()
    print(avg_hours)
    plt.figure(figsize=(14, 5))

    # Using Seaborn
    sns.barplot(data=avg_hours, x='age_group', y='hours-per-week')
    plt.title('Average Hours per Week Worked by Age Group (Seaborn)')
    plt.xlabel('Age Group')
    plt.ylabel('Average Hours per Week')

    # Show the Seaborn plot
    plt.show()

    # Using Matplotlib
    plt.figure(figsize=(14, 5))
    plt.bar(avg_hours['age_group'], avg_hours['hours-per-week'])
    plt.title('Average Hours per Week Worked by Age Group (Matplotlib)')
    plt.xlabel('Age Group')
    plt.ylabel('Average Hours per Week')
    # Show the Matplotlib plot
    plt.show()
    print("""Findings:
        The people from age ranging from 35 to 55 were working more hours compared to other age groups.""")

    print("Income Level")
    # Set the figure size
    plt.figure(figsize=(12, 6))

    # Using Seaborn
    sns.barplot(
        x=adult_df['income'].value_counts().index,
        y=adult_df['income'].value_counts(normalize=True) * 100  # Normalize counts to percentages
    )
    plt.title('Bar Plot of Income using Seaborn')
    plt.xlabel('Income')
    plt.ylabel('Percentage')
    plt.show()

    # Using Matplotlib
    plt.figure(figsize=(12, 6))
    income_percentage = adult_df['income'].value_counts(normalize=True) * 100
    plt.bar(income_percentage.index, income_percentage)
    plt.title('Bar Plot of Income using Matplotlib')
    plt.xlabel('Income')
    plt.ylabel('Percentage')
    plt.show()
    print("""Findings:\n
        Most of the people have income level <=50K USD per year as per the above analysis as 70% of the people fall 
        under <=50K income level.""")
    return adult_df
