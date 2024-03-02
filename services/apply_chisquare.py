from scipy.stats import chisquare 
import streamlit as st


def apply_chisquare(dataframe_column):

    countTable = dataframe_column.value_counts()

    results = chisquare(countTable)

    st.write('Executing Chisquare Test')

    st.write('Statistics = ', results.statistic)

    st.write('pvalue = ', results.pvalue)