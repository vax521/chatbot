# note:
This project now is updated, some rasa new features will be added soon.(项目已跟进到rasa新版本，一些新特性后面尝试后补充。)

# rasa_chatbot
A Chinese task oriented chatbot in  IVR(Interactive Voice Response) domain， Implement by rasa nlu and rasa core. This is a demo with toy dataset.

### install dependency:

#### python3
install or update to python 3

#### install rasa_core, this will install rasa nlu too, and now support chinese.
```
pip install rasa_core
```
this command will install rasa nlu too.

#### install sklearn and MITIE

```
pip install -U scikit-learn sklearn-crfsuite
pip install git+https://github.com/mit-nlp/MITIE.git
```

#### 训练
```
1. 训练NLU
python -m rasa_nlu.train --data ./data/mobile_nlu_data.json --config hr_chatbot.yml --path projects --fixed_model_name demo --project hr_nlu
2. 训练dialogue
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue -c config.yml
```
#### 测试
```
1. 直接测试
python -m rasa_core.run -d projects/dialogue -u projects/hr_nlu/demo

2. chatroom测试
2.1 
  cd C:\Users\xingxf03\AI\NLP\chatbot\hr_chatbot\chatroom
  yarn serve

   python -m rasa_utils.bot -d models/current/dialogue -u models/current/nlu

```