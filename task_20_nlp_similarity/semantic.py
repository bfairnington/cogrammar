"""
Practical Task 1
Follow these steps:
● Create a file called semantic.py and run all the code extracts above.
● Write a note on what you noticed about the similarities between cat,
monkey and banana and think of an example of your own.
● Run the example file on with the simpler language model ‘en_core_web_sm’
and write a note on what you notice may be different from the model
'en_core_web_md'
"""

# Run all the code extracts from the file

# Import library
import spacy

# Define nlp
nlp = spacy.load("en_core_web_md")

# Compare similarity of "cat", "monkey", "banana"
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print()
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Working with vectors
tokens = nlp("cat apple monkey banana ")

for token1 in tokens:
    print()
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
sentence_to_compare = "Why is the cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

print()
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))


# Write a note on what you noticed about the similarities between cat, monkey and banana
print("\nCat and monkey have the closest similarity perhaps because they are both animals whereas the similarity with banana is much lower.")

# Create your own example
word4 = nlp("dog")
word5 = nlp("horse")
word6 = nlp("bone")

print()
print(word4, word5, word4.similarity(word5))
print(word5, word6, word6.similarity(word5))
print(word4, word6, word6.similarity(word4))

print("\nDog and horse have the closest similarity once agin perhaps because they are both animals whereas the similarity with bone is much lower.")


# Run the example file on with the simpler language model ‘en_core_web_sm’

# Define nlp
nlp2 = spacy.load("en_core_web_sm")

# Compare similarity of "cat", "monkey", "banana"
word7 = nlp2("cat")
word8 = nlp2("monkey")
word9 = nlp2("banana")

print()
print(word7.similarity(word8))
print(word9.similarity(word8))
print(word9.similarity(word7))

# Working with vectors
tokens2 = nlp2("cat apple monkey banana ")

for token1 in tokens2:
    print()
    for token2 in tokens2:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
sentence_to_compare2 = "Why is the cat on the car"

sentences2 = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
]

model_sentence2 = nlp2(sentence_to_compare2)

print()
for sentence2 in sentences2:
    similarity2 = nlp2(sentence2).similarity(model_sentence2)
    print(sentence2 + "-" + str(similarity2))

print("\nWhen rerunning the model using 'en_core_web_sm' an error message is given that:")
print("\nThe model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.")
print("\nThis appears to produce some results that do not make as much sense. For eample, now all three words (cat, monkey, bannana) have approximately the same similarity score with one another.")
print()


"""
Practical Task 2
Let us build a system that will tell you what to watch next based on the word
vector similarity of the description of movies.
● Read in the movies.txt file. Each separate line is a description of a different
movie.
● Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”
● The function should take in the description as a parameter and return the
title of the most similar movie.
"""

# Read in the movies.txt file. Each separate line is a description of a different movie

# Empty list of movies
movie_list = []

# Import file
file = open("movies.txt", "r")

# Read lines to list
for line in file:
    movie_list.append(line)


# Create a function to return which movies a user would watch next if they have watched Planet Hulk

# Planet Hulk description
planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Define function
def recommended_movie(movie_watched):
    # Empty list to hold scores
    score_list = []

    # Loop through list of movies
    for movie in movie_list:
        # Similarity score between each movie description and watched movie
        similarity_score = nlp(movie).similarity(nlp(movie_watched))
        # Append scores into list
        score_list.append(similarity_score)
        # Max score
        max_score = max(score_list)
        # Index of max score
        max_score_index = score_list.index(max_score)
    
    # Return the max similarity score and the movie with that score
    return movie_list[max_score_index][0:7]

print(f"\nAs you have watched Plant Hulk, you might also be interested in {recommended_movie(planet_hulk)}.\n")