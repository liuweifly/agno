
from agno.agent import Agent
from agno.models.google import Gemini

agent = Agent(model=Gemini(id="gemini-2.0-flash-exp"), markdown=True)
agent.print_response("What is the stock price of Apple?", stream=True)