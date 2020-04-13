from bert_serving.client import BertClient
bc = BertClient()
print(bc.encode(['中国', '美国']))
print("获得了")# 启用多线程,如果没有服务响应的时候会自动等待,还是符合需求的!!!!!!!!!