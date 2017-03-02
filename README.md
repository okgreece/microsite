#OpenBudgets Microsite
This is an European Union project focused on giving EU municipalities a 
Software-as-a-Service (SaaS) solution that will allow their citizens to 
visualize, interact and discuss about Budget and Spending of their towns, cities
and countries. 

##For Administrators
###Create users for municipalities
- To create a new user for a municipality, follow these steps:
  - Go to the administration site (http://<your-url>/admin)
  - Create Profile:
    - Click "Add" on the Profile section.
    - Click the green plus sign to add a new user and actually add a one.
  - Assign permissions to the user:
    - Click the pencil to edit this new user, tick the is_superuser box. 
    - Add the following permissions:
      - Add/change/delete Dataset
      - Add/change/delete Microsite
      - Add/change/delete Theme
    - Save changes.
  - Assign the user to a municipality:  
    - Choose or create new municipality. This determines the content this user 
      has access to by filtering content in the admin site according to his/her 
      municipality.
  - Save changes.

##For Municipalities
###Workflow from zero to deployed
- First, create a Microsite and take note of the Microsite ID that is generated 
  for it. Enabling a Forum Platform here will enable discussion and 
  participation between citizens in your Microsite.
- Add as many Datasets as you want and link them to your Microsite.
- Set a layout for the microsite, which indicates how the datasets 
  are going to be drawn on screen and where should the discussion forum appear
- (optional) Add as many themes as you'd like and link them to your Microsite.
- (optional) Go to your Microsite detail page and select the theme you like the 
  most.
- Go to http://HOST_URL/vizmanager/{Microsite ID} to see your Microsite being 
  rendered

###Important
- The **code** field of a Dataset in the administration site has to be set to
  the code you get from OpenSpending when you upload the dataset there.
  <br>
  E.g., if you can see your dataset here: 
  ```
  http://next.openspending.org/viewer/23cdc48554ae8648deff7837c025d8c0:kpai2016
  ```
  Then your Dataset's code is:
  ```
  23cdc48554ae8648deff7837c025d8c0:kpai2016
  ```
  With the dataset-selection widget it should be as easy as inserting part of 
  the dataset name in the field and selecting it from the suggestions that will 
  appear in a second.

##For Developers / DevOps
###Run locally
```bash
$ sudo pip3 install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

###Run on Docker Compose
Configure environment variables inside docker-compose.yml and then run:
```bash
$ docker-compose up
```
The backend administration server should be reachable at 
http://localhost:8000/admin and the frontend for each microsite should be at
 http://localhost:8000/vizmanager/{Microsite ID}

###Important
- If you're using a remote version of OS-Viewer, your themes won't be available 
  on microsites; the idea for that functionality to work is to use a local 
  installation or a docker container of OS-Viewer. That way, you can share 
  volumes to get the os_viewer_themes folder shared between OS-Viewre and this 
  project.
- Disqus' guest comments are automatically flagged to be pre-moderated, so if 
  there are users commenting without an account, this will require a moderator 
  to approve their comments.
