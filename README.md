# BRAINTEASER: Lateral Thinking Puzzles for Large Language Models

### This repository contains data and code for the EMNLP 2023 paper "BRAINTEASER: Lateral Thinking Puzzles for Large Language Models". See the full paper [here](https://arxiv.org/abs/2310.05057).
### 1. **Data**
* The data of the two subtasks is saved in the **data** folder, *BTDATA.zip*, which contains the data for the sentence puzzle and word puzzle. 
* The data for training Roberta-L(RS) on RiddleSense is stored in *rs_train.jsonl*, and validation data is stored in *rs_dev.jsonl*.

**Note:** The brain teaser was also selected as one of the interesting competitions in [SemEval 2024](https://brainteasersem.github.io/), so we created a split for the Semeval Competition (train/test). The data contained in *BTDATA.zip* are as follows:

- Semeval Competition
  - Training Data
    - `SP_train.npy` (Semeval training data)
    - `WP_train.npy` (Semeval training data)
  - Test Data
    - `SP_test.npy` (Semeval test data)
    - `WP_test.npy` (Semeval test data)
    - `SP_test_answer.npy` (Semeval test data answer)
    - `WP_test_answer.npy` (Semeval test data answer)
- EMNLP Zero-Shot Experiment
  - `sentence_puzzle.npy` (on all sentence puzzle data)
  - `word_puzzle.npy` (on all word puzzle data)





**Note:** To prevent automatic data crawlers, *BTDATA.zip* needs a password: **brainteaser**

### 2. **Relation to SemEval2024-Task9**

The relationship between EMNLP and SemEval involves using the same dataset but with different data splitting and utilization methods. In EMNLP, the entire dataset is employed for testing, while in SemEval, the dataset is divided into training and testing sets, with the training set comprising a significant majority. 

Our EMNLP paper results on GitHub are tested on the entire data in a **zero-shot manner**. In the SemEval2024-Task9, although the whole dataset is the same as our EMNLP paper, we allow people to **train on 80% of the whole dataset**, and we **evaluate the system on the 20% left**. 

### 3. **Model evaluation**
The code files used for zero/few-shot prompting are all stored in the **prompting** folder:  
* The code for T0pp/T0p/T0 is in *Prompting_T0PP_emnlp.ipynb*.
* The code for FlanT5(11B/3B/780M) is in *Prompting_FlanT5_emnlp.ipynb*.
* The code for ChatGPT is in *Prompting_Chatgpt_emnlp.ipynb*.
* The code for Roberta-L(vanilla/CSKG) is in *Prompting_Roberta_emnlp.ipynb*.
* The code for Roberta-L(RS) is in *Prompting_roberta_riddle_emnlp.ipynb*.
* The code for CAR is in *Prompting_car_emnlp.ipynb*.
* The demonstration examples used in few-shot prompting are stored in *data/demonstration.npy*.
* The code for finetuning Roberta-L(RS) on RiddleSense is stored in *Finetuned_riddle.ipynb*.
* All models and their checkpoints are publicly available on the Hugging Face, and all methods used in the code are summarized in *utils.py*.
### 4. **Human experiments**
All spreadsheets used for human experiments are stored in the **data** folder:
* The human validation data is stored in *human_val.xlsx*.
* The human evaluation data is stored in *human_eval.xlsx*.
* The human open-end task is stored in *human_open.xlsx*.

### Cite
```
@inproceedings{jiang2023brainteaser,
      title={BRAINTEASER: Lateral Thinking Puzzles for Large Language Models}, 
      author={Yifan Jiang and Filip Ilievski and Kaixin Ma and Zhivar Sourati},
      year={2023},
      booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing}
}
```
