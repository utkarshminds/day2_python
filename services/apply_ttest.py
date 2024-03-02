
from scipy.stats import ttest_1samp
import streamlit as st 

def apply_ttest(dataframe_column):

    '''
    stats.ttest_1samp(rvs, popmean=0.5)
    TtestResult(statistic=2.456308468440, pvalue=0.017628209047638, df=49)

    '''
    results = ttest_1samp(dataframe_column, popmean=45, nan_policy='omit')

    st.write('Executing T Test')
    
    st.write('statistics =', results.statistic)
    st.write('pvalue =', results.pvalue)
    st.write('degree of freedom =', results.df)



