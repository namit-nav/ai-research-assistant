import ollama
from core.memory import get_memory


def ask_llm(prompt):

    memory = get_memory()

    memory.append({
        "role": "user",
        "content": prompt
    })

    response = ollama.chat(
        model="mistral",
        messages=memory
    )

    answer = response["message"]["content"]

    memory.append({
        "role": "assistant",
        "content": answer
    })

    return answer