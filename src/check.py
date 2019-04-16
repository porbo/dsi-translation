import scipy.stats as scs
import pandas as pd
from src.util import ttest

def sig_by_country(user, test=None, alpha = .05, col = 'conversion'):
    """
    input:
        user:dataframe of user info. Alternatively, pass in the merged user/test dataframe instead of the separate dataframes
        test:dataframe of info about test
        alpha:float significance level for testing. default .05
        col:string name of column of interest, with values of 1 or 0. default 'conversion'

    output:bool
        Whether or not there's a significant difference between control and test groups, in the column of interest, in at least one country`
    """
    
    if 'test' in user:
        df = user
    else:
        df = test.merge(user, on = 'user_id', how = 'left')

    countries = df['country'].unique()
    #We're doing multiple tests, so we need to be more surprised before concluding anything.
    a = alpha/countries.shape[0]

    for country in countries:
        p = ttest(df[df['country'] == country])[0][1]
        try:
            if p < a: 
                return True
        except:
            print('ttest failed on country', country)
    return False

def total_vs_bycountry(user, test= None, alpha = .05, col = 'conversion'):
    """
    check whether the significance of a difference in the column of interest is consistent with checking significance country by country
    input:
        user:dataframe of user info. Or a merged dataframe of user and test info
        test:dataframe about tests. optional, if a merged dataframe is passed into 'user'
        alpha:float significance threshold. default .05
        col:string name of column of interest. should be 0 or 1. default 'conversion'
    output:bool
        
    """
    if 'test' in user:
        df = user
    else:
        df = test.merge(user, on = 'user_id', how = 'left')


    return (ttest(df)[0][1] < alpha) == sig_by_country(df, alpha = alpha, col = col)
