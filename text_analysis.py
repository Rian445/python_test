sentence = input("Enter a sentence: ")

cleaned = sentence.strip()
length = len(cleaned)
words = cleaned.split()

first_char = cleaned[0] if length > 0 else ""
last_char = cleaned[-1] if length > 0 else ""

if length == 0:
    middle = ""
elif length % 2 == 0:
    middle = cleaned[length//2 - 1: length//2 + 1]
else:
    middle = cleaned[length//2]

print("\n--- Text Analysis ---")
print("Cleaned Sentence:", cleaned)
print("First character:", first_char)
print("Last character:", last_char)
print("Middle character(s):", middle)
print("Word count:", len(words))
print("Reversed sentence:", cleaned[::-1])
print("Capitalized:", cleaned.capitalize())

if cleaned.endswith(('.', '!', '?')):
    print("Ends with punctuation ")
else:
    print("Does NOT end with punctuation ")
