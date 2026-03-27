from agents.research_agent import research_company
from agents.document_agent import ask_document, load_document
from core.llm import ask_llm
from core.exporter import export_markdown
from core.prompts import comparison_prompt
from core.memory import clear_memory


def master_agent():

    print("\nAI Research Assistant Ready")
    print("Commands:")
    print("/research <company>")
    print("/document <file_path>")
    print("/ask <question>")
    print("/export <file_name.md>")
    print("/compare <company1> <company2>")
    print("/exit\n")

    last_report = ""

    while True:

        command = input(">>> ").strip()

        if command.startswith("/exit"):
            break

        elif command.startswith("/research"):

            clear_memory()

            company = command.replace("/research", "").strip()

            persona = input("Choose persona (research_assistant / market_analyst / sales_strategist): ").strip()

            print("\nGenerating report...\n")

            result = research_company(company, persona)

            last_report = result

            print("\nResult:\n")
            print(result)

        elif command.startswith("/document"):

            path = command.replace("/document", "").strip()
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

            clear_memory()

            print("\nResearching companies...\n")

            info1 = research_company(company1, "research_assistant")
            info2 = research_company(company2, "research_assistant")

            prompt = comparison_prompt(company1, company2, info1, info2)

            result = ask_llm(prompt)

            print("\nComparison Report:\n")
            print(result)

        else:

            print("Unknown command")


if __name__ == "__main__":
    master_agent()