from google.adk.agents import Agent # type: ignore

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="An agent that greets the user and offers help with tasks.",
)

