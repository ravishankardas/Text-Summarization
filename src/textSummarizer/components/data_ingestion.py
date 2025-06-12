import os
from pathlib import Path
import urllib.request as request
import zipfile
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from: {self.config.source_URL}")
            filename, _ = request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"Downloaded file: {filename} with size: {get_size(Path(filename))}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file} with size: {get_size(self.config.local_data_file)}")
    

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            logger.info(f"Extracting file to: {unzip_path}")
            zip_ref.extractall(unzip_path)
            logger.info(f"Extraction completed. Files extracted to: {unzip_path}")
