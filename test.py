import os
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

print(os.listdir(path='/'))
print(sys.__name__)

with os.scandir("/") as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)



class fiel_maneger(torch.utils.data.Dataset):
    """Some Information about fiel_maneger"""
    def __init__(self):
        super(fiel_maneger, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 

class api_test_install(torch.utils.data.Dataset):
    """Some Information about api_test_install"""
    def __init__(self):
        super(api_test_install, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 


class http_set(torch.utils.data.Dataset):
    """Some Information about http_set"""
    def __init__(self):
        super(http_set, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 


class port_tester(torch.utils.data.Dataset):
    """Some Information about port_tester"""
    def __init__(self):
        super(port_tester, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 


class sys_checer(torch.utils.data.Dataset):
    """Some Information about sys_checer"""
    def __init__(self):
        super(sys_checer, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 


class tey_lanwich(torch.utils.data.Dataset):
    """Some Information about tey_lanwich"""
    def __init__(self):
        super(tey_lanwich, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 
class docker_img_anayis(torch.utils.data.Dataset):
    """Some Information about docker_img_anayis"""
    def __init__(self):
        super(docker_img_anayis, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 

# dataloader = torch.utils.DataLoader(dataset, batch_size=1, suffle=False)

#ein beibility
