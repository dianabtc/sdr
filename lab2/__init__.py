from recombee_api_client.api_client import RecombeeClient
from config import RECOMBEE_DB_ID, RECOMBEE_PRIVATE_TOKEN, RECOMBEE_REGION

client = RecombeeClient(
    RECOMBEE_DB_ID,
    RECOMBEE_PRIVATE_TOKEN,
    region=RECOMBEE_REGION
)