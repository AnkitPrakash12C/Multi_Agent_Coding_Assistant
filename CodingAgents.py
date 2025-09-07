from crewai import Agent
from crewai import LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

error_finder_agent = Agent(
    role="Senior Code Error Analyst",
    goal="""Analyze the provided code to find and list all syntax and logical errors.
    Provide clear, concise descriptions of each error found.""",
    backstory="""You are an expert software developer with decades of experience in debugging.
    You have a keen eye for detail and can spot errors that others might miss.
    You do not fix the code; you only identify and list the problems.""",
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

code_debugger_agent = Agent(
    role="Expert Code Debugger",
    goal="""Receive a piece of code and a list of errors, and provide a corrected,
    fully functional version of the code that addresses all identified issues.""",
    backstory="""You are a master programmer known for your ability to fix any bug.
    Given a broken piece of code and an analysis of its errors, you can quickly
    produce a clean, working solution.""",
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

concept_explainer_agent = Agent(
    role="Programming Concept Educator",
    goal="""Explain the core programming concepts related to the errors found in the code.
    Your explanation should be clear, simple, and easy for a beginner to understand.""",
    backstory="""You are a beloved computer science professor who can break down
    complex topics into simple, digestible analogies and explanations. You focus on
    the 'why' behind the code, helping students build a solid foundation.""",
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

assignment_generator_agent = Agent(
    role="Coding Assignment Creator",
    goal="""Create a new, relevant coding assignment or practice problem that helps
    the user practice and reinforce the concepts they just learned about.""",
    backstory="""You are a creative curriculum developer who designs engaging coding
    challenges. Your assignments are designed to be slightly challenging but achievable,
    solidifying the user's understanding of a specific programming concept.""",
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)