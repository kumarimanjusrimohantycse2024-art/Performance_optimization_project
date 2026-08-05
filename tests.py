from collections import Counter


def normalize_word(word):
    import string
    return word.strip(string.punctuation).lower()


def original_count_words(text):
    words = text.split()
    cleaned_words = []
    for word in words:
        cleaned = normalize_word(word)
        if cleaned:
            cleaned_words.append(cleaned)

    frequency = {}
    unique_words = []
    for word in cleaned_words:
        if word not in unique_words:
            unique_words.append(word)

    for item in unique_words:
        count = 0
        for word in cleaned_words:
            if word == item:
                count += 1
        frequency[item] = count
    return frequency


def optimized_count_words(text):
    words = [normalize_word(word) for word in text.split()]
    words = [word for word in words if word]
    return Counter(words)


def run_tests():
    sample_text = "Python python code! Code? code. performance PERFORMANCE performance"
    original_result = original_count_words(sample_text)
    optimized_result = optimized_count_words(sample_text)

    assert original_result == dict(optimized_result), "Word counts do not match"
    assert original_result["python"] == 2, "Python count failed"
    assert original_result["code"] == 3, "Code count failed"
    assert original_result["performance"] == 3, "Performance count failed"

    print("All tests passed successfully.")


if __name__ == "__main__":
    run_tests()