# Pirotech

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c15fd8acb6344cccbdf9988a899ad086)](https://www.codacy.com/manual/leonardoalonsososa/Pirotech?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leonardoAlonso/Pirotech&amp;utm_campaign=Badge_Grade)

Api rest to sell fireworks in a mobile app

## Install 
Clone this project and create a virtual env based on python 3.6
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requeriments.txt
```
Create a mysqll database named `pirotech` and `pirotech-test` to run de unnittest

## Run project
To run this project exceute this comands into the terminal
```
flask db init
flask db migrate
flask db upgrade
flask run
```
