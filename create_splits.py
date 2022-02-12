import argparse
import glob
import os
import random

import numpy as np
import shutil
from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    files_length = int(len(glob.glob(data_dir+'/*')))
    files = glob.glob(data_dir+'/*')
    print('files length : ', data_dir+'/*', len(files) )
    train_lst =  files[:int(files_length * 0.73)]
    val_list = files[int(files_length * 0.73):int(files_length * 0.90)]
    print('val_list ', int(files_length * 0.77), int(files_length * 0.90) )
    test_list = files[int(files_length * 0.93):]
    
    for train_file in train_lst:
        shutil.move(train_file, '/home/workspace/data/waymo/train/' + train_file.split('/')[-1])
    
    for val_file in val_list:
        shutil.move(val_file, '/home/workspace/data/waymo/val/' + val_file.split('/')[-1])
                
    for test_file in test_list:
        shutil.move(test_file, '/home/workspace/data/waymo/test/' + test_file.split('/')[-1])
        
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)