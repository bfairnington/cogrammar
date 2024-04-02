"""
Capstone Project

In this task, you will develop a Python program that performs sentiment analysis
on a dataset of product reviews.

Follow these steps:

    ● Download a dataset of product reviews: Consumer Reviews of Amazon
    Products. You can save it as a CSV file, naming it:
    amazon_product_reviews.csv.

    ● Create a Python script, naming it: sentiment_analysis.py. Develop a Python
    script for sentiment analysis. Within the script, you will perform the
    following tasks using the spaCy library:

    1. Implement a sentiment analysis model using spaCy: Load the
    en_core_web_sm spaCy model to enable natural language processing
    tasks. This model will help you analyse and classify the sentiment of the
    product reviews.

    2. Preprocess the text data: Remove stopwords, and perform any
    necessary text cleaning to prepare the reviews for analysis.

        2.1. To select the 'review.text' column from the dataset and retrieve
        its data, you can simply use the square brackets notation. Here
        is the basic syntax:

        reviews_data = dataframe['review.text']

        This column, 'review.text,' represents the feature variable
        containing the product reviews we will use for sentiment
        analysis.

        2.2. To remove all missing values from this column, you can simply
        use the dropna() function from Pandas using the following
        code:

        clean_data = dataframe.dropna(subset=['reviews.text'])

    3. Create a function for sentiment analysis: Define a function that takes
    a product review as input and predicts its sentiment.

    4. Test your model on sample product reviews: Test the sentiment
    analysis function on a few sample product reviews to verify its accuracy
    in predicting sentiment.

    5. Write a brief report or summary in a PDF file:
    sentiment_analysis_report.pdf that must include:

        5.1. A description of the dataset used.

        5.2. Details of the preprocessing steps.

        5.3. Evaluation of results.

        5.4. Insights into the model's strengths and limitations.

Additional Instructions:

    ● Some helpful guidelines on cleaning text:

        ○ To remove stopwords, you can utilise the .is_stop attribute in spaCy.
        This attribute helps identify whether a word in a text qualifies as a
        stop word or not. Stopwords are common words that do not add
        much meaning to a sentence, such as "the", "is", and "of".
        Subsequently, you can then employ the filtered list of tokens or
        words(words with no stop words) for conducting sentiment analysis.

        ○ You can also make use of the lower(), strip() and str() methods to
        perform some basic text cleaning.

    ● You can use the spaCy model and the .sentiment attribute to analyse the
    review and determine whether it expresses a positive, negative, or neutral
    sentiment. To use the .polarity attribute, you will need to install the
    TextBlob library. You can do this with the following commands:

            ■ # Install spacytextblob
            ■ pip install spacytextblob

        ○ Textblob requires additional data before getting started, download the data
        using the following code:

            ■ python -m textblob.download_corpora

        ○ Once you have installed TextBlob, you can use the .sentiment and
        .polarity attribute to analyse the review and determine whether it
        expresses a positive, negative, or neutral sentiment. You can also
        incorporate this code to get yourself started:

            ■ # Using the polarity attribute
            ■ polarity = doc._.blob.polarity
            ■ # Using the sentiment attribute
            ■ sentiment = doc._.blob.sentiment

FYI: The underscore in the code just above is a Python convention for naming
private attributes. Private attributes are not meant to be accessed directly by the
user, but can be accessed through public methods.

    ● You can use the .polarity attribute to measure the strength of the
    sentiment in a product review. A polarity score of 1 indicates a very positive
    sentiment, while a polarity score of -1 indicates a very negative sentiment. A
    polarity score of 0 indicates a neutral sentiment.

    ● You can also use the similarity() function to compare the similarity of two
    product reviews. A similarity score of 1 indicates that the two reviews are
    more similar, while a similarity score of 0 indicates that the two reviews are
    not similar.

        ○ Choose two product reviews from the 'review.text' column and
        compare their similarity. To select a specific review from this column,
        simply use indexing, as shown in the code below:

        my_review_of_choice = data['reviews.text'][0]

        ○ The above code retrieves a review from the 'review.text' column at
        index 0. You can select two reviews of your choice using indexing.

        However, please be cautious not to use an index that is out of bounds,
        meaning it exceeds the number of data points or rows in our dataset.

    ● Include informative comments that clarify the rationale behind each line of
    code.
"""

