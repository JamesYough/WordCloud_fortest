from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

def generate_wordcloud_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    generate_wordcloud(text)

# Example usage
file_path = 'path/to/your/file.txt'
generate_wordcloud_from_file(file_path)