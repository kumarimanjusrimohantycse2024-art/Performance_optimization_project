import random
import string
import time
import cProfile
import pstats
from io import StringIO
from collections import Counter


def generate_text(num_sentences=5000):
    words = [
        "python", "code", "optimize", "speed", "performance", "project",
        "student", "data", "analysis", "profile", "function", "loop",
        "list", "set", "counter", "text", "word", "result", "system", "task"
    ]
    sentences = []
    for _ in range(num_sentences):
        sentence_words = []
        for _ in range(12):
            word = random.choice(words)
            if random.randint(0, 10) > 7:
                word = word.upper()
            sentence_words.append(word)
        sentences.append(" ".join(sentence_words))
    return ". ".join(sentences)


def normalize_word(word):
    return word.strip(string.punctuation).lower()


def count_words_fast(text):
    words = [normalize_word(word) for word in text.split()]
    words = [word for word in words if word]
    return Counter(words)


def get_top_words_fast(frequency, top_n=10):
    return frequency.most_common(top_n)


def analyze_text_fast(text):
    start = time.perf_counter()
    frequency = count_words_fast(text)
    top_words = get_top_words_fast(frequency)
    total_words = sum(frequency.values())
    unique_words = len(frequency)
    elapsed = time.perf_counter() - start
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "top_words": top_words,
        "elapsed": elapsed,
    }


def main():
    text = generate_text()
    result = analyze_text_fast(text)
    print("Total words:", result["total_words"])
    print("Unique words:", result["unique_words"])
    print("Top words:", result["top_words"])
    print("Elapsed time:", round(result["elapsed"], 6), "seconds")


def profile_run():
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    s = StringIO()
    stats = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
    stats.print_stats(15)
    output = s.getvalue()
    print("\n--- PROFILE OUTPUT ---\n")
    print(output)
    with open("profile_optimized.txt", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    profile_run()