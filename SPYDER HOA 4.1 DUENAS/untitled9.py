def filter(sentence, curse_words):
    words = sentence.split()
    filtered = ""

    for word in words:
        if word in curse_words:
            filtered += "#" * len(word) + " "
        else:
            filtered += word + " "

    return filtered.strip()

sentence = input("Enter a sentence: ")
curse_words_input = input("Enter bad words separated by commas: ")

curse_words = curse_words_input.split(",")

filtered = filter(sentence, curse_words)
print("Filtered sentence:", filtered)