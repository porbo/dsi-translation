import pandas as pd
import scipy.stats as scs

def conv_per_country(df):
    """
    input: full dataframe with all users and their countries
    
    print out each country, number of users from that country, and conversion percentages for test and control groups
    """
    for country in df['country'].unique():
        filtered = df[df['country'] == country]
        test = filtered[filtered['test'] == 1]
        control = filtered[filtered['test'] == 0]
        print(country, ':\n\ttest:\t', round(test['conversion'].mean(),5), '\tcontrol:\t', round(control['conversion'].mean(),5), '\tcount:\t',filtered.shape[0], '\tp-value:\t', round(scs.ttest_ind(test['conversion'], control['conversion'])[1], 5))

def df_filter(user, test):
    """
    input:
        user: dataframe of user info
        test: dataframe of info about the test
    output: merged dataframe, limited to people outside of spain who use the spanish option
    """
    df = test.merge(user, on = 'user_id', how = 'left')
    df2 = df[df['country'] != 'Spain']
    return df2[df2['browser_language'] == 'ES']

def ttest(df):
    """
    input: dataframe with a test column and a conversion column
    output: ttest, test, control 
        ttest:tuple results for conversion rates with and without the test 
        test: array of conversion results in test group
        control:array of conversion results in control group
    """
    test = df[df['test'] == 1]['conversion'].values
    control = df[df['test'] == 0]['conversion'].values
    return scs.ttest_ind(test, control), test, control
