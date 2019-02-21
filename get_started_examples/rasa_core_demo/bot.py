from rasa_core.agent import Agent
from rasa_core.channels.channel import UserMessage
from rasa_core.interpreter import RasaNLUInterpreter

agent = Agent.load("models/dialogue")
message = UserMessage(text="hello")
print(agent.handle_message(message=message))