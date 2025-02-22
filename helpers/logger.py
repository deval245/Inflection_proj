import logging

# Logger Configuration
logging.basicConfig(
    filename="tests/logs/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
