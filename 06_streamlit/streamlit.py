%%writefile streamlit.py # Not sure if this line is necessary

import pandas as pd
import numpy as np
import streamlit as streamlit
import matplotlib.pyplot as plt

import streamlit.components.v1 as components
import zipfile

import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB




st.title('The Tasting Game')

# Creating a function that loads in csv data
@st.cache
def load_data():
    cab_pinot_df = pd.read_cvs('../data/004_cab_pinot.csv')
    return wine_df

@st.cache
def load_test_csv()

#### Preprocessing User Input #####

##  Creating a text box for users to input their wine tasting notes ##
# This takes in a single line of text.
# the default value is optional, I may just eliminate it.
user_input = st.text_input('label goes here', default_value_goes_here)

# This takes in a multi-line of text.
# More info can be found here: https://discuss.streamlit.io/t/how-to-take-text-input-from-a-user/187
user_input_multi = st.text_area('label goes here', default_value_goes_here)

### NOTE ####
# May have to consider running user_input through preprocessing steps like stop_word removal and data cleaning.


### Making Predictions ###

def user_input_processor(user_input):

    


prediction = mnb.predict(user_input)
