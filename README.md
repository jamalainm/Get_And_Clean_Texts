# Get_And_Clean_Texts
We'll be scraping The Latin Library, breaking texts up into paragraphs, standardizing some spelling, removing certain characters, etc.

## Observations and things to do:
1. We should look for instances of punctuation surrounded by alphabetic characters without spaces. Similarly, brackets and parentheses. We'll also need to find brackets at the beginning or ends of words.

1. We should also look for punctuation that has a space on the left between it and an alphabetic character or quotation mark

1. Don't forget punctuation that has a character on the right hand side.

1. We might want to take a look at hyphens. There's a lot of variation in their use

1. what about enclitic -ne and enclitic -ve?

1. Similarly, I think we'll want to insert spaces between parentheses and the characters they demarcate

1. There's also the mysterious character (em dash?) embedded in this word that has be turned into something else: roquo

1. Like parentheses, quotation marks need to be separated from the words they introduce. We also want them on the inside of closing punctuation like periods, semicolons, and commas

1. Let's also look for the non-symmetrical quotation marks

1. And sometimes we have two + in place of an em dash

1. This mysterious character appears in some greek words: 

1. Looks like HS sometimes is followed by a tricky period.

1. Also difficulty in recognizing / processing dates

1. Some of the headers for Cicero's letters break into the middle of the text. E.g: EPP. AD ATTICVM XIV

1. I think 'h.' followed by a numeral indicates the time

1. At least on one occasion there is a footnote started in brackets with the Englihs word 'Footnote'

1. This character is used in elision in Greek: ’

1. We'll need to go through at least Apuleius' Apologia and maybe other texts where markup has split words apart by single spaces. Sometimes in just 1-2 letter chunks.

1. Look for examples of 'cic' for the number 'M'

1. Maybe look for 'h' following any consonant other than 't' or 'p' in order to spot uses of eta?

1. Make sure that colons are left adjacent to characters without spaces.

1. At least judging from one passage of Apuleius' De Mundo (13); there is A LOT of Greek that is not distinguished from the surrounding Latin at all.

1. Valerius Maximus has a strange organizational principal whereby some sections have an 'ext.' in them. Will need to remove.

1. It looks like sometimes spaces signify lost html tags, so that two spaces in a row could signify Greek words

1. Will need to look at plus signs, which regularly indicate corrupted texts

1. Sometimes numerals have commas betweene them, eg: 5, 2

1. Some Greek is written without accents but with parentheses for breathing marks. Should search for '(' and ')' between alphabetic characters
