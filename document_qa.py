
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCUMENT = Path("sample_document.txt")
THRESHOLD = 0.10


def load_document():
    if not DOCUMENT.exists():
        raise FileNotFoundError("sample_document.txt was not found.")
    return DOCUMENT.read_text(encoding="utf-8")


def split_into_passages(text):
    return [
        p.strip()
        for p in text.split("\n\n")
        if p.strip()
    ]


def build_retriever(passages):
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(passages)
    return vectorizer, matrix


def answer_question(question, passages, vectorizer, matrix):
    query_vector = vectorizer.transform([question])
    scores = cosine_similarity(query_vector, matrix).flatten()

    best_index = scores.argmax()
    best_score = scores[best_index]

    if best_score == 0 or best_score < THRESHOLD:
        print("\nAnswer: Information not found in provided document.")
        return

    print("\nAnswer:")
    print(passages[best_index])

    print("\nSupporting source passage:")
    print(f"Document: {DOCUMENT.name}")
    print(f"Passage number: {best_index + 1}")
    print(passages[best_index])

    print(f"\nRelevance score: {best_score:.3f}")


def main():
    text = load_document()
    passages = split_into_passages(text)

    if not passages:
        print("The document contains no readable passages.")
        return

    vectorizer, matrix = build_retriever(passages)

    print("DOCUMENT QUESTION-ANSWERING ASSISTANT")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nAsk a question: ").strip()

        if question.lower() == "exit":
            print("Assistant stopped.")
            break

        if not question:
            print("Please enter a question.")
            continue

        answer_question(question, passages, vectorizer, matrix)


if __name__ == "__main__":
    main()