# 1. Implement a sentiment analysis model using spaCy.

# Import libraries
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Define nlp
nlp = spacy.load("en_core_web_sm")


# 2. Preprocess the text data: Remove stopwords, and perform any necessary text cleaning to prepare the reviews for analysis.

# Import data
df = pd.read_csv('amazon_product_reviews.csv')

# Inspect dataframe
print("\nInspect the dataframe.\n")
print(df)
print(df.info())
print(df.describe())

# Drop missing values from the reviews.text column
df_cleaned = df.dropna(subset=['reviews.text'])

# Inspect the cleaned dataframe
print("\nInspect the cleaned dataframe.\n")
print(df_cleaned)
print(df_cleaned.info())
print(df_cleaned.describe())
print("\n1 value out of 34,660 has been removed.")

# Extract feature variable
reviews = df_cleaned['reviews.text']

# Inspect feature variable
print("\nInspect the feature variable.\n")
print(reviews)
print(reviews.info())
print(reviews.describe())


# 3. Create a function for sentiment analysis.

# Add pipe to enable sentiment score (polarity)
nlp.add_pipe('spacytextblob')

# For comparison I have made a few variations of the function as follows.
print("\nFour functions have been created:\n")
print("sentiment = a simple sentiment function")
print("sentiment_nopunc = the sentiment function with punctuation removed")
print("sentiment_nostop = the sentiment function with stop words removed")
print("sentiment_nopunc_nostop = the sentiment function with punctuation and stop words removed")

# Define functions:

# a) Sentiment function
def sentiment(review):
    # Use polarity to give a sentiment score of the input string
    polarity = nlp(review)._.blob.polarity
    # Round score to 2 decimal places
    return round(polarity,2)

# b) Sentiment function with punctuation removed
def sentiment_nopunc(review):
    # Create empty string
    review_stripped = ""
    # Loop over tokens in input string
    for token in nlp(review):
        # Exclude punction and stop words
        if not token.is_punct:
            # Concatenate all tokens not excluded
            review_stripped += " " + str(token)
    # Use polarity to give a sentiment score of the input string
    polarity = nlp(review_stripped)._.blob.polarity
    # Round score to 2 decimal places
    return round(polarity,2)

# c) Sentiment function with stop words removed
def sentiment_nostop(review):
    # Create empty string
    review_stripped = ""
    # Loop over tokens in input string
    for token in nlp(review):
        # Exclude punction and stop words
        if not token.is_stop:
            # Concatenate all tokens not excluded
            review_stripped += " " + str(token)
    # Use polarity to give a sentiment score of the input string
    polarity = nlp(review_stripped)._.blob.polarity
    # Round score to 2 decimal places
    return round(polarity,2)

# d) Sentiment function with punctuation and stop words removed
def sentiment_nopunc_nostop(review):
    # Create empty string
    review_stripped = ""
    # Loop over tokens in input string
    for token in nlp(review):
        # Exclude punction and stop words
        if not token.is_punct and not token.is_stop:
            # Concatenate all tokens not excluded
            review_stripped += " " + str(token)
    # Use polarity to give a sentiment score of the input string
    polarity = nlp(review_stripped)._.blob.polarity
    # Round score to 2 decimal places
    return round(polarity,2)


# 4. Test your model on sample product reviews.

print("\nTesting the output of each of the functions gives the following results:\n")
print("Example review 1:\n")
print(f"\"{reviews[0]}\"")
print(f"\nFunction name: sentiment. Sentiment score = {sentiment(reviews[0])}")
print(f"Function name: sentiment_nopunc. Sentiment score = {sentiment_nopunc(reviews[0])}")
print(f"Function name: sentiment_nostop. Sentiment score = {sentiment_nostop(reviews[0])}")
print(f"Function name: sentiment_nopunc_nostop. Sentiment score = {sentiment_nopunc_nostop(reviews[0])}")

