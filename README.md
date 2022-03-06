# SaltySocials

## A web app for grouping user social media feeds based on shared dislikes for specified topics

## Instructions to deploy

0. You will need to have virtualenv and python. 
  `pip install virtualenv`. 
  `pip install python3`. 

1. Create a directory in location of choice to launch app from. 

  &nbsp;`mkdir myApp`. 
  
2. Change into the directory and create a virtual environment, then activate. 

  &nbsp;`cd myApp`. 
  &nbsp;`virtualenv venv`. 
  
  &nbsp;on Mac:      
  &nbsp;`source bin/activate`. 
  
  &nbsp;on Windows:  
  &nbsp;`<pathtofolder>\Scripts\activate`. 
  
3. Clone the repo into your virtual environment, and install requirements. 
  &nbsp;`git clone https://github.com/lamolivia/SaltySocials/`. 
  &nbsp;`cd venv`. 
  &nbsp;`pip install -r requirements.txt`. 
  
4. Move into app directory (where your manage.py file is) and run the following command:  
  &nbsp;`python3 manage.py runserver`. 
  
&nbsp;All done!  
