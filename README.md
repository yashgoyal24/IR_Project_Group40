## Text-Based Hotel Review Retrieval System <br /> <br />

# END-SEM WORK Folder consists of our final project submitted for end-sem evaluation <br /> 
 "IR_Project_Group40_Final.pdf" consists of the Final Report of our project. <br />
 "Testing_diff_models.ipynb" is .ipynb file for running models on larger dataset(500k reviews) <br />
 "IR_Proj_Final.ipynb" is Final ipnyb file from aspect segmentation to ranking of hotels. <br />

 "User Interface" directory consists of code for the User Interface and Flask App <br />
  Heroku Link for accessing project: https://hotel-review-ir.herokuapp.com/ <br /> <br />
Drive Link: https://drive.google.com/drive/u/1/folders/1o1eEImxseF1eo3tTtlEqrR6jaNr2b2TQ
 
 
# These Files and Folders were submitted for our Mid-term evaluation <br /> 
 "IR_Project_Group40.pdf" consists of the Report of our project. <br /> <br />
 "Models" Folder consists of our models we ran as baselines. <br />
    (The Random Forest Model Drive Link: https://drive.google.com/file/d/1-JUj_yGH9jAyhfBeW19bq_6BAttwjSYI/view?usp=sharing )   <br /> <br />
  "Pre-processing" Folder consists of all the python code used during preprocessing of our data. <br />
         --> In ParsePrimary.py, we did the basic cleaning of data, i.e, extracting the hotel and location name from the url present in the reviews, and removing the reviews with no property dictionary present. <br />
         --> In FetchRecords.py, we extracted the reviews which contained the same 6 parameters being rated. <br />
         --> In ProcessText.py, we implemented the basic preprocessing steps such as (i) conversion to lowercase, (ii) Removing Punctuation and Stopwords and (iii) Stemming the words. <br /> <br />
   "IR_Proj.ipynb" consists of our notebook where everything was implemented. <br /> <br />
 Dataset Link: http://lia.epfl.ch/Datasets/Full_HotelRec.zip <br /> <br />
References: https://github.com/biubiutang/LARA-1/blob/master/BootStrap.ipynb
