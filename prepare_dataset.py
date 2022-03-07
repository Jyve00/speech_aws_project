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
        "labels": [], 
        "MFCCs": [],
        "files": []
    }

    # loop through all the sub-dirs
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # need to ensure that we're not at root level 
        if dirpath is not dataset_path:
            # update mappings 
            category = dirpath.split("/")[-1] # dataset/down -> [dataset, down]
            data['mappings'].append(category)

            # loop through all the filenames and extract MFCCs
            for f in filenames: 

                # get file path 

                # load audio file 

                # 


