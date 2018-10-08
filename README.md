## Using Levenshtein Distance to evaluate the likeliness of English-German word pairs being cognates. 

### Modifications

1. Alphabets
Added 4 special German alphabets - ä, ö, ü and ß in addition to the 26 alphabets of English.

2. Case-insensitive
converted all strings to lower case so that the capital letter in German nouns will not add to the edit cost.

3. Edit cost
3.1 Initial Consonants - Grimm's law
According to Grimm's law, some initial consonants that are distinct in English and German have the same origin. This script targets two pairs of them: English "t" (as in "ten") vs. German "ts" (as in "zwei") and English "th" (as in English "the") vs. German "d" (as in "drei"). English-German word pairs that contains the corresponding initial consonants would have 1 minus from their original edit cost (i.e. treating English "t-" as completely the same as German "z-", English "th-" as completely the same as German "d-" at word starting position). 
3.2 Day and Tag 
Based on the data given, it is obvious to see that "tag" in German means "day" in English, which is also verified with a dictionary look-up. Grimm's law also suggests that English "d" and German "t" as initial consonants have the same origin. English-German word pairs that contains the corresponding initial consonants would have 2 minus from their original edit cost (i.e. treating English "day" as completely the same as German "tag".)

4. Determination of Cognates
Likeliness of cognates is determined based on the ratio of edit cost (C) to average word length (AVG) of word pairs:
i. UNLIKELY - if C (after adjustment, if any) is larger than or equal to 90% of AVG.
ii. SOMEWHAT UNLIKELY - C is between 75% to 89% of AVG
iii. SOMEWHAT LIKELY - C is between 50% to 74% of AVG
iv. LIKELY - C is between 0 to 49% of AVG

## Limitations and Potential Improvement
1. The adjustment of edit cost are limited and apply only to word-beginning or word-final positions. 
2. More equivalent word pairs other than "day" and "tag" can also be added to enhance performance. 
3. The ratio used to evaluate likeness of cognate pairs is not based on empirical evidence on comparison between the English and German language.  