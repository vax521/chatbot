# Formbot - an example which demonstrates the implementation of FormAction

Formbot example is designed to help you understand how the FormAction works and how
to implement it in practice. Using the code and data files in this directory you
can build a simple restaurant search assistant capable of recommending
restaurants based on user preferences.

## What’s inside this example?

This example contains some training data and the main files needed to build an 
assistant on your local machine. The formbot consists of the following files:

- **data/nlu_data.md** contains training examples for NLU model  
- **data/stories.md** contains training stories for Core model  
- **actions.py** contains the implementation of a custom FormAction  
- **domain.yml** contains the domain of the assistant  
- **endpoints.yml** contains the webhook configuration for the custom action  
- **nlu_tensorflow.yml** contains the pipeline configuration of the NLU model  
- **Makefile** contains the shell commands which you can use to run this example  


## How to use this example?

Using this example you can build an actual assistant which demonstrates the
functionality of the FormAction. You can use the example using the following 
steps:

1. Train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/nlu/current/`
folder of your working directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/dialogue`
folder of your working directory.

4. Test the assistant by running:  
```make run```  
This will load the assistant in your command line for you to chat.


## Encountered any issues?
Let us know about it by posting on [Rasa Community Forum](https://forum.rasa.com)!
