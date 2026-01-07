# Internship & Placement FAQ Chatbot (RAG-Based)

## 📌 Problem Statement
Students often struggle to find accurate and timely information related to internships and placements because details are scattered across multiple documents such as guidelines, eligibility criteria, and placement rules. This leads to confusion, repeated queries, and difficulty in accessing the right information.

The goal of this project is to build a chatbot that allows students to ask natural language questions and receive accurate, document-based answers by retrieving relevant information from internship and placement documents.

---

## 💡 Solution Overview
This project implements a document-based chatbot using a **Retrieval-Augmented Generation (RAG)** style approach.  
Instead of generating answers blindly, the chatbot retrieves relevant content from stored documents and responds based only on that information.

The chatbot:
- Loads internship and placement documents
- Converts document text into vector representations
- Finds the most relevant document content for a user query
- Returns answers grounded in the source documents

This ensures clarity, correctness, and avoids hallucinated responses.

---

## 🏗️ Architecture / RAG Flow

Documents (.txt)
↓
Text Preprocessing
↓
Vector Embeddings (TF-IDF)
↓
Similarity Search (Cosine Similarity)
↓
Relevant Document Retrieval
↓
Answer to User

yaml
Copy code

---

## 🧠 Technologies & Tools Used
- **Python**
- **scikit-learn** (TF-IDF Vectorizer, Cosine Similarity)
- **VS Code**
- **GitHub**
- **Virtual Environment (venv)**

> Note: TF-IDF embeddings were used to ensure the system runs locally without dependency on paid APIs. The architecture is designed so that embeddings or LLMs (Azure OpenAI / AWS Bedrock) can be plugged in easily in production.

---

## 📂 Project Structure
inarva-internship-chatbot/
│
├── app.py
├── README.md
├── requirements.txt
└── data/
├── internship_guidelines.txt
├── eligibility.txt
└── placement_rules.txt

yaml
Copy code

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-link>
cd inarva-internship-chatbot
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\Activate
3️⃣ Install Dependencies
bash
Copy code
pip install scikit-learn
4️⃣ Run the Chatbot
bash
Copy code
python app.py
🧪 Sample Questions to Ask
What is the minimum CGPA required?

Who is eligible for internships?

Are students with backlogs allowed?

What are the placement rules?

Can final year students apply?

🎥 Project Explanation Video
A 5–10 minute explanation video is included in this repository (or linked here), where I explain:

The problem statement

Overall system architecture

RAG flow

Code walkthrough

Learnings and challenges faced

📚 Key Learnings
Understood how Retrieval-Augmented systems work

Learned document preprocessing and similarity-based retrieval

Gained hands-on experience with Python-based AI workflows

Improved ability to design explainable, real-world AI solutions

⚠️ Challenges Faced
Managing external API quotas

Handling library compatibility issues on Windows

Designing a system that is both simple and scalable

These challenges helped me better understand real-world constraints and engineering trade-offs.

✅ Conclusion
This project demonstrates a clear understanding of AI system design, document retrieval, and chatbot development. The architecture is simple, extensible, and aligned with real-world production practices.

Author: Mohsin Iqubal
Role: MCA Student
Project Type: AI / ML Internship Assessment