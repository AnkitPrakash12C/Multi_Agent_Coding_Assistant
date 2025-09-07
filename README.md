# Multi-Agent Coding Assistant

# AI-Powered Coding Assistant

This project is a multi-agent AI system I built to act as a personal coding tutor. It's designed to help beginner programmers by analyzing their code, providing fixes, explaining the core concepts behind the errors, and even creating new practice problems to help them learn.

The application was built using the CrewAI framework and is designed to run locally with Ollama.

## The Problem I'm Solving

When you're first learning to code, it's really common to get stuck. While you can often find a quick fix online, it's much harder to understand *why* your code was wrong in the first place. Without a clear explanation, you're likely to make the same mistake again.

I wanted to build a tool that does more than just debug code. The goal was to create a comprehensive learning loop where a student can get instant, expert-level help that not only fixes their immediate problem but also teaches them the core concepts so they can become a better programmer.

This is where a multi-agent system really shines. Tutoring isn't just one job; it's a combination of different roles. You need someone to spot errors, someone to fix them, a teacher to explain things, and a mentor to give you practice. By creating a specialized AI agent for each of these roles, the system can provide a much deeper and more helpful learning experience than a single AI ever could.

## How It Works: Multiple-Agents

The application is powered by a team of four specialist AI agents that work together in a sequence to provide a complete analysis for the user.

1.  **The Error Finder:** This agent performs a quick code review. It takes the user's code and it's job is to analyze it and create a simple, bulleted list of any syntax or logical errors it finds.

2.  **The Code Debugger:** This agent receives the original code snippet and the list of errors from the first agent. Its task is to correct all the identified issues and provide a clean, fully functional version of the code.

3.  **The Concept Explainer:** This is the explainer in the group. It looks at the original errors and the corrected code to identify the main programming concept the user was struggling with (for example, handling "edge cases" like division by zero). It then provides a simple, beginner-friendly explanation of that concept.

4.  **The Assignment Generator:** To complete the learning loop, this final agent takes the concept that was just explained and creates a brand-new practice problem. Also added a download button, so the user can easily save this assignment as a `.txt` file to work on later.

## Technology Stack

This project was built using a modern, open-source stack that is perfect for rapid development and testing:

* **Agent Framework:** **CrewAI** was used to define the agents and orchestrate their collaborative workflow.
* **Web UI Framework:** The entire user interface is built with **Streamlit**.
* **LLM:** The agents are powered by **Ollama**, which allows for running powerful open-source models locally.
* **Supporting Libraries:** The project also relies on the **LangChain** library and its various components to connect the agents to the language model.

## LLM Selection

* **Model Used for Development:** This project was developed and tested using **Ollama** to run the **Llama 3.2** model locally. This is an excellent free-tier option that provides powerful reasoning capabilities without any API costs, making it perfect for building and iterating on the project.

* **Ideal LLM for Deployment:** If this were a publicly deployed application for many users, an ideal choice would be a cloud-based model like **Google's Gemini 1.5 Flash** or **OpenAI's GPT-4o**. Using a cloud API would mean that end-users wouldn't need to install or run Ollama on their own machines, making the application much more accessible and scalable.

## How to Set Up and Run the Project

To run this project on your own machine, you'll need to have Ollama installed and running.

1.  **Install Ollama:** Follow the instructions on the [Ollama website](https://ollama.com/) to download and install it for your operating system.

2.  **Pull the Llama 3.2 Model:** Once Ollama is running, open your terminal and run the following command to download the model used in this project:
    ```bash
    ollama run llama3.2
    ```

3.  **Clone the Project:** Clone this repository to your local machine.

4.  **Install Dependencies:** Navigate to the project folder, create a Python virtual environment, and install the required packages from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the App:** Once the dependencies are installed and Ollama is running, you can start the Streamlit application:
    ```bash
    streamlit run main.py
    ```
