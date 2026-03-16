from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="tinyllama")

def analyze_habits(sleep, study, exercise, screen):

    prompt = f"""
    A student has these daily habits:

    Sleep: {sleep} hours
    Study: {study} hours
    Exercise: {exercise} minutes
    Screen time: {screen} hours

    Analyze the productivity level and give suggestions to improve habits.
    Also provide a productivity score out of 100.
    """

    response = llm.invoke(prompt)

    return response