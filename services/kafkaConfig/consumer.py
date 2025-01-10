import json
import asyncio
from aiokafka import AIOKafkaConsumer
from services.connection_manager import manager

KAFKA_TOPIC = "bids"

async def consume_bids(consumer):
    """Listens for new bids and broadcasts them via WebSockets."""
    async for message in consumer:
        bid_data = message.value
        bid_message = f"User {bid_data['bidder_id']} bid {bid_data['amount']} on {bid_data['product_id']}"
        await manager.broadcast(bid_message)

async def start_kafka_consumer():
    """Starts Kafka consumer and listens for new bids."""
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="bid-consumer-group",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )
    
    # Start consumer
    await consumer.start()
    try:
        await consume_bids(consumer)
    except Exception as e:
        print(f"Error in Kafka consumer: {e}")
    finally:
        await consumer.stop()








# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# from aiokafka import AIOKafkaConsumer
# import asyncio


# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins = ["*"],
# #     allow_credentials = True,
# #     allow_methods = ["*"],
# #     allow_headers = ["*"],
# # )

# KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
# KAFKA_TOPIC = "bidding_events"

# async def consume_kafka():
#     """Kafka Consumer Generator that streams messages"""
#     consumer = AIOKafkaConsumer(
#         KAFKA_TOPIC,
#         bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
#         group_id="bidding_service",
#         auto_offset_reset="earliest"  # Start from the earliest message
#     )
#     await consumer.start()
    
#     try:
#         async for msg in consumer:
#             yield f"data: {msg.value.decode('utf-8')}\n\n"  # SSE format
#             print(f"Received message: {msg.value.decode('utf-8')}")
#             await asyncio.sleep(0.1)
#     finally:
#         await consumer.stop()

# # @app.get("/stream-bids")
# # async def stream_bids():
# #     """FastAPI Streaming Endpoint for Kafka Consumer"""
# #     return StreamingResponse(consume_kafka(), media_type="text/event-stream")

    
# # if __name__== "__main__":
# #     import uvicorn
# #     uvicorn.run("consumer:app", host="0.0.0.0", port=8007, reload=True)
