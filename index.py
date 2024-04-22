from collections import Counter

def count_spellings(bowl_letters, target_word):
  word_counts = Counter(target_word.upper())
  letter_counts = Counter(bowl_letters.upper())
  result = {}

  for letter in target_word.upper():
      if letter not in letter_counts:
          return 0
      result[letter] = letter_counts[letter] // word_counts[letter]
  return min(result.values())

