from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class FaqAgent:
    def __init__(self, questions:list [str], answers:list [str]):
        self.questions = questions
        self.answers = answers
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1,2)
        )
        self.doc_vectors = self.vectorizer.fit_transform(questions)

    def answer(self, query:str):
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.doc_vectors)[0]
        best_idx = np.argmax(similarities)

        if similarities[best_idx] < 0.08:
            return None
        return self.answers[best_idx]
