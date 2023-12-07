import dataSumamry as ds
import eda
import inferences as infe
print("Introduction")
print("""Dataset I chosen is "Adults Income levels" taken from UCI Data Base which includes information such as age, work class, education level, marital status, occupation, relationship, race, sex, capital gain, hours per week, country of residence, and income range. Exploring this dataset presents an opportunity to gain invaluable insights into various societal and economic aspects, including the relationship between education and income, disparities in income across demographic categories, and how factors like age, work, and hours worked per week may influence one's financial well-being. EDA of this dataset will not only provide a deeper understanding of these interactions but may also offer critical perspectives on income inequality, gender pay gaps, and socio-economic mobility—essential topics for addressing economic disparities and formulating equitable policy solutions. The project will involve data visualization, statistical analysis, and the application of data-driven techniques to unravel the intricate relationships within this extensive dataset. Ultimately, the findings derived from this EDA can serve as a foundation for informed decision-making and policy recommendations in the realm of socio-economic dynamics.""")

print("Research Questions:")
print("""
\n1. Is there evidence of a gender pay gap within this dataset? Analyze income data to determine whether there is a significant difference in earnings between males and females.

\n2. Investigate whether individuals with higher education levels tend to achieve greater income mobility and assess the extent to which education is a predictor of income growth.

\n3. Do individuals working longer hours per week tend to earn higher incomes, or is there an optimal work-life balance that leads to better financial outcomes? Analyze the relationship between hours worked per week and income.

\n4. Is there any trend in income level range across demographic categories such as race, marital status, and country of residence.
""")
data=ds.dataSummary()
df=eda.eda(data)
infe.inferences(data)
print("""#5.Conclusion:\n
The analysis of the dataset reveals multifaceted patterns in income distribution, showcasing a 
pronounced gender pay gap with a higher prevalence of males in the >50k income bracket. Unexpectedly,
 while higher education levels do not uniformly translate to elevated incomes, individuals with 
 Bachelor's and High School education levels are more likely to surpass the 50k income threshold. 
 The correlation between extended work hours and higher income is evident, but the potential sacrifice 
 of work-life balance looms. Notably, marital status emerges as a key determinant, with those in stable 
 relationships, particularly "Married-civ-spouse," displaying higher income levels. Interestingly, 
 females in the >50k income category exhibit greater capital gains, offering a nuanced perspective on 
 financial success beyond salary. In navigating income dynamics, the findings underscore the need for 
 addressing gender disparities, reevaluating assumptions about education's impact, and recognizing the 
 intricate interplay of factors influencing income outcomes in individuals' lives.""")
print("References:")
print("""
\n1. https://archive.ics.uci.edu/dataset/2/adult

\n2. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html

\n3. https://www.bls.gov/careeroutlook/2018/data-on-display/education-pays.htm

\n4. https://docs.kanaries.net/articles/exploratory-data-analysis-python-pandas

\n5. https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html

\n6. https://machinelearningmastery.com/data-visualization-in-python-with-matplotlib-seaborn-and-bokeh/
""")

