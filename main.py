#importing our libraries 
import slack #for working with Slack API
import os  #for accessing environment variables 
from pathlib import Path 
from dotenv import load_dotenv



# Set the path to the .env file using pathlib
env_path =Path('.')/'.env' 

# Load environment variables from the .env file
load_dotenv(dotenv_path=env_path)



# Create a Slack WebClient object for API interaction
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#bek_testbot', text="Hello world!") #posting a message to the channel 
