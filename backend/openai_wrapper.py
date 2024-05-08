import json
import openai
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_PARSE = """
This is a conversation between “farmer” and “Lithos”. Your job is to extract information from the transcript to record pertinent information in a structured format.

__A__: Extract the information in the following format:
{
  'fields': []{
  'name': `type: str, description: name of field` ,
  'ph_level': `type: float, description: average ph level, pick exactly one number.`,
  'crop': `type: str, description: crop planted on field`,
  'limed': `type: bool, description: has field been limed`,
  'fertilizer': `type: str, description: fertilizer used on field`,
  'tilling': `type: str, description: field tilling technique`,
  'spreader': `type: bool, description: does farmer have a spreader`,
  'spreader_tons': `type: str, description: capacity of spreader`
  },
'timeline': int,
'follow_up': str
}

Note: fill up timeline in number of days and follow-up is a choice between mobile and email.
For any information not present in transcript, return N.A

Transcript:
"""