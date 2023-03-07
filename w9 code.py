import pandas as pd
from scipy.stats import ttest_ind
from IPython.core.display import display

#read our file
df = pd.read_excel('./LifeExp.xls')

display(df)

df.columns = df.columns.map(str)

import matplotlib.pyplot as plt

#create our histogram
plt.hist(df['2006'], bins= 20)
plt.title('Histogram of Mortality at age 65 in 2006')
plt.xlabel('Mortality after 65')
plt.ylabel('Frequency')
plt.show()

print(df.shape)

#shapiro 
from scipy.stats import shapiro

stat, p = shapiro(df['2006'])
print('Shapiro statistic:', stat)
print('Shapiro pvalue:', p)

if p < 0.05:
    print('Data is normally distributed')
else:
    print('Data is not nomally distributed')

#Kolmogorov smirnov
from scipy.stats import kstest
data = df['2006']

#performing KS test
statistic, pvalue = kstest (data, 'norm')
print('KS statistic:', statistic)
print('KS pvalue:', pvalue)

alpha = 0.05
if pvalue > alpha:
    print('Data is not nomally distributed')
else:
    print('Data is normally distributed')
    
    
#t-test
hammersmith_df = df[df['Local Authority'] == 'Hammersmith and Fulham']
hammersmith_df.columns = hammersmith_df.columns.map(str)

#create two subsets (that we want to compare)
mortality_2006 = hammersmith_df['2006']
mortality_2014 = hammersmith_df['2014']

#conduct t-test
t_test, p_val = ttest_ind(mortality_2006, mortality_2014)

#print results
print('T-statistic:',t_test)
print('P values:', p_val)

if p_val < 0.05:
    print('the means are statistically different')
else:
    print('the means are NOT statistically different')
    

#anova
from scipy.stats import f_oneway
#group data (2+)
grouped_data= df.groupby('Local Authority').mean()[['2006','2007','2008','2009',
                                                    '2010', '2011', '2012', '2013',
                                                    '2014']]

#conduct anova
anova_results = f_oneway(*[grouped_data[year] for year in grouped_data.columns])
print('One way ANOVA results:', anova_results)



from scipy.stats import chi2_contingency

#chi squared
df['quartile'] = pd.qcut(df['2006'], q=4, labels = ['Q1', 'Q2', 
                                                    'Q3', 'Q4'])
contingency_table = pd.crosstab(df['Local Authority'], df['quartile'])

#perform chisquared
chi2,p,dof, expected = chi2_contingency(contingency_table)

print('Chi squared results:')
print('Chi squared statistic= ', chi2)
print('pvalue:', p)

#variance
mortality_2006 = df.groupby('Local Authority')['2006'].mean()
mortality_2014 = df.groupby('Local Authority')['2014'].mean()

#perform f-test
f_stat, pvalue = f_oneway(mortality_2006,mortality_2014)

#print results
print("F statistic:", f_stat)
print("p value:", pvalue)