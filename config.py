import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21145186")

API_HASH = os.environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7681830527:AAHIy7NeWz06sK6EeBLPxogBCLR1AGFvX0c") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002123546604") 

DB_NAME = os.environ.get("DB_NAME","maamthree")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://infohubstore06:RUQbKf1YWc42rOIf@maamthree.csbu5.mongodb.net/?retryWrites=true&w=majority&appName=maamthree")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/kXJ.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6011680723 5178714818').split()]

PORT = os.environ.get("PORT", "8080")
