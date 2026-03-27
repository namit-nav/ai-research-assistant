from core.llm import ask_llm


def plan_research(question):

    prompt = f"""
You are an expert research planner.

Break the given question into 5 clear, non-overlapping research questions.

Rules:
- Each question should focus on a different aspect
- Avoid repetition
- Be specific and analytical
- Return ONLY a numbered list

Question:
{question}
"""

    response = ask_llm(prompt)

    return response