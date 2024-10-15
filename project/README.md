# CPSC 324 Big Data Analytics
## Final Report

### Project Description
This project aims to create a model analyzes the sentiment of towards the two presumptive candidates for the presidential election later this year. This model is trained based on 
two datasets that include hashtags #Trump, #DonaldTrump, #Biden, and #JoeBiden during the 
2020 election. The trained model will then be used against two similar but more current datasets 
to see if there is a shift compared to the 2020 version, which will hopefully see if it can predict the 2024 winner.  

### Presentation Links
* [Link](https://drive.google.com/file/d/1P-2wI81Yrb_s5SyXre04Aj2YWusvMNqb/view?usp=sharing)

### How to run this project?
1. Download this dataset
* [Link](https://www.kaggle.com/datasets/manchunhui/us-election-2020-tweets)

2. Install the required libraries
```bash
pip install -r requirements.txt
```

3. Run the Data Preprocessing
```bash
python data_cleaning.py
```

4. Create a Google Cloud project and enable the Vertex API

5. Upload the dataset to Cloud Storage (through a bucket)

6. Add the dataset to the Vertex AI via the "Datasets" tab
* Make sure to choose "Tabular" as the dataset type

8. Train the model
* Use AutoML to train the model
