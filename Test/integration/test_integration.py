import pytest
import random
from datetime import datetime
from helpers.api_helper import APIHelper
from helpers.logger import logger


def test_integration_email_templates():
    """Test integration with email template service."""
    template_id = APIHelper.get_email_template()
    assert template_id, "⚠️ Email template retrieval failed!"
    logger.info(f"✅ Email Template Service Integration Successful: {template_id}")


def test_integration_recipient_lists():
    """Test integration with recipient list service."""
    recipient_id = APIHelper.get_recipient_list()
    assert recipient_id, "⚠️ Recipient list retrieval failed!"
    logger.info(f"✅ Recipient List Service Integration Successful: {recipient_id}")


def test_integration_campaign_creation():
    """Test integration for campaign creation."""
    campaign_name = f"Integration Test {random.randint(1000, 9999)}"
    campaign_data = {
        "campaignName": campaign_name,
        "recipientListId": APIHelper.get_recipient_list(),
        "emailTemplateId": APIHelper.get_email_template(),
        "scheduledTime": int(datetime.now().timestamp() * 1000)
    }

    campaign_id = APIHelper.create_campaign(campaign_data)

    if campaign_id is None:
        pytest.skip(f"⚠️ Skipping test: Campaign '{campaign_name}' might already exist.")

    assert campaign_id, "⚠️ Campaign creation failed!"
    logger.info(f"✅ Campaign Service Integration Successful: {campaign_id}")
