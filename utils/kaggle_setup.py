import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Kaggle competition setup.')
parser.add_argument('name', type=str, help='Provide kaggle competition name')
results = parser.parse_args()

competition = results.name
KAGGLE_CMD = 'kaggle competitions download -c ' + competition

FASTAI_PATH = '/home/ubuntu/fastai/fastai/'

DATA_PATH = '/home/ubuntu/.kaggle/competitions/' + competition + '/'

subprocess.run(KAGGLE_CMD, shell=True, check=True)
os.symlink(FASTAI_PATH, 'fastai')
os.symlink(DATA_PATH, 'data')
