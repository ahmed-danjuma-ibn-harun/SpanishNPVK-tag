####
# Spanish text tagging module
# install the spanish model wheel, by running this line below in your prompt or command line
#  !pip install https://huggingface.co/Ahmed-ibn-Harun/es_pipeline/resolve/main/es_pipeline-any-py3-none-any.whl

# Using spacy.load().



# Using spacy.load().
import spacy
import pandas as pd
from collections import Counter
nlp = spacy.load('es_pipeline')



class SpanishNPVK:
    
    """Class for extracting Nouns, Proper Nouns, Verbs, and Keywords in Spanish.

    Atttributes
    -----------
    text : str
        the input text which Nouns, Proper Nouns, Verbs, and Keywords will be predicted.
    
    Methods
    -------
    extract_keywords
        extracts the nouns, propn, verbs, keywords from the input text
.
    tag_text
        returns a dictionary format of the tagged text with keys: "TEXT", "NOUNS", "PROPN", "VERBS" "KEYW"
    display_tags
        returns a spacy.displacy.render for the tags
   
    """
    
        
    def extract_keywords(text):
        
        # Load Spanish model
        doc = nlp(text)
       
        #Extract Nouns
        nouns = [token.text for token in doc if token.ent_type_ == "NOUN"]
    
        #Extract Proper Nouns
        propn = [token.text for token in doc if token.ent_type_ == "PNOUN"]

        #Extract Verbs
        verbs = [token.text for token in doc if token.ent_type_ == "VERB"]

        #Extract keywords
        words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
        freq_words = Counter(words)
        keywords = [word for word, freq in freq_words.most_common(10)]
    
        return nouns, propn, verbs, keywords

    def tag_text(text):
        noun = []
        prop = []
        verb = []
        keyw = []
        nouns, propn, verbs, keywords = SpanishNPVK.extract_keywords(text)
        noun.append(nouns)
        prop.append(propn)
        verb.append(verbs)
        keyw.append(keywords)
        df = pd.DataFrame({"TEXT": text, "NOUNS": noun, "PROPN": prop, "VERBS": verb, "KEYW": keyw})
        
        return df.to_dict(orient= "records")

    def display_tags(text,jupyter=False):
        # Input:
        # text : str
        # jupyter : Boolean: set to true wen using jupyter notebook
        # Load Spanish model
        doc = nlp(text)
        img = spacy.displacy.render(doc, style = "ent", jupyter = jupyter, options = {'distance': 120})
        return img