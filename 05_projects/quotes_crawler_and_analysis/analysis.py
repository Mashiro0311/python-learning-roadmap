import pandas as pd
import matplotlib.pyplot as plt


def analysis(filename):
    df = pd.read_csv(filename)
    author_count = df['author'].value_counts().head(10)

    top_author = author_count.idxmax()
    top_count = author_count.max()

    print(f"名言最多的作者是：{top_author}（{top_count} 条）")
    author_count.plot(kind='bar')
    plt.title("Top 10 Authors by Number of Quotes")
    plt.xlabel("Author")
    plt.ylabel("Number of Quotes")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    analysis('quotes_crawl.csv')
