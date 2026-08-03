import tkinter as tk
from rapidfuzz import process

faq = {
    "Hi": "Hello! How can I help you?",
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is Python?": "Python is a programming language.",
    "What is machine learning?": "Machine learning allows computers to learn from data.",
    "Who created Python?": "Python was created by Guido van Rossum.",
    "Bye": "Goodbye! Have a nice day."
}

def reply():
    question = entry.get()

    match = process.extractOne(question, faq.keys())

    if match and match[1] >= 60:
        answer.set(faq[match[0]])
    else:
        answer.set("Sorry, I don't know the answer.")

root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("500x300")

tk.Label(root, text="Ask a Question", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Ask", command=reply).pack(pady=10)

answer = tk.StringVar()

tk.Label(root, textvariable=answer, wraplength=450, font=("Arial", 12)).pack(pady=20)

root.mainloop()