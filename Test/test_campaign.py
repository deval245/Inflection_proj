import requests
import pytest
import random
import traceback
import logging
from datetime import datetime
from faker import Faker

faker = Faker()

# Logging Configuration
logging.basicConfig(
    filename="campaign_test.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# Define API Endpoints
BASE_URL_TEMPLATE = "http://localhost:7071"
BASE_URL_RECIPIENT = "http://localhost:7072"
BASE_URL_CAMPAIGN = "http://localhost:7070"


# Helper Functions
def get_template_id():
    """Random email & template generation.."""
    try:
        url = f"{BASE_URL_TEMPLATE}/email/templates"
        response = requests.get(url, headers={'accept': '*/*'})
        response.raise_for_status()
        response_data = response.json()
        template_id = random.choice(response_data['data'])['id']

        logger.info(f"✅ Template ID retrieved: {template_id}")
        return template_id
    except Exception as e:
        logger.error(f"❌ Failed to fetch email templates: {e}")
        pytest.fail(f"Failed to fetch email templates: {e}")


def get_recipient_list_id():
    """Random recipient list ID"""
    try:
        url = f"{BASE_URL_RECIPIENT}/recipients/lists"
        response = requests.get(url, headers={'accept': '*/*'})
        response.raise_for_status()
        response_data = response.json()
        recipient_id = random.choice(response_data['data'])['id']

        logger.info(f"✅ Recipient List ID retrieved: {recipient_id}")
        return recipient_id
    except Exception as e:
        logger.error(f"❌ Failed to fetch recipient lists: {e}")
        pytest.fail(f"Failed to fetch recipient lists: {e}")


@pytest.fixture(scope="module")
def create_campaign():
    """New campaign and return ID."""
    try:
        recipient_list_id = get_recipient_list_id()
        template_id = get_template_id()
        campaign_name = faker.catch_phrase()
        scheduled_time = int(datetime.now().timestamp() * 1000)

        url = f"{BASE_URL_CAMPAIGN}/campaigns"
        campaign_data = {
            "campaignName": campaign_name,
            "recipientListId": recipient_list_id,
            "emailTemplateId": template_id,
            "scheduledTime": scheduled_time
        }

        response = requests.post(url, json=campaign_data)
        response.raise_for_status()
        response_json = response.json()

        campaign_id = response_json.get('data', {}).get('id')

        if not campaign_id:
            logger.error("❌ camp.no response !")
            pytest.fail("camp.no response !")

        logger.info(f"✅ camp.. created.. successfully : {campaign_id}")
        print("\n camp.. created.. successfully :", response_json)
        return campaign_id

    except Exception as e:
        logger.error(f"❌ Error creating campaign: {traceback.format_exc()}")
        pytest.fail(f"Error creating campaign: {traceback.format_exc()}")


# Test Cases
def test_retrieve_campaign(create_campaign):
    """Getting details of the campaign.. (retrieval.)"""
    try:
        campaign_id = create_campaign
        url = f"{BASE_URL_CAMPAIGN}/campaigns/{campaign_id}"
        response = requests.get(url)
        response.raise_for_status()

        response_json = response.json()
        campaign_data = response_json.get('data', {})

        assert campaign_data.get('id') == campaign_id, "Campaign ID mismatch"
        logger.info(f"✅ camp.. retrived.. awesome.!: {campaign_id}")
        print("\n camp.. retrived.. awesome.!:", response_json)

    except Exception as e:
        logger.error(f"❌ Error retrieving campaign: {traceback.format_exc()}")
        pytest.fail(f"Error retrieving campaign: {traceback.format_exc()}")


def test_update_campaign(create_campaign):
    """Updation of campaign & verifying it...."""
    try:
        campaign_id = create_campaign
        updated_name = faker.bs().capitalize()

        url = f"{BASE_URL_CAMPAIGN}/campaigns/{campaign_id}/name"
        response = requests.patch(url, json={"campaignName": updated_name})
        response.raise_for_status()

        response_json = response.json()
        assert response_json.get('data', {}).get('campaignName') == updated_name, "Campaign name not updated"
        logger.info(f"✅ camp.. updated.. awesome!: {campaign_id}")
        print("\n camp.. updated.. awesome!:", response_json)

    except Exception as e:
        logger.error(f"❌ Error updating campaign: {traceback.format_exc()}")
        pytest.fail(f"Error updating campaign: {traceback.format_exc()}")


if __name__ == "__main__":
    pytest.main(["--html=test_report.html", "--self-contained-html"])
