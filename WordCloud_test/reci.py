from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

def generate_wordcloud(sentence):
    # Split the sentence and calculate word frequencies
    words = sentence.split()
    word_freq = Counter(words)

    # Generate word cloud based on word frequencies
    wordcloud = WordCloud(width=800, height=400, background_color='white', prefer_horizontal=0.5).generate_from_frequencies(word_freq)

    # Assign random colors to each word
    wordcloud.recolor(color_func=random_color_func)

    # Display the word cloud image
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Assign a random color to each word
def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

# Example sentence
sentence = "This is an example sentence where some words will be repeated. The example sentence is shuffled, and the most frequently repeated words will appear larger in the word cloud. shabi shabi shabi shabi shabi shabi shabi shabi"

generate_wordcloud(sentence)