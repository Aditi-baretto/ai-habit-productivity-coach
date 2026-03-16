from langchain_ollama import OllamaLLM
from prompts import HABIT_ANALYSIS_PROMPT


llm = OllamaLLM(model="tinyllama")

def analyze_habits(sleep, study, exercise, screen):

    prompt = HABIT_ANALYSIS_PROMPT.format(
        sleep=sleep,
        study=study,
        exercise=exercise,
        screen=screen
    )

    response = llm.invoke(prompt)

    return response
