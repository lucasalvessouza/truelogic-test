## Truelogic assessment 

The problem:
You have a bowl of letters (Alphabet soup).
Please write a method that outputs how many times you would be able to spell PENNYMAC from the letters in the bowl.
If you are unable to spell it, please return 0

## Solution
Using Counter method to give me the count of each letter, I'll check for each letter, how many times it will be found on the "bowl of letters".
The maximum that this word will be repeated in the text is the minimum of the letter that is repeated least within its condition (a letter can be repeated more times depending on the word).

## Test
You can run ```pytest test.py``` to run the cases. 