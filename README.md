# Pirotech

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c15fd8acb6344cccbdf9988a899ad086)](https://www.codacy.com/manual/leonardoalonsososa/Pirotech?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leonardoAlonso/Pirotech&amp;utm_campaign=Badge_Grade)

Api rest to sell fireworks in a mobile app

## Install

Clone this project and create a virtual env based on python 3.6

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requeriments.txt
```

In Linux distros based on Devian run:

```bash
sudo apt-get install python3-dev build-essential
sudo apt-get install libpq-dev
sudo pip install psycopg2
```

Create a postgresql database named `pirotech` and `pirotech-test` to run de unnittest
using pirotechuser as user

## Run project

Set envirnment var

```bash
export APPLICATION_ENV='DEVELOPMENT_CONFIG'
```

use next values to set environment app

```bash
DEVELOPMENT_CONFIG
TESTING_CONFIG
```

To run this project exceute this comands into the terminal

```bash
flask db init
flask db migrate
flask db upgrade
flask run
```
