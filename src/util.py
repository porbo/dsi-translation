import pandas as pd

def conv_per_country(df):
    """
    input: full dataframe with all users and their countries
    
    print out each country, number of users from that country, and conversion percentages for test and control groups
    """
    for country in df['country'].unique():
        filtered = df[df['country'] == country]
        test = filtered[filtered['test'] == 1]
        control = filtered[filtered['test'] == 0]
        print(country, ':\ttest:\t', test['conversion'].mean(), '\tcontrol:\t', control['conversion'].mean(), '\tcount:\t',filtered.shape[0])
