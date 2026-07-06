# Multi-Agent Research System 🤖🔍

A modular, multi-agent AI research ecosystem that automates information gathering, deep content scraping, report drafting, and structured critiquing. Built using **Mistral AI**, **LangChain (LCEL)**, and **Streamlit**, this system deploys a coordinated team of AI agents equipped with specialized tools to deliver comprehensive, verified research briefs.

---

## 🏗️ System Architecture & Data Flow

The project is structured around a stateful execution pipeline using LangChain Expression Language (`LCEL`) and `Runnables`:

1. **Search Agent (`agents.py`):** Takes the research topic and utilizes a `create_react_agent` factory to invoke the **Tavily Search API**, pulling down the top 5 highly relevant web references.
2. **Reader Agent (`agents.py`):** Evaluates the gathered context, selects the most promising URL, and calls **BeautifulSoup** to extract clean web body text.
3. **Writer Chain (`agents.py`):** An LCEL sequence (`prompt | llm | parser`) that aggregates the research to synthesize a structured report (Introduction, Key Findings, Conclusions, and Sources).
4. **Critic Chain (`agents.py`):** An independent LCEL verification loop that strictly critiques the draft, returning a score out of 10 along with structured areas of improvement.

---

## 🛠️ Tech Stack & Dependencies

- **LLM Engine:** Mistral AI (`mistral-large-latest`) via `langchain-mistralai`
- **Agent Orchestration:** LangChain Core & Expression Language (LCEL) chains, and `langgraph` prebuilt runnables
- **Tools:** Tavily Python SDK (`tavily-python`), BeautifulSoup4 (`beautifulsoup4`), Requests
- **User Interface:** Streamlit (Layout engine with reactive tab containers)
- **Environment Management:** Python-dotenv, UV package installer

---
