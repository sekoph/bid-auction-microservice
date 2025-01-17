# Auction Service

## 📌 Introduction
This is a part of microservices-based online auction platform built using FastAPI for backend services. The system is designed to handle products, bidding, user management, separately for better scalability, maintainability, and fault isolation.

## 🚀 Features
- Manages auctions, including bid placements, tracking, and winner determination.
- Stores bid history and ensures bid validation (e.g., bid must be higher than the last bid).
- Uses Kafka and web_sockects for event-driven communication for realtime bidding analysis.

## 🛠️ Prerequisites
make sure you have installed
- **python3.8+**
- **Virtual Environment**

## Other services include - Git branches
- bid-product-microservice
- bid-user-microservice
- service-registry

## 🔧 Setup & Configuration

### 1️⃣ Clone the Repository
- Create a parent directory for the microservice as online-auction

```sh
mkdir online-auction
```
- navigate to online-auction and clone this repo

```sh
cd online-auction
git clone git@github.com:sekoph/bid-auction-microservice.git
```

### 2️⃣ Add local Environment Configuration to `.env` file
- create .env file at the root of the cloned repo
- copy the contents of example.env at the root of this cloned folder, paste to created .env file
- replace the value for :
       - DATABASE_USER with your username
       - DATABASE_PASSWORD with your user password


### 3️⃣ Configure virtual environment
- At the root of this cloned folder, configure virtual environment run
```sh
python3 -m venv venv
```

-To activate virtual environment run
```sh
source venv/bin/activate
```

### 4️⃣ Install Requirements
- To install requirements run
```sh
pip install requirements.txt
```

### 5️⃣  Create a Mysql Database
- note the database should be the same as the one below
database_name: "user_microservices"


### 6️⃣ Run migration
- To configure alembic run
```sh
alembic init alembic
```

-To create migration run
```sh
alembic upgrade head
```


## 🎯 Run and Test Service
```sh
python3 index.py
```

## 🤝 Contributing
Pull requests are welcome! Feel free to fork and improve the project.

---
🚀 Happy Coding!