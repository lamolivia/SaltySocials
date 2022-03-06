# SaltySocials

## A web app for grouping user social media feeds based on shared dislikes for specified topics

## Instructions to deploy

0. You will need to have virtualenv and python. 
  `pip install virtualenv`. 
  `pip install python3`. 

1. Create a directory in location of choice to launch app from. 

  :`mkdir myApp`. 
  
2. Change into the directory and create a virtual environment, then activate. 

  :`cd myApp`. 
  :`virtualenv venv`. 
  
  :on Mac:      
  :`source bin/activate`. 
  
  :on Windows:  
  :`<pathtofolder>\Scripts\activate`. 
  
3. Clone the repo into your virtual environment, and install requirements. 
  :`git clone https://github.com/lamolivia/SaltySocials/`. 
  :`cd venv`. 
  :`pip install -r requirements.txt`. 
  
4. Move into app directory (where your manage.py file is) and run the following command:  
  :`python3 manage.py runserver`. 
  
:All done!  
