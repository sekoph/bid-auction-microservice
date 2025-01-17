## About
Is a part of microservices-based online auction platform built using FastAPI for backend services. The system is designed to handle products, bidding, user management, separately for better scalability, maintainability, and fault isolation.

# This particular service - "auction-service"
- Manages auctions, including bid placements, tracking, and winner determination.
- Stores bid history and ensures bid validation (e.g., bid must be higher than the last bid).
- Uses Kafka and web_sockects for event-driven communication for realtime bidding analysis.

## Other services include - Git branches
- bid-product-microservice
- bid-user-microservice
- service-registry

# Usage
- Create a parent directory for the microservice as online-auction

```sh
mkdir online-auction
```
- navigate to online-auction and clone this repo

```sh
cd online-auction
git clone git@github.com:sekoph/bid-auction-microservice.git
```
- create .env file at the root of the cloned repo
- copy the contents of example.env at the root of this cloned folder, paste to created .env file
- replace the value for :
       - DATABASE_USER with your username
       - DATABASE_PASSWORD with your user password



## prerequisites
- make sure you have python3.8 , virtual environment package installed and configured

## At the root of this cloned folder, configure virtual environment run
```sh
python3 -m venv venv
```

## activate virtual environment run
```sh
source venv/bin/activate
```

## install requirements run
```sh
pip install requirements.txt
```

## create a mysql database
- note the database should be the same as the one below
database_name: "user_microservices"


## configure alembic run
```sh
alembic init alembic
```

## create migration run
```sh
alembic upgrade head
```


## run application run
```sh
python3 index.py
```

