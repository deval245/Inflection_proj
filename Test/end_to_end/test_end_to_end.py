import pytest
import requests
from datetime import datetime
from faker import Faker

from helpers.api_helper import APIHelper
from config.settings import BASE_URL_CAMPAIGN, HEADERS, TIMEOUT
from helpers.logger import logger

faker = Faker()


@pytest.fixture(scope="module")
def create_campaign():
    """Create a campaign for end-to-end testing."""
    campaign_data = {
        "campaignName": faker.catch_phrase(),
        "recipientListId": APIHelper.get_recipient_list(),
        "emailTemplateId": APIHelper.get_email_template(),
        "scheduledTime": int(datetime.now().timestamp() * 1000)
    }

    campaign_id = APIHelper.create_campaign(campaign_data)

    if not campaign_id:
        pytest.fail(f"⚠️ Campaign creation failed for: {campaign_data['campaignName']}")

    return campaign_id


def test_end_to_end_campaign_creation(create_campaign):
    """Verify campaign creation end-to-end."""
    assert create_campaign, "⚠️ Campaign creation failed!"
    logger.info(f"✅ End-to-end campaign creation verified: {create_campaign}")


def test_end_to_end_campaign_retrieval(create_campaign):
    """Retrieve campaign details."""
    campaign_id = create_campaign
    url = f"{BASE_URL_CAMPAIGN}/campaigns/{campaign_id}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        response_json = response.json()

        assert response_json.get('data', {}).get('id') == campaign_id, "⚠️ Campaign ID mismatch"
        logger.info(f"✅ End-to-end campaign retrieval successful for: {campaign_id}")

    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Error retrieving campaign {campaign_id}: {e}")
        pytest.fail(f"Error retrieving campaign {campaign_id}: {e}")
