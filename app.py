import streamlit as st
from pipeline import run_research_pipeline

# Set page configuration for a wider, more professional layout
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🤖",
    layout="wide"
)

# Sidebar for application details and status
with st.sidebar:
    st.title("⚙️ System Overview")
    st.write("This system uses a multi-agent LCEL architecture:")
    st.markdown('''
    1. **Search Agent**: Finds recent, reliable sources.
    2. **Reader Agent**: Scrapes deep content from the best URL.
    3. **Writer Chain**: Drafts a structured, factual report.
    4. **Critic Chain**: Evaluates the report strictly.
    ''')
    st.divider()
    st.info("Ensure your `.env` file is properly configured with your API keys (e.g., MISTRAL_API_KEY).")

# Main Application UI
st.title("🤖 Multi-Agent AI Researcher")
st.markdown("Enter a topic below to deploy the agents. They will independently search the web, read articles, draft a detailed report, and critique their own work.")

# User Input Section
topic = st.text_input("Enter Research Topic:", placeholder="e.g., The impact of quantum computing on modern cryptography")

# Execution Section
if st.button("Launch Research Agents", type="primary"):
    if not topic.strip():
        st.warning("⚠️ Please enter a valid research topic.")
    else:
        # Use st.status to show a loading state while the pipeline runs
        with st.status(f"Deploying agents for: **{topic}**...", expanded=True) as status:
            st.write("⏳ Pipeline is running. (Check your terminal for detailed step-by-step print statements)")
            
            try:
                # Call the imported pipeline function
                state = run_research_pipeline(topic)
                status.update(label="✅ Research Complete!", state="complete", expanded=False)
                
                st.success("Agents have successfully completed the research lifecycle!")
                
                # Create tabs for better UI organization
                tab1, tab2, tab3 = st.tabs(["📝 Final Report", "⚖️ Critic Feedback", "🔍 Raw Agent Data"])
                
                with tab1:
                    st.header("Research Report")
                    # Display the report. We use markdown so formatting like bolding and lists render correctly.
                    st.markdown(state.get('report', 'No report found.'))
                    
                with tab2:
                    st.header("Critic's Evaluation")
                    # Display the critic's feedback in an info box
                    st.info(state.get('feedback', 'No feedback found.'))
                    
                with tab3:
                    st.subheader("Agent 1: Search Results")
                    st.text_area("Web Search Output", state.get('search_results', ''), height=200)
                    
                    st.subheader("Agent 2: Scraped Content")
                    st.text_area("Scraper Output", state.get('scraped_content', ''), height=200)
                    
            except Exception as e:
                status.update(label="❌ Error occurred", state="error", expanded=False)
                st.error(f"An error occurred during pipeline execution: {e}")