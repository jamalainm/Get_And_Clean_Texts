import re
import os
import pickle
from unidecode import unidecode

# file = 'ciceronis_pro_roscio_comodeo.txt'
def remove_space_punct(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
#            text = re.sub("([LXIVCDM]+) ([\.,;:!?])", r'\1\2', text)
            text = re.sub(" ;", r';', text)
            full_name = in_directory + '/' + e
            hits.append(full_name)

            with open(f"{in_directory}/{e}", 'w', encoding="utf-8") as g:

                g.write(text)

def find_space_punct(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            if re.search(" ([\.,;:!?])", text):
                if not re.search("\. \. \.", text):
                    full_name = in_directory + '/' + e
                    hits.append(full_name)

    for hit in hits:
        print(hit)
    print(len(hits))

def find_numerals(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            if re.sub(r"M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?<=(I|V|X|C|D|M))", "", text):
                full_name = in_directory + '/' + e
                hits.append(full_name)

    for h in hits:
        print(h)

def remove_numeral_sections(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            text = re.sub(r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?<=(I|V|X|C|D|M))\.( )+", "", text)
            full_name = in_directory + '/' + e
            hits.append(full_name)

            with open(f"{'texts_without_section_numbers'}/{e}", 'a') as g:

                g.write(text)

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
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
#            elif bool(re.search(r'(??)', text)):
#                greek.append(fn)
# Need to move '|' to another search. It seems preoccupied with numbers
            elif bool(re.search(r'[????&?????=????????????????????????????????????????????jJ????????????????????????w??????????????????]', text)):
                greek.append(fn)

    for gk in greek:
        print(gk)

    print(f"Number of texts: {len(greek)}")

def report_bad_emdash(in_directory):
    entries = os.listdir(in_directory)

    hits = []
    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            if re.search(r"??", text):
                hits.append(e)

    print(len(hits))
    print(hits[-3:])

def remove_bad_emdash(in_directory,out_directory):
    entries = os.listdir(in_directory)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
#            text = re.sub(r"??", " ", text)
            if re.search(r"??", text):
                text = str(text)
    

            with open(f"{out_directory}/{e}", 'a') as g:

                g.write(text)


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

    Like parentheses, quotation marks need to be separated from the words
    they introduce. We also want them on the inside of closing punctuation
    like periods, semicolons, and commas

    Let's also look for the non-symmetrical quotation marks

    And sometimes we have two + in place of an em dash

    This mysterious character appears in some greek words: ??

    Looks like HS sometimes is followed by a tricky period.

    Also difficulty in recognizing / processing dates

    Some of the headers for Cicero's letters break into the middle
    of the text. E.g: EPP. AD ATTICVM XIV

    I think 'h.' followed by a numeral indicates the time

    At least on one occasion there is a footnote started in brackets with
    the Englihs word 'Footnote'

    This character is used in elision in Greek: ???

    We'll need to go through at least Apuleius' Apologia and maybe other
    texts where markup has split words apart by single spaces. Sometimes
    in just 1-2 letter chunks.

    Look for examples of 'cic' for the number 'M'

    Maybe look for 'h' following any consonant other than 't' or 'p'
    in order to spot uses of eta?
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

def remove_underscore(in_directory):
    entries = os.listdir(in_directory)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            text = re.sub(r"_", "", text)
    
            with open(f"{in_directory}/{e}", 'w', encoding="utf-8") as g:

                g.write(text)

def reverse_punct_quote(in_directory):
    entries = os.listdir(in_directory)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
#            text = re.sub(r"\.'", "'.", text)
#            text = re.sub(r'\."', '".', text)
#            text = re.sub(r"\?'", "'?", text)
#            text = re.sub(r'\?"', '"?', text)
#            text = re.sub(r",'", "',", text)
#            text = re.sub(r',"', '",', text)
#            text = re.sub(r";'", "';", text)
#            text = re.sub(r';"', '";', text)
#            text = re.sub(r"!'", "'!", text)
#            text = re.sub(r'!"', '"!', text)
            text = re.sub(r":'", "':", text)
            text = re.sub(r':"', '":', text)
    
            with open(f"{in_directory}/{e}", 'w', encoding="utf-8") as g:

                g.write(text)

def find_punct_numeral(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            if re.search("\d\.", text):
                hits.append(f)

    print(len(hits))
    print(hits[-3:])

def replace_punct_numeral(in_directory):
    entries = os.listdir(in_directory)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            text = re.sub("\d\.", "", text)

            with open(f"{in_directory}/{e}", 'w', encoding="utf-8") as g:

                g.write(text)

def replace_num_between_parens(in_directory):
    entries = os.listdir(in_directory)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            text = re.sub("(\((\d)+\))", "", text)

            with open(f"{in_directory}/{e}", 'w', encoding="utf-8") as g:

                g.write(text)

def find_num_between_parens(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            if re.search("(\((\d)+\))", text):
                full_name = in_directory + '/' + e
                hits.append(full_name)

    for h in hits:
        print(h)
    print(len(hits))
    
def find_punct_between(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
#            if re.search("(\w\(-)(\w)", text):
            if re.search("r[a-zA-Z]<[a-zA-Z]", text):
                full_name = in_directory + '/' + e
                hits.append(full_name)

    for h in hits:
        print(h)
    print(len(hits))
    

def replace_punct_between(in_directory):
    entries = os.listdir(in_directory)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            text = re.sub(r'(\w,)(\w)', r'\1 \2', text)

            with open(f"{in_directory}/{e}", 'w', encoding="utf-8") as g:

                g.write(text)

def find_period_quote(in_directory):
    entries = os.listdir(in_directory)

    hits = []

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            if re.search(r":'", text):
                hits.append(f)

    print(len(hits))
    print(hits[-3:])

def remove_newlines(in_directory,out_directory):
    entries = os.listdir(in_directory)

    for e in entries:

        with open(f"{in_directory}/{e}") as f:
            text = f.read()
            text = re.sub(r"\n+", " ", text)

            with open(f"{out_directory}/{e}", 'a', encoding='utf8') as g:

                g.write(text)


if __name__ == '__main__':
#    in_directory = "texts_without_section_numbers"
    out_directory = "texts_being_processed"
#    remove_underscore(out_directory)
#    find_period_quote(out_directory)
#    remove_newlines(in_directory,out_directory)
    find_space_punct(out_directory)
