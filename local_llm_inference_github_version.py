# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 07:42:18 2025

@author: georg
"""

import ollama
import uuid


def local_llm_infer(prompt,  max_tokens = 30, model = "gemma3:1b"):
    result = ollama.chat(
            model = model,
            messages = prompt,
            options={
                "stream": False,
                "num_predict": max_tokens,
                "temperature": 0.0,
                "think": False
    })
    return result['message']['content'].strip()

def local_llm_infer_v2(prompt_text, max_tokens=500, model="gemma3:1b"):
    
    result = ollama.generate(
        model=model,
        prompt=prompt_text,
        options={
            "num_predict": max_tokens,
            "temperature": 0.0,
            "top_p": 1.0,
            "seed": 2107
        }
    )
    return result["response"].strip()

#local_llm_infer(test_prompt("What is the beste sportscar to buy?"), 200)


