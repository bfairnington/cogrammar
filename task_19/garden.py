"""
Practical Task 1

Follow these steps:

● Read the introduction about garden path sentences and study a few of
the examples provided on Wikipedia.

● Create a new Python file called garden.py and save it to your Dropbox
folder for this task.

● Find at least 2 garden path sentences from the web, or think up your own.

● Store the sentences you have identified or created in a list called gardenpathSentences.

● Add the following sentences to your list:

○ Mary gave the child a Band-Aid.

○ That Jill is never here hurts.

○ The cotton clothing is made of grows in Mississippi.

● Tokenize each sentence in the list, and perform named entity recognition.

● Examine how spaCy has categorised each sentence. Then, use
spacy.explain to look up and print the meaning of entities that you don’t
understand. For example: print(spacy.explain("FAC"))

● At the bottom of your file, write a comment about two entities that you
looked up. For each entity answer the following questions:

○ What was the entity and its explanation that you looked up?

○ Did the entity make sense in terms of the word associated with it?

"""

# Create garden path sentence list
gardenpathSentences = ["When Fred eats food gets thrown.", "We painted the wall with cracks."]

# Append additional garden path sentences
gardenpathSentences.append("Mary gave the child a Band-Aid.")
gardenpathSentences.append("That Jill is never here hurts.")                           
gardenpathSentences.append("The cotton clothing is made of grows in Mississippi.")

# Import library
import spacy

# Define nlp function
nlp = spacy.load('en_core_web_sm')


# Inspect words identified as tokens in each sentence in the list

# Loop through all sentences
for i in range(len(gardenpathSentences)):
    # Print sentence number
    print(f"\nSentence {i+1})")

    # Loop through each word in each sentence
    for token in nlp(gardenpathSentences[i]):

        # Exclude punction and stop words
        if not token.is_punct and not token.is_stop:
            # Print token, orth_ and orth
            print(token, token.orth_, token.orth)


# Perform named entity recognition 

# Loop through all sentences
for i in range(len(gardenpathSentences)):
    # Print sentence number
    print(f"\nSentence {i+1})")

    # Loop through each word in each sentence
    for token in nlp(gardenpathSentences[i-1]).ents:
        # Print token, label_ and label
        print(token, token.label_, token.label)

print(f"\nAs can be seen the .ents .label_ method is only able to categorise proper nouns (names) in the list of garden path sentences.")


# Use spacy to explain the categorisations applied

# Create empty list
label_list = [] 

# Loop through all sentences
for i in range(len(gardenpathSentences)):

    # Loop through each word in each sentence
    for token in nlp(gardenpathSentences[i-1]).ents:

        # Create list of all labels identified
        label_list.append(token.label_)

# For each label print the spacy label_ and its spacy explanation
for label in range(len(label_list)):
    print()
    print(label_list[label] + " = " + spacy.explain(label_list[label]))

# Answer the final two questions
print("\nWhat was the entity and its explanation that you looked up?")
print(label_list[0] + " & " + label_list[1])
print()
print("Did the entity make sense in terms of the word associated with it?")
print('The entities make sense but it is a shame that these were the only entities identified.')
print()