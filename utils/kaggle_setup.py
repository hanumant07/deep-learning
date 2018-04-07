import os
import subprocess
import zipfile


class KaggleSetup():
    def __init__(self, competition, data_path):
        if os.path.isfile(data_path):
            raise Exception('data path is a file')
        self.data_path = data_path
        self.kaggle_cmd = 'kaggle competitions download -c {} -p {}'.format(competition, data_path)

    def download(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
        subprocess.run(self.kaggle_cmd, shell=True, check=True)

    def unzip_all(self):
        for folders, subfolders, files in os.walk(self.data_path):
            for file in files:
                if not file.endswith('.zip'):
                    continue
                # TODO display progress bar
                unzip = zipfile.ZipFile(os.path.join(self.data_path, file))
                unzip.extractall(self.data_path)
