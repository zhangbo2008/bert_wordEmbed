'''
bert 词向量:

https://blog.csdn.net/zhonglongshen/article/details/88125958

https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip
权重下载完解压缩到e盘根目录即可.

bert-serving-start  -model_dir E:/chinese_L-12_H-768_A-12 -num_worker=2bert-serving-start  -model_dir E:/chinese_L-12_H-768_A-12 -num_worker=2



pip install  bert-serving-server
pip install bert-serving-client

# 我来弄一个cpu版本的


'''
import os
os.system("bert-serving-start  -model_dir E:/chinese_L-12_H-768_A-12 -num_worker=1 -cpu")























