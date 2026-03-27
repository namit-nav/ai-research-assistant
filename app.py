import streamlit as st

from agents.research_agent import research_company
from agents.planner_agent import plan_research
from agents.document_agent import ask_document, load_document
from core.prompts import comparison_prompt
from core.llm import ask_llm
from core.memory import clear_memory


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Research Assistant", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
# 🤖 AI Research Assistant  
### Powered by LLM + RAG + Multi-Agent System
""")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Choose Feature",
    ["Research", "Planner", "Document Q&A", "Compare"]
)

# ---------------- RESEARCH ----------------
if option == "Research":

    st.header("🔍 Company Research")

    company = st.text_input("Enter Company Name")

    persona = st.selectbox(
        "Choose Persona",
        ["research_assistant", "market_analyst", "sales_strategist"]
    )

    if st.button("Generate Report"):

        if company == "":
            st.warning("Please enter a company name.")
        else:
            clear_memory()

            with st.spinner("Analyzing data and generating insights..."):
                result = research_company(company, persona)

            st.success("Report Generated!")
            st.markdown(result)


# ---------------- PLANNER ----------------
elif option == "Planner":

    st.header("🧠 Research Planner")

    question = st.text_input("Enter your research question")

    if st.button("Generate Plan"):

        if question == "":
            st.warning("Please enter a question.")
        else:
            clear_memory()

            with st.spinner("Breaking down the problem..."):
                result = plan_research(question)

            st.success("Plan Ready!")
            st.markdown(result)


# ---------------- DOCUMENT ----------------
elif option == "Document Q&A":

    st.header("📄 Document Analysis")

    uploaded_file = st.file_uploader("Upload a document")

    if uploaded_file:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        load_document(uploaded_file.name)
        st.success("Document loaded successfully!")

    question = st.text_input("Ask a question about the document")

    if st.button("Ask"):

        if question == "":
            st.warning("Please enter a question.")
        else:
            with st.spinner("Analyzing document..."):
                result = ask_document(question)

            st.success("Answer Generated!")
            st.markdown(result)


# ---------------- COMPARE ----------------
elif option == "Compare":

    st.header("⚖️ Company Comparison")

    company1 = st.text_input("Enter Company 1")
    company2 = st.text_input("Enter Company 2")

    if st.button("Compare"):

        if company1 == "" or company2 == "":
            st.warning("Please enter both company names.")
        else:
            with st.spinner("Researching and comparing companies..."):

                clear_memory()
                info1 = research_company(company1, "research_assistant")

                clear_memory()
                info2 = research_company(company2, "research_assistant")

                prompt = comparison_prompt(company1, company2, info1, info2)
                result = ask_llm(prompt)

            st.success("Comparison Ready!")
            st.markdown(result)