import pip 
import os 

os.system("python3 -m venv venv_torch")
os.system("source ./venv_torch/bin/activate ")
os.system("pip install torch ")
os.system("pip install docker")
os.system("pip install discord")

pip.main(["install","torch","discord","docker" ])