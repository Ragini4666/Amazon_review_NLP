# Sentiment Analysis on Amazon Customer Reviews Using NLP
## Importing Necessary Libraries:
Here, we import all the necessary libraries required for sentiment analysis and data processing
## Read the Datasets:
The dataset containing Amazon customer reviews is imported for analysis.
## Basic Exploratory Data Analysis(EDA):
Perform basic EDA, such as checking the dataset's shape, identifying null values, and reviewing general information about the dataset.In this it shows the rating field how much percentage occurs in the dataset
## Divide the Dataset as Train and Test datasets:
The dataset is split into training and testing sets using the train_test_split function for model evaluation.

## TFIDF [Term Frequency Inverse Document Frequency] FEATURES:
Convert the text data into numerical features using TfidfVectorizer or CountVectorizer.
## Train the Model:
In this , Choose and train a machine learning classifier, such as Logistic Regression, Random Forest,  MultiNomialNB, or SVM.
## Evaluate the Model:
in this, to use metrics like accuracy, precision, recall, and F1-score to evaluate performance.
## Final Report
Better accuracy results are achieved with Random Forest Classifier and Support Vector Machines (SVC), both ranging are near as 90%."
## Make Predictions:
Predict the sentiment of new or unseen text.
In that , to train the data and Perform sentiment Analysis of Text,
1.Exploring the Keyword name Column

2.text Data Preprocessing

3.Tokenization of the dataset

4.Stopwords Removal in the dataset

5.Stemming and lemmatization are done in the dataset

6.Bag of words in the dataset

## Final
The final_score(reviews) function should process the input by first passing it through the clean_text function, calculate the polarity scores using the SentimentIntensityAnalyzer, and then return the final sentiment analysis result based on the user's entered review in the text box.

 It calculates polarity scores using the SentimentIntensityAnalyzer and returns the final sentiment analysis result, including positive, negative, neutral, and compound scores. The sentiment scores are also integrated into the dataset for further analysis.








