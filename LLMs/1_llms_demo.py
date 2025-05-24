from langchain_openai import OpenAI
# is part of the new modular LangChain integration (post langchain v0.1+) and does help you use OpenAI models 
# (like GPT-4 or GPT-3.5) within LangChain.


from dotenv import load_dotenv
# yhn pr dotenv ko import kiye jisse env file load hoga 

load_dotenv()
# env file load kiye
llm = OpenAI(model='gpt-3.5-turbo-instruct')
# open ai k ek object bnaye
result = llm.invoke("What is the capital of India")
# The .invoke() method is used in LangChain to run a model (like an LLM) on an input and get the output.
#  It’s a standard method for executing a chain, prompt, or model call in the new LangChain v0.1+ framework.
# This the string "What is the capital of India?" to the LLM (like OpenAI's GPT).
# The LLM processes the input.
# Sends Returns the response (e.g., "New Delhi").


print(result)