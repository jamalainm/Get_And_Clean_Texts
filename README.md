# Get_And_Clean_Texts
We'll be scraping The Latin Library, breaking texts up into paragraphs, standardizing some spelling, removing certain characters, etc.

# Observations and things to do:
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

Look for examples of 'cic' for the number 'M'

Maybe look for 'h' following any consonant other than 't' or 'p'
in order to spot uses of eta?

