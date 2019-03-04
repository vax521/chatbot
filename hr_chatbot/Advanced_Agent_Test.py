from utils.bot_server_channel import BotServerInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter


# Creating the Interpreter and Agent
def load_agent():
    agent = Agent.load("projects/dialogue", interpreter=RasaNLUInterpreter("projects/hr_nlu/demo"))
    return agent


# Creating the server
def main_server():
    agent = load_agent()
    channel = BotServerInputChannel(agent, port=5005)
    agent.handle_channels([channel], http_port=5005)


if __name__ == '__main__':
        main_server()