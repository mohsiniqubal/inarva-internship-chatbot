import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load documents
data_folder = "data"
documents = []
doc_names = []

for file_name in os.listdir(data_folder):
    if file_name.endswith(".txt"):
        with open(os.path.join(data_folder, file_name), "r", encoding="utf-8") as f:
            documents.append(f.read())
            doc_names.append(file_name)

# Create TF-IDF embeddings
vectorizer = TfidfVectorizer(stop_words="english")
doc_vectors = vectorizer.fit_transform(documents)

print("Internship & Placement FAQ Chatbot")
print("Type 'exit' to quit\n")

while True:
    query = input("Ask a question: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, doc_vectors)[0]

    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    if best_score < 0.1:
        print("\nAnswer: Sorry, I could not find relevant information.\n")
    else:
        print("\nAnswer (from document):")
        print(documents[best_match_index])
        print()
