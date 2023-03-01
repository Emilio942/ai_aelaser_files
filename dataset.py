import torch
from torch.utils.data import Dataset
import requests

class WebsiteDataset(Dataset):
    def __init__(self, urls):
        self.urls = urls
        
    def __len__(self):
        return len(self.urls)
    
    def __getitem__(self, idx):
        url = self.urls[idx]
        response = requests.get(url)
        website = response.content
        website = website.decode('utf-8') #decode website
        website = website.lower() #convert website to lowercase
        website = website.split() #split website into words
        return website