print("\nExample review 2:\n")
print(f"\"{reviews[1]}\"")
print(f"\nFunction name: sentiment. Sentiment score = {sentiment(reviews[1])}")
print(f"Function name: sentiment_nopunc. Sentiment score = {sentiment_nopunc(reviews[1])}")
print(f"Function name: sentiment_nostop. Sentiment score = {sentiment_nostop(reviews[1])}")
print(f"Function name: sentiment_nopunc_nostop. Sentiment score = {sentiment_nopunc_nostop(reviews[1])}")

print("\nExample review 3:\n")
print(f"\"{reviews[2]}\"")
print(f"\nFunction name: sentiment. Sentiment score = {sentiment(reviews[2])}")
print(f"Function name: sentiment_nopunc. Sentiment score = {sentiment_nopunc(reviews[2])}")
print(f"Function name: sentiment_nostop. Sentiment score = {sentiment_nostop(reviews[2])}")
print(f"Function name: sentiment_nopunc_nostop. Sentiment score = {sentiment_nopunc_nostop(reviews[2])}")

print("Example review 4:\n")
print(f"\"{reviews[34657]}\"")
print(f"\nFunction name: sentiment. Sentiment score = {sentiment(reviews[34657])}")
print(f"Function name: sentiment_nopunc. Sentiment score = {sentiment_nopunc(reviews[34657])}")
print(f"Function name: sentiment_nostop. Sentiment score = {sentiment_nostop(reviews[34657])}")
print(f"Function name: sentiment_nopunc_nostop. Sentiment score = {sentiment_nopunc_nostop(reviews[34657])}")

print("\nExample review 5:\n")
print(f"\"{reviews[34658]}\"")
print(f"\nFunction name: sentiment. Sentiment score = {sentiment(reviews[34658])}")
print(f"Function name: sentiment_nopunc. Sentiment score = {sentiment_nopunc(reviews[34658])}")
print(f"Function name: sentiment_nostop. Sentiment score = {sentiment_nostop(reviews[34658])}")
print(f"Function name: sentiment_nopunc_nostop. Sentiment score = {sentiment_nopunc_nostop(reviews[34658])}")

print("\nExample review 6:\n")
print(f"\"{reviews[34659]}\"")
print(f"\nFunction name: sentiment. Sentiment score = {sentiment(reviews[34659])}")
print(f"Function name: sentiment_nopunc. Sentiment score = {sentiment_nopunc(reviews[34659])}")
print(f"Function name: sentiment_nostop. Sentiment score = {sentiment_nostop(reviews[34659])}")
print(f"Function name: sentiment_nopunc_nostop. Sentiment score = {sentiment_nopunc_nostop(reviews[34659])}")

# Analysis
print("\nAnalysing the 4 reviews sampled and the sentiment scores given by the 4 models, it can be seen that the models that strip punctuation appear to have no impact whatsoever on the outcome of the score and provide the exact same results whether punctuation is removed or not.")
print("\nAnalysing the impact of including or excluding stop words, however, shows that sometimes there is and sometimes there is not an impact on the score.")
print("\nReading the actual reviews themselves the simple model appears to perform better than the model without stop words but why is this?")
print("\nLets examine review 1 and review 5 which have the most differentiated scores.")

# To review the function with stop words removed, modify the function so that the stripped string is output
def sentiment_nostop_output(review):
    # Create empty string
    review_stripped = ""
    # Loop over tokens in input string
    for token in nlp(review):
        # Exclude punction and stop words
        if not token.is_stop:
            # Concatenate all tokens not excluded
            review_stripped += " " + str(token)
    return review_stripped

print(f"\nReview 1 states:\n\"{reviews[0]}\"")
print(f"\nWhereas when removing the stop words the stripped string becomes:\n\"{sentiment_nostop_output(reviews[0])}\"")
print("\nOverall the review appears to be fairly positive but when the stop words are removed the score is not positive and this seems to be because the stop words includes removing negation such as \"not\".")

print(f"\nReview 5 states:\n\"{reviews[34658]}\"")
print(f"\nWhereas when removing the stop words the stripped string becomes:\n\"{sentiment_nostop_output(reviews[34658])}\"")
print("\nOverall the review appears pretty negative so neither function performs too well but when removing stop words the performance becomes even worse (i.e. positive)! Again this appears to be because the stop words removes negation such as \"not\" which appears to completely change the sentiment of the review.\n")