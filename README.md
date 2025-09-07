# Multi_Agent_Coding_Assistant

This project is a multi-agent AI system designed to act as a personal coding tutor. It helps beginner programmers by analyzing their code, providing fixes, explaining the underlying concepts, and creating new practice problems to reinforce their learning. It was built using the CrewAI framework and is deployed as a live web application on Streamlit Cloud.

## The Problem I'm Solving

When you're new to programming, getting stuck is a huge part of the learning process. It’s often easy to find a quick fix online, but it's much harder to understand *why* your code was wrong in the first place. Without a clear explanation, you're likely to make the same mistake again.

I wanted to build a tool that does more than just debug code. The goal was to create a comprehensive learning loop where a student can get instant, expert-level help that not only fixes their immediate problem but also teaches them the core concepts so they can become a better programmer.

A multi-agent system is perfect for this because tutoring isn't just one skill; it's a combination of different roles. You need a debugger, a teacher, and a curriculum designer. By creating a specialized AI agent for each of these roles, the system can provide a much deeper and more effective learning experience than a single, monolithic AI could.

## How It Works: A Team of AI Experts

The application is built around a team of four AI agents that collaborate in a sequence to help the user.



1.  **The Error Finder:** The first agent acts like a senior developer doing a quick code review. It receives the user's code and its only job is to analyze it and create a bulleted list of all the syntax and logical errors it can find.

2.  **The Code Debugger:** This agent takes the original code and the list of errors from the first agent. Its task is to fix all the identified issues and provide a clean, corrected, and fully working version of the code.

3.  **The Concept Explainer:** This is the teacher. It looks at the errors and the corrections and identifies the main programming concept the user was struggling with (e.g., handling "edge cases" like division by zero). It then provides a simple, beginner-friendly explanation of that concept using analogies and examples.

4.  **The Assignment Generator:** To complete the learning loop, this final agent takes the concept explained by the teacher and creates a new, relevant practice problem. This gives the user a chance to immediately apply what they've just learned.

## Technology Stack

This project was built using a modern, open-source stack:
* **Agent Framework:** **CrewAI** was used to define and orchestrate the four AI agents.
* **Web UI:** The user interface is built with **Streamlit**.
* **Supporting Libraries:** The project also relies on **LangChain** and several of its components to connect everything.

## LLM Selection

* **Model Used for Deployment:** The live application uses **Google's Gemini 1.5 Flash** model. It was chosen because it's a powerful and fast model with a very generous free tier, making it ideal for a publicly deployed student project.
* **Ideal LLM:** An ideal, more powerful alternative would be a model like **GPT-4o** or **Claude 3 Opus**. Their advanced reasoning and coding capabilities would provide even more nuanced feedback and explanations, especially for more complex programming problems.

## Setup and Run Instructions

1.  Clone the repository from GitHub.
2.  Create a virtual environment and install the required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
3.  Create a `.env` file for local development or add your `GOOGLE_API_KEY` to the Streamlit Cloud secrets for deployment.
4.  Run the application.
    ```bash
    streamlit run main.py
    ```
