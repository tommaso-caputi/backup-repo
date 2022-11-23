from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv('TOKEN')

print(ACCESS_TOKEN)
