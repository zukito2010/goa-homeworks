def filter_bad_words(sentence, bad_words):
    words = sentence.split()
    filtered_words = [word for word in words if word not in bad_words]
    return ' '.join(filtered_words)

sentence = "Today I feel lazy and I don't want to do anything"
bad_words = ["lazy", "don't"]
filtered_sentence = filter_bad_words(sentence, bad_words)

print(filtered_sentence)