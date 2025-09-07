from crewai import Task

def find_errors_task(agent, user_code, language):
    return Task(
        description=f"""
        Analyze the following {language} code snippet provided by the user.
        Your job is to identify all syntax errors, logical flaws, and potential bugs.
        Do not fix the code. Create a clear, bulleted list of the errors you find.

        User Code:
        ```
        {user_code}
        ```
        """,
        expected_output="A markdown-formatted bulleted list of all identified errors in the code.",
        agent=agent,
    )

def debug_code_task(context, agent, user_code, language):
    return Task(
        description=f"""
        Here is a {language} code snippet and a list of errors that were found in it.
        Your task is to fix the code to resolve all the listed errors and make it fully functional.
        Provide only the corrected code block in your response.

        Original User Code:
        ```
        {user_code}
        ```
        """,
        expected_output="A single markdown code block containing the complete, corrected code.",
        context=context,
        agent=agent,
    )

def explain_concept_task(context, agent):
    return Task(
        description="""
        Based on the errors found and the corrections made, identify the core programming
        concept that the user was struggling with.
        Provide a simple, clear, and beginner-friendly explanation of this concept.
        Use analogies and simple code examples to illustrate your point.
        """,
        expected_output="A well-formatted markdown explanation of the core programming concept.",
        context=context,
        agent=agent,
    )

def generate_assignment_task(context, agent, language):
    return Task(
        description=f"""
        Based on the concept explanation provided, create a new, subsequent assignment
        or practice problem in {language}.
        This assignment should allow the user to practice the concept they just learned about.
        The problem should be slightly challenging but appropriate for a beginner.
        """,
        expected_output="A markdown-formatted practice problem, including a clear prompt and expected output.",
        context=context,
        agent=agent,
    )