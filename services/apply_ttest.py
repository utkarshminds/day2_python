
from scipy.stats import ttest_1samp
import streamlit as st 
from openai import OpenAI

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

    

    APIKEY = st.secrets['OPEN_AI']['APIKEY']
    client = OpenAI(api_key=APIKEY)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are an expert in statistical hypothesis testing"
        },
        {
        "role": "user",
        "content": f"""Explain in simple words the results of t-test for a non-technical user. 
        You will be given the p-value and the t-test statistic as well as the variable name.
        p-value = {results.pvalue}
        t-test statistic = {results.statistic}
        """
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    #to get line
    answer = response.choices[0].message.content
    st.write(answer)

