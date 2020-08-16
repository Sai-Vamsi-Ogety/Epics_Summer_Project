# from spacy.lang.en import English

# nlp = English()
# doc = nlp(
# "In 1990, more than 60% of people in East Asia were in extreme poverty."
# "Now less than 4% are.")
# # Tokens

# for token in doc:
    
#     if token.like_num:


# import spacy

# nlp = spacy.load("en_core_web_sm")

# text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"


# doc = nlp(text)


# for token in doc:

#     token_txt = token.text 
#     token_pos = token.pos_
#     token_dep = token.dep_

#     print(f"{token_txt : <12}{token_pos: <10}{token_dep :<10}")

# import spacy

# nlp = spacy.load("en_core_web_sm")

# text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# # Process the text
# doc = nlp(text)

# # Iterate over the predicted entities
# for ent in doc.ents:
#     # Print the entity text and its label
#     print(ent.text, ent.label_)



# import spacy

# # Import the Matcher
# from spacy.matcher import Matcher

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# # Initialize the Matcher with the shared vocabulary
# matcher = Matcher(nlp.vocab)

# # Create a pattern matching two tokens: "iPhone" and "X"
# pattern = [{"TEXT":"iPhone"},{"TEXT":"X"}]

# # Add the pattern to the matcher
# matcher.add("IPHONE_X_PATTERN", None, pattern)

# # Use the matcher on the doc
# matches = matcher(doc)
# print("Matches:", [doc[start:end].text for match_id, start, end in matches])

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp(
    "Twitch Prime, the perks program for Amazon Prime members offering free "
    "loot, games and other benefits, is ditching one of its best features: "
    "ad-free viewing. According to an email sent out to Amazon Prime members "
    "today, ad-free viewing will no longer be included as a part of Twitch "
    "Prime for new members, beginning on September 14. However, members with "
    "existing annual subscriptions will be able to continue to enjoy ad-free "
    "viewing until their subscription comes up for renewal. Those with "
    "monthly subscriptions will have access to ad-free viewing until October 15."
)

# Create the match patterns
pattern1 = [{"LOWER": "Amazon"}, {"IS_TITLE": True, "POS": "PROPN"}]
pattern2 = [{"LOWER": "ad"},{"LOWER": "-"},{"LOWER": "free"},{"POS": "NOUN"}]

# Initialize the Matcher and add the patterns
matcher = Matcher(nlp.vocab)
matcher.add("PATTERN1", None, pattern1)
matcher.add("PATTERN2", None, pattern2)

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Print pattern string name and text of matched span
    print(doc.vocab.strings[match_id], doc[start:end].text)
print("END")