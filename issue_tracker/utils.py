from .models import Issue
import logging

logger = logging.getLogger(__name__)


def create_issue(title, description, exception):
    issue = Issue(title=title, description=description, exception=exception)
    issue.save()
    if exception:
        logger.error(f"Error occured: {exception}")
    logger.info(f"Created issue {issue.id}")
