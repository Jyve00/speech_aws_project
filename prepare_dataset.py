import librosa  
import json     
import os 

DATASET_PATH = "data"
JSON_PATH = "data.json"
SAMPLES_TO_CONSIDER = 8000

def prepare_dataset(dataset_path, json_path, n_mfcc=13, hop_length=512, n_fft=2048):

    # data dictionary 
    data = {
        "mappings": [],
    }