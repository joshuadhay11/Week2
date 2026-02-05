'''
NLTK Practice - Week 2
'''

'''
---------------------------------------------------
Purpose:

To become proficient in using:
  - Python
  - Natural Language Toolkit (NLTK)
  - Matplot Library 
  
To prepare for the Week 2-4 quiz and assignment.

---------------------------------------------------

 - I have provided two books are provided in the '/texts' folder.
 - One by Jules Vern and One by Sir Arthur Conan Doyle
 
You are to develop a script in Python that uses the Natural Language Toolkit (NLTK)
to extract key features from each book.


The features to be extracted include (for each book separately) the number of occurrences of:
    o Nouns (all types)
    o Verbs (all types)
    o Adjectives (all types)
    o Other Types

Then using the matplotlib you will plot the percentage of:

    - nouns
    - verbs
    - adjectives
    - other parts of speech
 as they are used by each author in reference to the entirety of their respective texts.

These percentages will be plotted on the same plot.
   
---------------------------------------------------

Please review the attached examples in the /examples/ folder to help you get started.

---------------------------------------------------

To Submit:
    - Commit and Push your final script to GitHub. (this file edited)
    (This should be done before posting in the discussion in D2L)
    
    - Commit a legible screenshot of your results to the /docs/ folder.
       - Make sure all results and labels are correct and visible
       
    - Then post your screenshot to the appropriate D2L Discussion Board.
    - Explain any challenges you might have had. 
    - Explain how your results are relevant to Cyber Deception Detection.

'''

# Start your script here:

from pathlib import Path
from typing import Dict, Tuple

import nltk
import matplotlib.pyplot as plt

def bucket_tag(tag: str) -> str:
    if tag.startswith("NN"):
        return "nouns"
    if tag.startswith("VB"):
        return "verbs"
    if tag.startswith("JJ"):
        return "adjectives"
    return "other"


def analyze_text(text: str) -> Tuple[Dict[str, int], Dict[str, float], int]:
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(s) for s in sentences]
    tagged_sentences = nltk.pos_tag_sents(tokenized_sentences)

    counts = {"nouns": 0, "verbs": 0, "adjectives": 0, "other": 0}
    total = 0

    for sent in tagged_sentences:
        for word, tag in sent:
            if all(not ch.isalnum() for ch in word):
                continue
            counts[bucket_tag(tag)] += 1
            total += 1

    if total == 0:
        raise ValueError("No tokens were counted.")

    percentages = {k: (v / total) * 100.0 for k, v in counts.items()}
    return counts, percentages, total


def plot_percentages(results, out_path: Path):
    categories = ["nouns", "verbs", "adjectives", "other"]
    labels = list(results.keys())

    x = list(range(len(categories)))
    bar_width = 0.35

    plt.figure()
    for i, label in enumerate(labels):
        offsets = [xi + (i - 0.5) * bar_width for xi in x]
        values = [results[label][c] for c in categories]
        plt.bar(offsets, values, width=bar_width, label=label)

    plt.xticks(x, ["Nouns", "Verbs", "Adjectives", "Other"])
    plt.ylabel("Percentage (%)")
    plt.title("Parts of Speech Comparison")
    plt.legend()
    plt.tight_layout()

    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=200)
    plt.show()


def main():

    # ---- BOOK PATHS ----
    doyle_path = "C:/Users/hayjo/PycharmProjects/Week2/texts/doyle.txt"
    jules_path = "C:/Users/hayjo/PycharmProjects/Week2/texts/jules.txt"
    # -----------------------------

    docs_dir = Path("docs")
    out_img = docs_dir / "pos_percentages.png"

    results = {}

    # Doyle
    doyle_text = Path(doyle_path).read_text(encoding="utf-8", errors="ignore")
    counts, percentages, total = analyze_text(doyle_text)
    print("\n=== Doyle ===")
    print("Counts:", counts)
    print("Percentages:", {k: round(v, 2) for k, v in percentages.items()})
    results["Doyle"] = percentages

    # Jules
    jules_text = Path(jules_path).read_text(encoding="utf-8", errors="ignore")
    counts, percentages, total = analyze_text(jules_text)
    print("\n=== Jules Verne ===")
    print("Counts:", counts)
    print("Percentages:", {k: round(v, 2) for k, v in percentages.items()})
    results["Jules Verne"] = percentages

    plot_percentages(results, out_img)
    print(f"\nSaved plot to: {out_img.resolve()}")


if __name__ == "__main__":
    main()
