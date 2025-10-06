# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 08:58:35 2025

@author: ggoldenits
"""

import os
import sys
import ollama
import pandas as pd
import re
import json
import time
import ast


ROOT = "/workspace/scripts"
sys.path.append(ROOT)


from local_llm_inference_github_version import *
from prompt_template_github_version import *
from extract_json_github_version import *



# ---- Read Data ----

data_path = "/workspace/dataset/temp"
files = os.listdir(data_path)
#print(files)

d = {}

# Load all JSON files into dictionary d
for i in files:
    if i.endswith("json"):
        with open(os.path.join(data_path, i), 'r') as file:
            d[i] = json.load(file)

# Extract phishing keys
phish = list(d["phish_5_url.json"].keys())

# Merge benign and phishing datasets into d5
d5 = d["benign_5_url.json"]
d5.update(d["phish_5_url.json"])

#d50 = d["benign_50.json"]
#d50.update(d["phish_50.json"])


d_all = {"d5":d5}#,"d50": d50}

# ---- Read Models ----
#either directly from the model directory
model_list = [i["model"] for i in ollama.list()["models"]]

#or manually
#model_list = ["dolphin3:8b", "phi3:medium", "mistral-nemo:latest", "qwen3:4b", "gemma3:4b", "gemma3:12b", "deepseek-r1:1.5b", "llama3.2:1b", "llama3.1:8b"]


# ---- Create CSV Loop ----
page_runs = 2

t5=time.time()
for m in model_list:
    result_collection = {} # stores results per model
    
    if not m in result_collection.keys():
        result_collection[m] = {}
       
    print(m)
    print(time.time())
    
    for dname, ds in d_all.items():
        if not dname in result_collection[m].keys():
            result_collection[m][dname] = {}
            
        pageID = 0
    
        # Iterate over dataset entries (websites)
        for ws_name, ws in list(ds.items()):
            
            if not pageID in result_collection[m][dname].keys():
                result_collection[m][dname][pageID] = {}
                
            true_label = ws_name in phish
            
            for i in range(page_runs):
                run_result = {}
                
                # Build prompt from HTML and metadata
                html_prompt = build_html_prompt_v4(ws, len(ws))
                
                # Run model inference and time it
                t1 = time.time()
                analysis_result = local_llm_infer_v2(html_prompt, max_tokens = 750, model = m)
                t2 = time.time()
                
                # Store results
                run_result["ws_name"] = ws_name
                run_result["True_Phish_Label"] = true_label
                run_result["runtime"] = t2 - t1
                run_result["prompt_len"] = len(html_prompt)
                run_result["analysis_result"] = analysis_result
                
                result_collection[m][dname][pageID][i] = run_result 
                
            # Save intermediate results periodically
            if pageID in [200,400,600,800]:
                save_loc1 = f"/workspace/results/temp/res_{m}_all_{pageID}.json"
                with open(save_loc1, 'w') as fp:
                    json.dump(result_collection, fp)
                    
            pageID += 1
            
    # Save results for this model        
    save_loc = f"/workspace/results/temp/res_{m}_all.json"
    with open(save_loc, 'w') as fp:
        json.dump(result_collection, fp) 
t6=time.time()