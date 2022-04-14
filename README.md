# DS-RNN-RobotNavigation-DRL

```
1. Install Python3.8 (3.6 or higher is highly recommended).
sudo apt install python3.8

2. Install the required python package using pip. We can use
below command to install all the required packages
pip install -r requirements.txt
The above requirements.txt file consists of below packages:
-> numpy
-> pandas
-> pytorch
-> torchvision
-> gym
-> tensorflow
-> matplotlib

3. Install OpenAI Baselines.
git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .

4. Install Python-RVO2 library.
git clone https://github.com/sybrenstuvel/Python-RVO2.git
pip install Cython
cd Python-RVO2
python setup.py build
python setup.py install
```