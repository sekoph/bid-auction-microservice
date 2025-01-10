from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from aiokafka import AIOKafkaProducer
import asyncio
import json


KAFKA_TOPIC = "bids"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"


async def send_to_kafka(message: dict):
    """Send bid data to Kafka"""
    producer = AIOKafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    await producer.start()
    try:
        await producer.send(KAFKA_TOPIC, message)
    finally:
        await producer.stop()
















# from fastapi import FastAPI, HTTPException
# from aiokafka import AIOKafkaProducer
# import asyncio
# import json
# import time

# # app = FastAPI()

# KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
# KAFKA_TOPIC = "bidding_events"

# # Initialize producer globally
# producer: AIOKafkaProducer = None

# async def get_kafka_producer():
#     """Ensure Kafka producer is started before sending messages"""
#     global producer
#     if producer is None:
#         producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
#         await producer.start()
#     return producer

# # @app.post("/send-bid/")
# # async def send_bid(user_id: str, bid_amount: float):
# #     """Send a bid to Kafka"""
# #     try:
# #         producer = await get_kafka_producer()
# #         message = json.dumps({"user_id": user_id, "bid_amount": bid_amount})
        
# #         for i in range(10):
# #             # message = json.dumps({f"Message {i}" :"test"})
# #             # await producer.send_and_wait(KAFKA_TOPIC, message)
# #             # await asyncio.sleep(0.1)
# #             await producer.send_and_wait(KAFKA_TOPIC, message.encode("utf-8"))
        
# #         return {"status": "success", "message": "Bid sent to Kafka"}
    
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))

# # @app.
# # async def shutdown_event():
# #     """Shutdown Kafka producer when FastAPI stops"""
# #     global producer
# #     if producer:
# #         await producer.stop()
