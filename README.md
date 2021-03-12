# e-kazi-online
## Author

Albert Kizito
Jean Bede
Zephania Ngenoh
Derrick Muriithi

# Description
This  is a web application that on is able to look for their desired jobs from all the country despite there location 


## User Story

* log in to the website
* search for the desired jobs based on the profile

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|

## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
https://github.com/Kizito-Alberrt/e-kazi-online.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd e-kazi-online
### create virtual environment and install pip
  $ python3 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python

  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* Python3
* Flask



## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug



