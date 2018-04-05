import os                                                                       
import argparse                                                                 
from process import subprocess                                                                                                          

parser = argparse.ArgumentParser(description='Kaggle competition setup.')
parser.add_argument('name', metavar='N', type=str, nargs='+', 
                     help='Provide kaggle competition name')
NAME = parser.parse_args()                                                       

KAGGLE_CMD = -f'kaggle competitions download -c {NAME}'.format()

FASTAI_PATH = '/home/ubuntu/src/fastai'

DATA_PATH = -f'/home/ubuntu/.kaggle/competetions/{NAME}'.format()                

subprocess.run(KAGGLE_CMD, shell=True, check=True)                               
os.symlink(FASTAI_PATH, 'fastai')                             
os.symlink(DATA_PATH, 'data')