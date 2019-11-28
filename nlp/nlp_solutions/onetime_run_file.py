###################################################################
########             One time run file .             #############
###################################################################

""" 

    onetime_run_file.py
    
    This file contains the codes that need to be run one time depending on how you change the data. 
    
    To run this code navigate to the folder and then execute the following command in terminal (command prompt)
    
    python onetime_run_file.py
    
    It will create a "onetime.txt" pickle file which will be later used by the bot to tune the nlp search.
    
"""

from sklearn.externals import joblib
import pandas as pd
import os,sys
sys.path.append(os.path.normpath(os.getcwd()))

from config import onetime_file
from nlplearn import *

if __name__ == "__main__":
    
    metadata = pd.read_csv('data/metadata_prep.csv')
    
    ###################################################################
    ########      Metadata based collobarative filtering  #############
    ###################################################################    
    
    documents = metadata['overview'].fillna('')
    cosine_sim = metadata_filtering(documents)
    indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
    
    ###################################################################
    ########      Title search based on Keywords  #############
    ###################################################################
    
    documents = list(metadata['title'].fillna(''))
    tfidf_fit, tfidf_matrix = tfidf_fit(documents)
    
    ###################################################################
    ########       dump the variables to a text file      #############
    ###################################################################
    
    i = [cosine_sim,indices,tfidf_fit, tfidf_matrix]
    joblib.dump(i,onetime_file)
    
    