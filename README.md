## prerequisites
- make sure you have python3.8 , virtual environment installed and configured

## configure virtual environment run
python3 -m venv venv

## activate virtual environment run
source venv/bin/activate

## install requirements run
pip install requirements.txt

## database configuration
create user_microservices mysql database


## configure alembic run
alembic init alembic

## create migration run
alembic upgrade head

## run application run
python3 index.py

this is microservices that depends on other microservices in the repo
namely - bid-user-microservice
       - bid-product-microservice

