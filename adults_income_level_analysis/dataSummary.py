from ucimlrepo import fetch_ucirepo
import pandas as pd
def dataSummary():
    """
    Fetch and summarize the Adult Income dataset from the UCI Database.

    Returns:
    - pd.DataFrame: The Adult Income dataset.
    """
    print("Data Summary Starts here....")
    print("""
    I picked the data from subset of adult income levels data set from UCI Database.
    
    \nMy data contains 48842 observations and 15 attributes.
    
    \nAttributes:
    
    \n1.age : Age
    \n2.workclass : workclass of the individual
    \n3.fnlwgt
    \n4.education : education level
    \n5.education num : unique identification number
    \n6.marital-status
    \n7.Occupation
    \n8.Race
    \n9.sex
    \n10.capital-gain
    \n11.capital-loss
    \n12.hours-per-week
    \n13.native country
    \n14.income (range)
    \n15.Relationship""")
    # fetch dataset
    adult = fetch_ucirepo(id=2)
    print("Fetching the dataset")
    print("concatenating the data set of both features and the target variable making the complete data set")
    adult_df = pd.concat([adult.data.features, adult.data.targets], axis=1)
    #adult_df.to_csv("adults.csv")
    print("Displaying the information")
    print(adult_df)
    print("Here can see that there are 48842 observations and 15 columns in the dataset.")
    print(adult_df.dtypes)
    print("Above results shows the data types of al attributes in the dataset.")
    print(adult_df.shape)
    print("Data set has 48842 observations and 15 attributes")
    print("Data Summary Ends here....")
    return adult_df


