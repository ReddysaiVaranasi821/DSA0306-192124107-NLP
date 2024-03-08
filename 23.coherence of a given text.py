import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def calculate_similarity_matrix(sentences):
    vectorizer = CountVectorizer().fit_transform(sentences)
    similarity_matrix = cosine_similarity(vectorizer)
    return similarity_matrix

def evaluate_coherence(text):
    sentences = nltk.sent_tokenize(text)

    similarity_matrix = calculate_similarity_matrix(sentences)
    average_similarity = np.triu(similarity_matrix, k=1).sum() / np.count_nonzero(np.triu(similarity_matrix, k=1))

    return average_similarity

if __name__ == "__main__":
    input_text = """
    Natural language processing (NLP) is a subfield of artificial intelligence that deals with the interaction between computers and humans using natural language. NLP techniques are used in various applications, including language translation, sentiment analysis, and chatbot development. Machine learning and deep learning play crucial roles in advancing NLP capabilities. However, coherence in text remains a challenging aspect to measure.

    Coherence refers to the logical flow and connectivity of ideas within a text. A coherent text is one where sentences and ideas are well-connected, making it easy for readers to follow. Various factors contribute to coherence, such as proper use of transition words, consistent terminology, and a clear structure.

    Evaluating coherence is essential for assessing the quality of written content. In this program, we use a basic approach that calculates the average pairwise similarity between sentences. While this approach is simplistic, it provides a starting point for coherence evaluation.

    As NLP research progresses, more advanced techniques may emerge for evaluating coherence in text. Researchers continue to explore innovative ways to enhance language understanding and coherence assessment. The future of NLP holds exciting possibilities for improving human-computer interaction and communication.
    """

    coherence_score = evaluate_coherence(input_text)
    print(f"Coherence Score: {coherence_score}")
