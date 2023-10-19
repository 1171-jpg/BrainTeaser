### This repository contains data and code for the EMNLP 2023 paper "BRAINTEASER: Lateral Thinking Puzzles for Large Language Models"
### 1. **Data**
* The data of the two subtasks is saved in the **data** folder, *BTDATA.zip*, which contains the data for the sentence puzzle and word puzzle. 
* The data used for training Roberta-L on riddlesense is stored in *rs_train.jsonl* and validation data is stored in *rs_dev.jsonl*.

### 2. **Main experiment**
The code files used for zero/few-shot prompting are all stored in the **prompting** folder:  
* Code for T0pp/T0p/T0 is in *Prompting_T0PP_emnlp.ipynb*.
* Code for FlanT5(11B/3B/780M) is in *Prompting_FlanT5_emnlp.ipynb*.
* Code for ChatGPT is in *Prompting_Chatgpt_emnlp.ipynb*.
* Code for Roberta-L(vanilla/CSKG) is in *Prompting_Roberta_emnlp.ipynb*.
* Code for Roberta-L(RS) is in *Prompting_roberta_riddle_emnlp.ipynb*.
* Code for CAR is in *Prompting_car_emnlp.ipynb*.
* The demonstration examples used in few-shot prompting is stored in *data/demonstration.npy*.
* The code for finetuning Roberta-L on riddlesense is stored in *Finetuned_riddle.ipynb*.
* All models and its checkpoints are publicly available on huggingface, and all methods used in the code are summarized in *utils.py*.
### 3. **Human experiments**
All spreadsheets used for human experiments are stored in **data** folder:
* Human validation data is stored in *human_val.xlsx*.
* Human evaluation data is stored in *human_eval.xlsx*.
* Human open-end task is stored in *human_open.xlsx*.
