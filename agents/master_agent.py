from agents.research_agent import research_company
from agents.document_agent import ask_document
from core.llm import ask_llm
from core.exporter import export_markdown
from core.prompts import comparison_prompt


def decide_tool(query):

    prompt = f"""
You are an AI controller.

Decide which tool should handle the query.

Available tools:
1. research_agent → internet research
2. document_agent → document analysis
3. hybrid → use both

User query:
{query}

Return only one word:
research_agent
document_agent
hybrid
"""

    decision = ask_llm(prompt)

    return decision.strip().lower()


def master_agent():

    print("\nAI Research Assistant Ready")
    print("Commands:")
    print("/research <company>")
    print("/document <file_path>")
    print("/ask <question>")
    print("/export <file_name.md>")
    print("/compare <Company1 Company2>")
    print("/exit\n")

    last_report = ""

    while True:

        command = input(">>> ")

        if command.startswith("/exit"):
            break

        elif command.startswith("/research"):

            company = command.replace("/research", "").strip()

            print("\nRunning internet research...\n")

            result = research_company(company)
            last_report = result
            print("\nResult:\n")
            print(result)

        elif command.startswith("/document"):

            path = command.replace("/document", "").strip()

            from agents.document_agent import load_document

            load_document(path)

        elif command.startswith("/ask"):

            question = command.replace("/ask", "").strip()

            result = ask_document(question)

            print("\nAnswer:\n")
            print(result)

        elif command.startswith("/export"):
            
            filename = command.replace("/export", "").strip()
            
            if last_report == "":
                print("No report available to export.")
            else:
                export_markdown(filename, last_report)
        
        elif command.startswith("/compare"):
            parts = command.split()
            
            if len(parts) != 3:
                print("Usage: /compare <company1> <company2>")
                continue
            company1 = parts[1]
            company2 = parts[2]
            
            print("\nResearching companies...\n")
            info1 = research_company(company1)
            info2 = research_company(company2)
            prompt = comparison_prompt(company1, company2, info1, info2)
            result = ask_llm(prompt)
            print("\nComparison Report:\n")
            print(result)

        else:

            print("Unknown command")


if __name__ == "__main__":

    master_agent()