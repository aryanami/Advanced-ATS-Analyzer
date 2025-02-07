import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def start_fine_tuning(file_id, model="gpt-3.5-turbo"):
    try:
        response = openai.FineTuningJob.create(
            training_file=file_id,
            model=model
        )
        return response
    except Exception as e:
        print(f"Error starting fine-tuning: {e}")
        return None 