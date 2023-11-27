import os
from google.cloud import pubsub_v1

# Set the path to your service account key file
service_account_path = 'service-account.json'

# Set your Google Cloud Platform project ID and Pub/Sub topic name
project_id = 'yamini-test-workspace'
topic_name = 'PythonTopic'

# Set the environment variable for authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path

# Create a Pub/Sub subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Create a fully qualified topic name
topic_path = subscriber.topic_path(project_id, topic_name)

# Create a subscription name (you can customize this)
subscription_name = 'PythonTopic-sub'

# Create or retrieve the subscription
subscription_path = subscriber.subscription_path(project_id, subscription_name)

try:
    # Create the subscription if it doesn't exist
    subscriber.create_subscription(subscription_path, topic_path)
except Exception as e:
    print(f"Error creating subscription: {e}")

def callback(message):
    # This function will be called when a message is received
    print(f"Received message: {message.data}")

    # Acknowledge the message to remove it from the queue
    message.ack()

# Set the callback function
subscriber.subscribe(subscription_path, callback=callback)

print(f"Listening for messages on {subscription_path}...")

# Keep the script running to continue receiving messages
try:
    # Keep the script running to continue receiving messages
    while True:
        pass
except KeyboardInterrupt:
    # Gracefully exit the script on Ctrl+C
    print("Exiting...")
finally:
    # Stop the subscriber
    subscriber.close()
