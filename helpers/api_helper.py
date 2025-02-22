import requests
import random
import traceback
import pytest
from config.settings import BASE_URL_TEMPLATE, BASE_URL_RECIPIENT, BASE_URL_CAMPAIGN, HEADERS, TIMEOUT
from helpers.logger import logger


class APIHelper:
    """Helper class for API interactions"""

    @staticmethod
    def get_email_template():
        """Fetch a random email template"""
        try:
            url = f"{BASE_URL_TEMPLATE}/email/templates"
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            response_data = response.json()
            return random.choice(response_data['data'])['id']
        except Exception as e:
            logger.error(f"❌ Failed to fetch email templates: {traceback.format_exc()}")
            pytest.fail(f"Failed to fetch email templates: {e}")

    @staticmethod
    def get_recipient_list():
        """Fetch a random recipient list"""
        try:
            url = f"{BASE_URL_RECIPIENT}/recipients/lists"
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            response_data = response.json()
            return random.choice(response_data['data'])['id']
        except Exception as e:
            logger.error(f"❌ Failed to fetch recipient lists: {traceback.format_exc()}")
            pytest.fail(f"Failed to fetch recipient lists: {e}")

    @staticmethod
    def create_campaign(campaign_data):
        """Create a new campaign and return its ID, handling conflicts."""
        try:
            url = f"{BASE_URL_CAMPAIGN}/campaigns"
            response = requests.post(url, json=campaign_data, headers=HEADERS, timeout=TIMEOUT)

            if response.status_code == 409:
                logger.warning(f"⚠️ Campaign already exists: {campaign_data['campaignName']}")
                return None  # Return None to indicate a conflict

            response.raise_for_status()
            response_json = response.json()

            campaign_id = response_json.get('data', {}).get('id')
            if not campaign_id:
                pytest.fail("⚠️ Campaign ID not returned in response!")

            logger.info(f"\n✅ Campaign created successfully: {response_json}")
            return campaign_id

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error creating campaign: {traceback.format_exc()}")
            pytest.fail(f"Error creating campaign: {traceback.format_exc()}")
