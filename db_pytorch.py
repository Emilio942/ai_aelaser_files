import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import docker
import urllib.request
from list import   url_list


##############################################
# Error lists
##############################################


class fiel_search(torch.utils.data.Dataset):
    """Some Information about fiel_search"""

    def __init__(self):
        super(fiel_search, self).__init__()

    def __getitem__(self, index):
        return

    def __len__(self):
        return


class erro_set_db(torch.utils.data.Dataset):
    """Some Information about erro_set_db"""

    def __init__(self):
        super(erro_set_db, self).__init__()

    def __getitem__(self, index):
        return

    def __len__(self):
        return


class port_set(torch.utils.data.Dataset):
    """Some Information about port_set"""

    def __init__(self):
        super(port_set, self).__init__()

    def __getitem__(self, index):
        return

    def __len__(self):
        return


class http_db(torch.utils.data.Dataset):
    """Some Information about http_db"""

    def __init__(self):
        super(http_db, self).__init__()

    def __getitem__(self, index):
        return

    def __len__(self):
        return
#####################################################
# Eror lists end
#####################################################


#####################################################
# server + web site  test
#####################################################

class docker_server(torch.utils.data.Dataset):
    """Some Information about docker_server"""
    def __init__(self):
        super(docker_server, self).__init__()
        os.system("echo GeeksForGeeks")
        self.test1_net = docker.from_env()
        self.test2_net = docker.from_env()
        self.test3_net = docker.from_env()
        self.test4_net = docker.from_env()
        self.test5_net = docker.from_env()
        self.test6_net = docker.from_env()
        self.test7_net = docker.from_env()
        self.test8_net = docker.from_env()
        self.test9_net = docker.from_env()
        self.test10_net = docker.from_env()
        self.test11_net = docker.from_env()
        self.test12_net = docker.from_env()
        self.test13_net = docker.from_env()
        self.test14_net = docker.from_env()
        self.test15_net = docker.from_env()
        self.test16_net = docker.from_env()
        self.test17_net = docker.from_env()
        self.test18_net = docker.from_env()
        self.test19_net = docker.from_env()
        self.test20_net = docker.from_env()
        self.test21_net = docker.from_env()
        self.test22_net = docker.from_env()
        self.test23_net = docker.from_env()
        self.test24_net = docker.from_env()
        self.test25_net = docker.from_env()
        self.test26_net = docker.from_env()
        self.test27_net = docker.from_env()
        self.test28_net = docker.from_env()
        self.test29_net = docker.from_env()
        self.test30_net = docker.from_env()

    def web_sever(self, server_tye, sripe):
        ###################################################################
        # Exemple
        # self.dhd=self.containers.run("ubuntu:latest", "echo hello world")
        ###################################################################
        docker_list: list = [
            self.test1_net.containers.run(server_tye, sripe),
            self.test2_net.containers.run(server_tye, sripe),
            self.test3_net.containers.run(server_tye, sripe),
            self.test4_net.containers.run(server_tye, sripe),
            self.test5_net.containers.run(server_tye, sripe),
            self.test6_net.containers.run(server_tye, sripe),
            self.test7_net.containers.run(server_tye, sripe),
            self.test8_net.containers.run(server_tye, sripe),
            self.test9_net.containers.run(server_tye, sripe),
            self.test10_net.containers.run(server_tye, sripe),
            self.test11_net.containers.run(server_tye, sripe),
            self.test12_net.containers.run(server_tye, sripe),
            self.test13_net.containers.run(server_tye, sripe),
            self.test14_net.containers.run(server_tye, sripe),
            self.test15_net.containers.run(server_tye, sripe),
            self.test16_net.containers.run(server_tye, sripe),
            self.test17_net.containers.run(server_tye, sripe),
            self.test18_net.containers.run(server_tye, sripe),
            self.test19_net.containers.run(server_tye, sripe),
            self.test20_net.containers.run(server_tye, sripe),
            self.test21_net.containers.run(server_tye, sripe),
            self.test22_net.containers.run(server_tye, sripe),
            self.test23_net.containers.run(server_tye, sripe),
            self.test24_net.containers.run(server_tye, sripe),
            self.test25_net.containers.run(server_tye, sripe),
            self.test26_net.containers.run(server_tye, sripe),
            self.test27_net.containers.run(server_tye, sripe),
            self.test28_net.containers.run(server_tye, sripe),
            self.test29_net.containers.run(server_tye, sripe),
            self.test30_net.containers.run(server_tye, sripe)
        ]

        self.test1 = self.test1_net.containers.run(server_tye, sripe)
        self.test2 = self.test2_net.containers.run(server_tye, sripe)
        self.test3 = self.test3_net.containers.run(server_tye, sripe)
        self.test4 = self.test4_net.containers.run(server_tye, sripe)
        self.test5 = self.test5_net.containers.run(server_tye, sripe)
        self.test6 = self.test6_net.containers.run(server_tye, sripe)
        self.test7 = self.test7_net.containers.run(server_tye, sripe)
        self.test8 = self.test8_net.containers.run(server_tye, sripe)
        self.test9 = self.test9_net.containers.run(server_tye, sripe)
        self.servert1 = self.test10_net.containers.run(server_tye, sripe)
        self.servert2 = self.test11_net.containers.run(server_tye, sripe)
        self.servert3 = self.test12_net.containers.run(server_tye, sripe)
        self.servert4 = self.test13_net.containers.run(server_tye, sripe)
        self.servert5 = self.test14_net.containers.run(server_tye, sripe)
        self.servert6 = self.test15_net.containers.run(server_tye, sripe)
        self.servert7 = self.test16_net.containers.run(server_tye, sripe)
        self.servert8 = self.test17_net.containers.run(server_tye, sripe)
        self.servert9 = self.test18_net.containers.run(server_tye, sripe)
        self.servert0 = self.test19_net.containers.run(server_tye, sripe)
        self.servert11 = self.test20_net.containers.run(server_tye, sripe)
        self.servert12 = self.test21_net.containers.run(server_tye, sripe)
        self.servert13= self.test22_net.containers.run(server_tye, sripe)
        self.servert14 = self.test23_net.containers.run(server_tye, sripe)
        self.servert15 = self.test24_net.containers.run(server_tye, sripe)
        self.servert16 = self.test25_net.containers.run(server_tye, sripe)
        self.servert17 = self.test26_net.containers.run(server_tye, sripe)
        self.servert18 = self.test27_net.containers.run(server_tye, sripe)
        self.servert19 = self.test28_net.containers.run(server_tye, sripe)
        self.servert20 = self.test29_net.containers.run(server_tye, sripe)
        self.servert21 = self.test30_net.containers.run(server_tye, sripe)

    def fiel(self, fiels: str):
        S=os.listdir()
        for file in S :
            for fiel in file:
                with open(fiel) as f:
                    fii = f.read()
                    print(fii)
                    return fii

    def db(self):
        
        for i in url_list:
            for url in  url_list:
                site= urllib.request.urlopen(url=url)
                site= site.read()

                for i in site.split():
                    if i == "htttps://":
                        for url_i in url_list:
                            if i == url_i:
                                break
                            elif i == str():
                                url_list.append(i)
                            else:
                                print("Error Emilio if")
            
            with urllib.request.urlopen(str(i)) as f:
                print(f.read())
                list_data_texit:list = []
            list_data_texit.append(f)


        for web in list_data_texit:
            client = docker.from_env()

            
            client.containers.run("bfirsh/reticulate-splines", detach=True)
            dockerList= client.containers.list()
            for contener in dockerList:

                container = client.containers.get(str(contener))
        site = urllib.request.urlopen

           
        
                

            
        
        
    

    def __getitem__(self, index):
        return index

    def __len__(self):
        return
