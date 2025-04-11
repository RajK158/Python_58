print("!!! Welcome to learn Ai Ml!!!")
print("\n To learn Ai you need to know python.\n If you are already aware of Python start from level 2 or above.\n If not then start with the level 0")
print("\n• Here are the levels choose any one for more description ")
print("🎯 LEVEL 0: Setup & Python Foundations")
print("🎯 LEVEL 1: DSA + Python")
print("🎯 LEVEL 2: Math for AI")
print("🎯 LEVEL 3: Core AI/ML Skills")
print("🎯 LEVEL 4: Amazing AI Projects (Portfolio Boost)")
print("🎯 Enter 5: ")
level=str(input("Select any level to start with.."))
if level == "level 0" or level == "0" :
    print("""Goal: Get comfortable with Python basics.
        ✅ What to learn:
    •	Variables, loops, conditionals, functions
    •	Lists, dictionaries, sets, tuples
    •	File I/O
    •	OOP (classes and objects)
        📘 Resources:
    •	W3Schools Python
    •	Python Official Tutorial
    •	Python Crash Course (Book)
        🛠️ Practice:
    •	HackerRank Python Basics
    •	LeetCode Easy Python Problems """)
elif level == "level 1" or level == "1" :
    print("""Goal: Build your problem-solving skills in Python.
        ✅ What to learn:
    •	Arrays, Strings
    •	Stack, Queue, Linked List
    •	Hash Maps, Sets
    •	Recursion, Binary Search
    •	Trees, Graphs
    •	Sorting, Searching algorithms
        📘 Resources:
    •	NeetCode DSA Roadmap
    •	LeetCode Patterns (Blind 75)
    •	Book: Grokking Algorithms (great visuals!)
        🛠️ Practice:
    •	LeetCode, HackerRank, or Codeforces
          """)
elif level == "level 2" or level == "2" :
    print("""Goal: Understand the math behind AI.
        ✅ What to learn:
    •	Linear Algebra (vectors, matrices)
    •	Probability & Statistics
    •	Calculus (basic understanding of gradients)
    •	Discrete Math (sets, logic, combinations)
        📘 Resources:
    •	Khan Academy - Linear Algebra
    •	3Blue1Brown’s “Essence of Linear Algebra” (YouTube)
    •	Book: Mathematics for Machine Learning by Deisenroth
        """)
elif level == "level 3" or level == "3" :
    print("""Goal: Understand how machines actually learn.
        ✅ What to learn:
    •	Machine Learning (ML)
    o	Supervised vs Unsupervised
    o	Regression, Classification
    o	Decision Trees, SVM, kNN, Clustering
    •	Deep Learning (DL)
    o	Neural Networks
    o	CNNs (image)
    o	RNNs (text/sequences)
    o	Transformers (like ChatGPT)
        📘 Resources:
    •	Andrew Ng’s ML Course (Coursera)
    •	Deep Learning Specialization (Coursera)
    •	Book: Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow by Aurélien Géron
        🛠️ Practice:
    •	Kaggle Projects
    •	Google Colab Notebooks
    •	Build your own models
        """)
elif level == "level 4" or level == "4" :
    print("""
        ✅ Beginner Projects:
    •	Image classifier (e.g. cat vs dog)
    •	Sentiment analyzer (NLP)
    •	Movie recommendation system
    •	Stock price prediction
        ✅ Intermediate Projects:
    •	Chatbot (like mini-ChatGPT)
    •	Face recognition app
    •	Object detection with YOLO or OpenCV
    •	Music genre classification
        ✅ Advanced Projects (CV Booster):
    •	Build your own GPT-like model (with Hugging Face)
    •	AI-powered Resume Screener
    •	AI Tutoring Bot
    •	Autonomous driving simulation (CARLA)
    •	AI in Healthcare (X-ray classifier)
    •	Build your own AI agents
    •	Students (Content ) – Create contents for huge research papers or notes.(Short description)
    •	Medical field - personal health assistant
        📘 Platforms:
    •	Kaggle
    •	Papers with Code
    •	HuggingFace
        """)