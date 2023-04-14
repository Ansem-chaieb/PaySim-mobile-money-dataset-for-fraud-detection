<h1 align="center">PaySim mobile money dataset for fraud detection</h1>

[![Streamlit_App]][streamlit_App_url]

PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country. 

During this project, I worked on exploring the data and building a predictive models to determine whether or not transactions are fraudulent.


<p align="center"><img src ="https://github.com/Ansem-chaieb/Apollo-Agriculture-Case-Study/blob/main/images/apollo.gif" alt = "Bassmalah" class="center"></p>


## Instructions
**1 . Clone the repository:**
```bash
git clone https://github.com/Ansem-chaieb/Apollo-Agriculture-Case-Study.git
cd Apollo-Agriculture-Case-Study/
```
**2 . Set configurations**
before runing the project you need to set same configuration:
* paths, test size, repeated kfold parameters.
* used models (xgboost, lgbm, catboost) parameters.

**3 . Run project**
 ```bash
  python3 main.py --process --eda --train
  ```

  The command comes with 3 flags:
  
--process: load initial dataset, do some memory management and generate some feature so we can use them for analysis.
  
--eda:  use streamlit application to analyse data and visualise models results.

--train: load dataset then split it into train and test then train models using repeated kfold and finally test models and visualise the confusion matrix.
  
## Final results
|Models| train speed(min) | test speed (min) | F1 | recall | Precision | Accuracy | 
|------|------------------|------------------|----|--------|-----------|----------|
|lgbm  |1.2800            |0.9800            |0.5100|0.9960|0.3430     |0.9840    |
|catboost|0.8300          |0.0100            |**0.8820**|**0.8040**|**0.9750**      |0.9980   |


  <!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Streamlit_App]: https://img.shields.io/badge/streamlit-%23FF4B4B.svg?&style=for-the-badge&logo=streamlit&logoColor=white
[streamlit_App_url]: https://share.streamlit.io/ansem-chaieb/apollo-agriculture-case-study/main/src/streamlit_app.py
