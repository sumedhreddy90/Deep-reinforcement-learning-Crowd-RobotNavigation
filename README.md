
## Simulation 

### Setput Packages and libraries

```
cd simulation
```
- Install [Python-RVO2](https://github.com/sybrenstuvel/Python-RVO2) library

```
git clone https://github.com/sybrenstuvel/Python-RVO2.git
pip install -r requirements.txt 
python setup.py build
python setup.py install
```
- Install crowd_sim and crowd_nav into pip
```
pip install -e .
```
### After installing all the packages Run below commands to train and test the RL model
1. Train a policy.
```
python train.py --policy scr
```
### Trained Model optimal output:


https://user-images.githubusercontent.com/24978535/167305560-f4d7835f-2940-4b94-bf92-776b99261f4a.mp4



2. Test policies with 500 test cases.
```
python acceptance_test_score.py --policy scr --model_dir data/output --phase test
```
### Score Report:

2022-05-04 14:18:57, INFO: Using device: cpu
2022-05-04 14:18:57, INFO: Policy: SCR w/ global state
2022-05-04 14:18:57, INFO: human number: 5
2022-05-04 14:18:57, INFO: Not randomize human's radius and preferred speed
2022-05-04 14:18:57, INFO: Square width: 10.0, circle width: 4.0
2022-05-04 14:18:57, INFO: Agent is visible and has holonomic kinematic constraint
2022-05-04 14:49:25, INFO: TEST  has success rate: 0.94, collision rate: 0.06, nav time: 9.06, total reward: 0.3574
2022-05-04 14:49:25, INFO: Frequency of being in danger: 3.61, average min separate distance in danger: 0.08
2022-05-04 14:49:25, INFO: Collision cases: 16 21 42 56 60 75 95 112 115 116 129 150 152 166 212 218 220 238 370 392 404 407 426 434 436 442 459 464 469 483 489 490
2022-05-04 14:49:25, INFO: Timeout cases:

3. Visualize a test case
```
python acceptance_test_visualisation.py --policy scr --model_dir data/output --phase test --visualize --test_case 0
```
### Test Case 0
https://user-images.githubusercontent.com/24978535/167305641-6a4b9027-9dea-48ca-a6c6-70ba62ef399d.mov

### Test Case 490

https://user-images.githubusercontent.com/24978535/167305673-f448dd5b-f8c9-48c2-b833-3e9947b90ac5.mov

4. Ocupancy Map visualization:

![scr](https://user-images.githubusercontent.com/24978535/167305724-cf05a8f8-c077-4084-8420-3af019e5fac1.gif)
