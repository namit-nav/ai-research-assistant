from documents.file_loader import load_pdf, load_docx, load_txt
from documents.chunker import chunk_text
from documents.vector_store import store_chunks, search_chunks
from core.llm import ask_llm


def load_document(path):

    if path.endswith(".pdf"):
        text = load_pdf(path)

    elif path.endswith(".docx"):
        text = load_docx(path)

    elif path.endswith(".txt"):
        text = load_txt(path)

    else:
        print("Unsupported file format")
        return

    print("\nDocument loaded.")

    chunks = chunk_text(text)

    store_chunks(chunks)

    print("Document indexed for search.\n")


def ask_document(question):

    relevant_chunks = search_chunks(question)

    context = "\n".join(relevant_chunks)

    prompt = f"""
You are a research assistant.

Use the information below from a document to answer the question.

Context:
{context}

Question:
{question}
"""

    answer = ask_llm(prompt)

    return answer


if __name__ == "__main__":

    path = input("Enter document path: ")

    load_document(path)

    while True:

        question = input("\nAsk a question about the document: ")

        if question.lower() == "exit":
            break

        answer = ask_document(question)

        print("\nAnswer:\n")
        print(answer)