# mtgclassifier

Unfinished project intended to apply NLP tecniques to predict Magic the Gathering card colors based on a number of text attributes.

Relevant Files:

data.py uses mtgsdk API to generate a CSV with all relevant card content

clean.py is testing ground for data cleaning, feature engineering and inital models.

Progress: Created initial train/test split. Encoded target variables, applied a count vectorizer to the predictors.
  Created duplicate sets of train and test data and applied tf-IDF vectorizer to one and n-gram vectorizer to the second.
  
 Next step: Run initial set of models. Use results to inform focus for next set of data analysis.

