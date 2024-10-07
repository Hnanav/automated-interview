"""
Created by Alejandro Cuevas
(t-alejandroc@microsoft.com / acuevasv@andrew.cmu.edu)
August 2023
"""

import asyncio
import os
import logging
import google.generativeai as genai  # Correct import for the SDK

from models import AIModel
import prompts
import utils
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = utils.setup_logger(__name__)

## LOAD API CREDENTIALS START ##
GEMINI_API_KEY = utils.get_api_credentials()  # Assume this returns a single value

logger.info("GEMINI_API_KEY found.")
assert GEMINI_API_KEY is not None, "No Gemini API key found. Please set the GEMINI_API_KEY environment variable."

# Configure the Gemini API client with the API key
genai.configure(api_key=GEMINI_API_KEY)

MAX_API_TIMEOUT = 60

# Create new skills
prober_depersonalized_skill = prompts.PROBER_PROMPT_DEPERSONALIZED_FEWSHOT
active_listener_global_skill = prompts.ACTIVE_LISTENER_GLOBAL

# Create AIModel instances for each skill
prober_depersonalized = AIModel("prober_depersonalized", genai, prober_depersonalized_skill)
global_active_listener = AIModel("global_active_listener", genai, active_listener_global_skill)

# Set up initial context
prober_depersonalized.context["history"] = ""
global_active_listener.context["history"] = ""

try:
    logger.info("LLM modules started...")
except Exception as e:
    logger.error("Error: %s", e)


def get_new_global_vars():
    """Retrieve global API configuration variables."""
    try:
        api_retry_delay = int(os.environ.get("API_RETRY_DELAY", 5))
        api_retries = int(os.environ.get("API_RETRIES", 6))
        api_retry_func = os.environ.get("API_RETRY_FUNC", "expo")
    except Exception as e:
        logger.error("Error retrieving global variables: %s", e)
        api_retry_delay = 5
        api_retries = 6
        api_retry_func = "expo"
    return api_retry_delay, api_retries, api_retry_func


async def get_module_response(module_name, no_api_calls=False):
    """Get response from the specified module."""
    logger.warning(f"Attempting API call for module: '{module_name}'")
    if no_api_calls:
        return f"We invoked {module_name}"
    
    response = None
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')  # Specify your model here
        if module_name == "prober_depersonalized":
            # response = await asyncio.wait_for(
            #     model.generate_content(prober_depersonalized_skill),
            #     timeout=MAX_API_TIMEOUT,
            # )
            response = model.generate_content(prober_depersonalized_skill)
        elif module_name == "global_active_listener":
            # response = await asyncio.wait_for(
            #     model.generate_content(active_listener_global_skill),
            #     timeout=MAX_API_TIMEOUT,
            # )
            response = model.generate_content(active_listener_global_skill)
        
        logger.info("Module name: %s | Response: %s", module_name, response)
        
        return response.text if response else "No response returned."
    
    except Exception as e:
        logger.error("Error in get_module_response: %s", e)
        return "Faced an error in get_module_response()"


if __name__ == "__main__":
    print(get_new_global_vars()[2])
