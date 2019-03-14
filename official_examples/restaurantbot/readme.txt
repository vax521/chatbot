
1. 训练NLU
python -m rasa_nlu.train -c nlu_model_config.yml --data ./data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose

2. 训练core
 python -m rasa_core.train -d restaurant_domain.yml -s ./data/babi_stories.md -o models/dialogue

 3.与chatroom 配合测试
 启动前段应用：yarn serve
 新建窗口：python -m utils.bot -d models/dialogue -u models/nlu/default/current
