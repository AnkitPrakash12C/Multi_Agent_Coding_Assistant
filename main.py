from CodingAgents import (
    error_finder_agent, code_debugger_agent,
    concept_explainer_agent, assignment_generator_agent
)
from CodingTasks import (
    find_errors_task, debug_code_task,
    explain_concept_task, generate_assignment_task
)
from crewai import Crew, Process
import streamlit as st

st.title("AI-Powered Coding Assistant")

st.markdown("""
**Get help with your code from a team of AI experts!** Provide your code snippet below, and our AI agents will collaborate to:
1.  **Find Errors:** Identify syntax and logical mistakes. 
2.  **Debug Code:** Provide a corrected, working version. 
3.  **Explain Concepts:** Break down the core programming concepts. 
4.  **Create an Assignment:** Generate a new problem to practice the concept. 
""")

if 'results' not in st.session_state:
    st.session_state.results = None

language = st.text_input("Programming Language", "Python")
user_code = st.text_area("Paste Your Code Here", height=200)

if st.button("Analyze My Code"):
    if not user_code or not language:
        st.error("Please provide the programming language and your code snippet.")
    else:
        with st.spinner("The AI team is analyzing your code... Please wait."):
            task1 = find_errors_task(error_finder_agent, user_code, language)
            task2 = debug_code_task([task1], code_debugger_agent, user_code, language)
            task3 = explain_concept_task([task1, task2], concept_explainer_agent)
            task4 = generate_assignment_task([task3], assignment_generator_agent, language)

            crew = Crew(
                agents=[
                    error_finder_agent,
                    code_debugger_agent,
                    concept_explainer_agent,
                    assignment_generator_agent
                ],
                tasks=[task1, task2, task3, task4],
                process=Process.sequential,
                verbose=True,
            )

            crew.kickoff()

            st.session_state.results = {
                "error_analysis": task1.output.raw,
                "corrected_code": task2.output.raw,
                "concept_explanation": task3.output.raw,
                "assignment": task4.output.raw
            }

if st.session_state.results:
    results = st.session_state.results
    st.subheader("AI Analysis Complete!")

    with st.expander("Error Analysis", expanded=True):
        st.markdown(results["error_analysis"])

    with st.expander("Corrected Code", expanded=True):
        st.markdown(results["corrected_code"])

    with st.expander("Concept Explanation", expanded=True):
        st.markdown(results["concept_explanation"])

    with st.expander("Practice Assignment", expanded=True):
        assignment_content = results["assignment"]
        st.markdown(assignment_content)

        st.download_button(
            label="Download Assignment",
            data=str(assignment_content),
            file_name="coding_assignment.txt",
            mime="text/plain"
        )