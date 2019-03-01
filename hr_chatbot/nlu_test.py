from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./projects/hr_nlu/demo")
message = "我想提取公积金?"
result = interpreter.parse(message)
# print(json.dumps(result, indent=2))
# 中文支持
print(json.dumps(result, indent=2, ensure_ascii=False))