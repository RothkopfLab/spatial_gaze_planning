----------------------
- Code
----------------------

spatialPlanningCode.py  
reads in the preprocessed data and the stimulus shapes, computes mean landing locations and generates the behavioral plot shown in the paper. 


----------------------
- Data 
----------------------

spatialPlanningData.csv  
contains the data of individual subjects after preprocessing. This data is used to estimate the parameters of our computational model.  

Description of the dataframe:

Unnamed: 0 :  row number
code:         participant code
seed:         stimulus code
cols:         classification of fixation (0: first fixation in the short search interval, 1: first fixation in the long interval, 2: second location in the long interval)
posX:         x-coordinate of the fixation
posY:         y-coordinate of the fixation

----------------------
- Experimental Stimuli 
----------------------
spatialPlanningShape-13.gz  
spatialPlanningShape-19.gz  
spatialPlanningShape-26.gz  
spatialPlanningShape-4.gz

Each file contains the shape used for our visual search task. Shape numbers correspond to the column seed in the data file.
