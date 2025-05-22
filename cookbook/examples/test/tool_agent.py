from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Gemini(id="gemini-2.5-flash-preview-04-17"),
    tools=[YFinanceTools(stock_price=True)],
    instructions=[
        "Use tables to display data.",
        "Only include the table in your response. No other text.",
    ],
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)

