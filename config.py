from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY= os.environ['SECRET_KEY']
MONGO_ROUTE= os.environ['MONGO_ROUTE']