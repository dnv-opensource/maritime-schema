import logging

from maritime_schema.types import caga

__ALL__ = ["publish_schema"]

logger = logging.getLogger(__name__)


def publish_schema():
    """Publish the maritime schema."""

    logger.info("Start publishing schema")

    caga.publish_schema()

    logger.info("Successfully published schema")

    return
