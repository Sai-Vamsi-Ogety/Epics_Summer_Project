import spacy

nlp = spacy.load("en_core_web_md")




def entities(text):

    """
    This function takes input as text and output is a list of entities for every token in the text
    """
    ent_list = []
    doc = nlp(text)

    for ent in doc.ents:

        ent_list.append((ent.text, ent.label_))

    return ent_list


if __name__ == "__main__":

        entities()


