import os
from llama_index.core.agent import ReActAgent
from llama_index.llms.groq import Groq
from llama_index.core.tools import FunctionTool
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("GROQ_KEY")

model = Groq(model='llama-3.1-8b-instant',temperature=0,api_key=api)

def Add(a:float, b:float) -> float:
    """Add two numbers and return the sum."""
    return a+b

def Subtract(a:float, b:float) -> float:
    """Subtract Second Number with First Number and return final result"""
    return a-b

def Multiply(a:float, b:float) -> float:
    """Multiply two numbers and return the product."""
    return a*b

def Divide(a:float, b:float) -> float:
    """Divide First Number by the Second Number and return the quotient"""
    return a/b

add_tool = FunctionTool.from_defaults(fn=Add)
sub_tool = FunctionTool.from_defaults(fn=Subtract)
multiply_tool = FunctionTool.from_defaults(fn=Multiply)
divide_tool = FunctionTool.from_defaults(fn=Divide)

tools_list =[add_tool,sub_tool,multiply_tool,divide_tool]

agent = ReActAgent.from_tools(tools_list,llm=model,verbose=True)


def main():
    while True:
        user = input("Questions: ")
        response = agent.chat(user)
        print("Agent: ",response)

        if user == "exit":
            break



if __name__ == "__main__":
    main()