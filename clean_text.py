import re
import os
import pickle
from unidecode import unidecode

# file = 'ciceronis_pro_roscio_comodeo.txt'
def unidecode_text():
    f = open('unprocessed_texts/ciceronis_de_finibus_5-92.txt')
    data = f.read()
    new_data = unidecode(data)
    print(new_data)

def clean_plinius():
    """
    Remove paragraphs from Pliny that are just headers for different letters
    """
    source_dir = 'unprocessed_texts/'
    filenames = [source_dir + f for f in os.listdir(source_dir)]

    pliny_salutations = []

    for fn in filenames:
        with open(fn, 'r') as f:
            text = f.read()

            if 'C. PLINIUS' in text:
                pliny_salutations.append(fn)

    for ps in pliny_salutations:
        os.remove(ps)

def clean_emph_by_space():
    """
    Locate texts that have emphasized words by inserting spaces between the
    letters.
    """
    source_dir = 'unprocessed_texts/'
    filenames = [source_dir + f for f in os.listdir(source_dir)]

    emphasized = []

    for fn in filenames:
        with open(fn, 'r') as f:
            text = f.read()

            if bool(re.search(r'([a-zA-Z] ){3,}', text)):
                emphasized.append(fn)

    for emph in emphasized:
        print(emph)

#    ([a-zA-z]{1} {1}){2, }

def find_greek_words():
    """
    Using slashes and maybe the tilda (accent marks) with alphabetic characters
    on both sides, identify texts with Greek in them.

    Some texts also use _____ to indicate Greek words. I guess I'll need to
    search for any occurrance of two underscores next to each other as well
    """
    source_dir = 'unprocessed_texts/'
    filenames = [source_dir + f for f in os.listdir(source_dir)]

    greek = []

    for fn in filenames:
        with open(fn, 'r') as f:
            text = f.read()

            if bool(re.search(r'([a-zA-Z]/[a-zA-Z])', text)):
                greek.append(fn)
            elif bool(re.search(r'([a-zA-Z]\\[a-zA-Z])', text)):
                greek.append(fn)
            elif bool(re.search(r'([a-zA-Z]=[a-zA-Z])', text)):
                greek.append(fn)
            elif bool(re.search(r'([a-zA-Z]/)', text)):
                greek.append(fn)
            elif bool(re.search(r'([a-zA-Z]\\)', text)):
                greek.append(fn)
            elif bool(re.search(r'([a-zA-Z]=)', text)):
                greek.append(fn)
            elif bool(re.search(r'(__)', text)):
                greek.append(fn)
#            elif bool(re.search(r'(w)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(¤)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(Ë)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(ž)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(Æ)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(Ò)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(Ü)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(ç)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(ê)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(È)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(Ÿ)', text)):
#                greek.append(fn)
# Need to move '|' to another search. It seems preoccupied with numbers
            elif bool(re.search(r'[¶&‰¾=«»±§Ø°¤Æãåç¢ÐéêëËÈÊÍÎjJþÞóòðÒÜÙÚŲwýŸž]', text)):
                greek.append(fn)

    for gk in greek:
        print(gk)

    print(f"Number of texts: {len(greek)}")

def clean_and_process_texts():
    """
    We should look for instances of punctuation surrounded by alphabetic
    characters without spaces. Similarly, brackets and parentheses

    We should also look for punctuation that has a space on the left between
    it and an alphabetic character or quotation mark

    what about enclitic -ne and enclitic -ve?

    It looks like there are also underscores between Roman numerals that will
    need to be dealt with

    If there's an em dash it is intepreted as a CCONJ; we'll want to replace
    all of them with sinle hyphens, I think; or maybe we get rid of all
    hyphens? Maybe we should see how common they are.

    Similarly, I think we'll want to insert spaces between parentheses and the
    characters they demarcate

    There's also the mysterious character (em dash?) embedded in this word
    that has be turned into something else: roquo

    Should I search for 'j' just in case it's for Greek characters before
    doing a replace?

    Like parentheses, quotation marks need to be separated from the words
    they introduce. We also want them on the inside of closing punctuation
    like periods, semicolons, and commas

    Let's also look for the non-symmetrical quotation marks

    And sometimes we have two + in place of an em dash

    This mysterious character appears in some greek words: 

    Looks like HS sometimes is followed by a tricky period.

    Also difficulty in recognizing / processing dates

    Some of the headers for Cicero's letters break into the middle
    of the text. E.g: EPP. AD ATTICVM XIV

    I think 'h.' followed by a numeral indicates the time

    At least on one occasion there is a footnote started in brackets with
    the Englihs word 'Footnote'

    This character is used in elision in Greek: ’

    We'll need to go through at least Apuleius' Apologia and maybe other
    texts where markup has split words apart by single spaces. Sometimes
    in just 1-2 letter chunks.
    """
    entries = os.listdir(in_directory)

    que_words = []

    with open('que_words.json','rb') as fp:
        que_words = pickle.load(fp)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()

            text = re.sub(r"M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?<=(I|V|X|C|D|M))\.", "", text)
            text = re.sub(r"M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?<=(I|V|X|C|D|M))\n", "", text)
            text = re.sub(r"M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?<=(I|V|X|C|D|M)) \d", "", text)
            text = re.sub(r"\[M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?<=(I|V|X|C|D|M))\]", "", text)
            text = re.sub(r"\.{3}", "... ", text)
            text = re.sub(r"\(\d+\)", "", text)
            text = re.sub(r"\[\d+\]", "", text)
            text = re.sub(r"\d", "", text)
            text = re.sub(r"<|>", "", text)
            """ This should really just put a space between the word and the
            Parenthesis """
#            text = re.sub(r"\(|\)", "", text)
            text = re.sub(r"\[|\]", "", text)
            text = re.sub(r"\n+", " ", text)
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"\*", " ", text)
            text = re.sub(r"\+", " ", text)
            text = re.sub(r"j", "i", text)
            text = re.sub(r"J", "I", text)
            text = re.sub(r"V", "U", text)
            text = re.sub(r"v", "u", text)
            text = re.sub(r"_", "", text)

            enclitic_que = re.findall(r'\w+que\b', text)
            for eq in enclitic_que:
                if eq not in que_words:
                    separated_enclitic = f'{eq[:-3]} que'
                    text = re.sub(eq, separated_enclitic, text)
        


            with open(f"{out_directory}/{e}", 'a') as g:

                g.write(text)

if __name__ == '__main__':
    in_directory = "Experimental_Unprocessed_Texts"
    out_directory = "To_Be_Converted"
    find_greek_words()
