import ollama
from core.memory import get_memory


def ask_llm(prompt):

    memory = get_memory()

    # Limit memory (keep last 6 messages)
    memory = memory[-6:]

    # Add system role (important for better output)
    messages = [
        {
            "role": "system",
            "content": "You are a professional AI research assistant that provides clear, structured, and analytical answers."
        }
    ]

    # Add memory context
    messages.extend(memory)

    # Add current prompt
    messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        response = ollama.chat(
            model="mistral",
            messages=messages
        )

        answer = response["message"]["content"]

        # Save only meaningful memory (not full history)
        memory.append({
            "role": "user",
            "content": prompt
        })

        memory.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    except Exception:
        return "Error: Unable to generate response. Please try again."