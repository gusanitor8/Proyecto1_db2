import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from typing import List, Dict
from io import BytesIO


def plot_top_authors(data: List[Dict]) -> BytesIO:
    author_names = [result["author_name"] for result in data]
    book_counts = [result["books"] for result in data]

    buffer = BytesIO()

    plt.figure(figsize=(8, 6))  # Adjust figure size as needed
    plt.bar(author_names, book_counts, color='skyblue')
    plt.xlabel("Author Name")
    plt.ylabel("Book Count")
    plt.title("Top 5 Authors with Most Books")
    plt.xticks(rotation=15, ha="right")  # Rotate x-axis labels for better readability
    plt.tight_layout()

    plt.savefig(buffer, format="png")

    plt.close()
    buffer.seek(0)
    return buffer
