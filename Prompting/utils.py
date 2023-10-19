import json
from tqdm import tqdm
import torch
import logging
import argparse
import numpy as np

def getResultdata(result_data):
    choice_to_index = {'A':0,'B':1,'C':2,'D':3}

    word_play = {}
    reverse_play = {}
    for item in result_data:
        item_type = item['id'].split("-")[0]
        item_id = item['id'].split("-")[1].split("_")[0]
        if item_type == 'WP':
            if item_id not in word_play:
                word_play[item_id] = [0,0,0]
        else:
            if item_id not in reverse_play:
                reverse_play[item_id] = [0,0,0]

    for item in result_data:
        item_type = item['id'].split("-")[0]
        item_id = item['id'].split("-")[1].split("_")[0]
        ad_type = 0
        if 'SR' in item['id']:
            ad_type = 1
        elif 'CR' in item['id']:
            ad_type = 2
        else:
            ad_type = 0

        if item_type == 'WP':
            if choice_to_index[item['predict']] == item['label']:
                word_play[item_id][ad_type] = 1
        else:
            if choice_to_index[item['predict']] == item['label']:
                reverse_play[item_id][ad_type] = 1
                
    return word_play,reverse_play


def getMetric(data_list):
    data_list = np.array(data_list)
    overall_accuracy = np.sum(data_list)/3/len(data_list)
    original_accuracy = np.sum(data_list,axis = 0)[0]/len(data_list)
    semantic_accuracy = np.sum(data_list,axis = 0)[1]/len(data_list)
    context_accuracy = np.sum(data_list,axis = 0)[2]/len(data_list)
    ori_sema = np.sum([1 if item[0]==1 and item[1] == 1 else 0 for item in data_list])/len(data_list)
    ori_sema_cont = np.sum([1 if item[0]==1 and item[1] == 1 and item[2] == 1  else 0 for item in data_list])/len(data_list)
    
    print("over_all accuracy {}".format(overall_accuracy))
    print("single_original_accuracy {}".format(original_accuracy))
    print("single_semantic_accuracy {}".format(semantic_accuracy))
    print("single_context_accuracy {}".format(context_accuracy))
    print("sr_accuracy {}".format(ori_sema))
    print("cr_accuracy {}".format(ori_sema_cont))

    return {'over_all accuracy':overall_accuracy,'original_accuracy':original_accuracy,'semantic_accuracy':semantic_accuracy,'context_accuracy':context_accuracy,'ori_sema':ori_sema,'ori_sema_cont':ori_sema_cont}


def getSeperateResult(word_play,reverse_thinking):
    final_result = {}
    word_data_list = []
    for item in word_play.values():
        word_data_list.append(item)
    print('#########Wordplay##########')
    final_result['wordplay'] = getMetric(word_data_list)
    
    reverse_data_list = []
    for item in reverse_thinking.values():
        reverse_data_list.append(item)
    print('#########Sentence##########')   
    final_result['sentence'] = getMetric(reverse_data_list)  
    
    
    all_data = word_data_list + reverse_data_list
    print('#########All data##########') 
    final_result['all'] = getMetric(all_data) 
    
    return final_result


