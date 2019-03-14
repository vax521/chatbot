# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import CmdlineInput
from rasa_core.channels.channel import UserMessage
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
# from rasa_core.channels.console import ConsoleInputChannel

logger = logging.getLogger(__name__)
import rasa_core
support_search = ["消费", "流量"]


def extract_item(item):
    """
    check if item supported, this func just for lack of train data.
    :param item: item in track, eg: "流量"、"查流量"
    :return:
    """
    if item is None:
        return None
    for name in support_search:
        if name in item:
            return name
    return None


class ActionSearchConsume(Action):
    def name(self):
        return 'action_search_consume'

    def run(self, dispatcher, tracker, domain):
        item = tracker.get_slot("item")
        item = extract_item(item)
        if item is None:
            dispatcher.utter_message("您好，我现在只会回答公积金有关的问题")
            dispatcher.utter_message("你可以这样问我：“公积金提取”")
            return []

        # time = tracker.get_slot("time")
        # if time is None:
        #     dispatcher.utter_message("您想查询哪个月的消费？")
        #     return []
        # # query database here using item and time as key. but you may normalize time format first.
        # dispatcher.utter_message("好，请稍等")
        # if item == "流量":
        #     dispatcher.utter_message("您好，您{}共使用{}二百八十兆，剩余三十兆。".format(time, item))
        # else:
        #     dispatcher.utter_message("您好，您{}共消费二十八元。".format(time))
        return []

'''
class MobilePolicy(KerasPolicy):
    def model_architecture(self, num_features, num_actions, max_history_len):
        """Build a Keras model and return a compiled model."""
        from keras.layers import LSTM, Activation, Masking, Dense
        from keras.models import Sequential

        n_hidden = 32  # size of hidden layer in LSTM
        # Build Model
        batch_shape = (None, max_history_len, num_features)

        model = Sequential()
        model.add(Masking(-1, batch_input_shape=batch_shape))
        model.add(LSTM(n_hidden, batch_input_shape=batch_shape))
        model.add(Dense(input_dim=n_hidden, output_dim=num_actions))
        model.add(Activation("softmax"))

        model.compile(loss="categorical_crossentropy",
                      optimizer="adam",
                      metrics=["accuracy"])

        logger.debug(model.summary())
        return model
'''


def train_dialogue(domain_file="hr_domain.yml",
                   model_path="projects/dialogue",
                   training_data_file="data/hr_story.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data,
        augmentation_factor=50,
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu.config import RasaNLUModelConfig
    from rasa_nlu.model import Trainer

    training_data = load_data("data/hr_nlu_data.json")
    trainer = Trainer(RasaNLUModelConfig("mobile_nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist("models/", project_name="ivr", fixed_model_name="demo")

    return model_directory


def run(serve_forever=True):
    agent = Agent.load("projects/dialogue", interpreter=RasaNLUInterpreter("projects/ivr_nlu/demo"))
    # input_channel = InputChannel()
    # input_channel.blueprint()
    # if serve_forever:
    #     agent.handle_channels()
    # # print(agent.handle_text("我想看一下消费情况"))
    message = UserMessage(text="我想看一下消费情况")
    print(agent.handle_message(message=message))
    print(rasa_core.__version__)
    # if serve_forever:
    #     agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == "__main__":
    logging.basicConfig(level="INFO")

    parser = argparse.ArgumentParser(
        description="starts the bot")

    parser.add_argument(
        "task",
        choices=["train-nlu", "train-dialogue", "run", "online_train"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    else:
        warnings.warn("Need to pass either 'train-nlu', 'train-dialogue' or "
                      "'run' to use the script.")
        exit(1)
