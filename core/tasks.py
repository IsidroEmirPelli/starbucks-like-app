import datetime

from cafe.celery import app

from .models import Campain
from .utils import send_campain_email
from issue_tracker.utils import create_issue


@app.task
def send_campain_mail():
    # first get all campains with date today
    campains = Campain.objects.filter(date=datetime.date.today())
    for campain in campains:
        try:
            recipients = []
            for user in campain.users:
                recipients.append(user.email)
            send_campain_email(
                campain.html_content,
                campain.subject,
                recipients,
            )
        except Exception as e:
            create_issue(
                title="Error al enviar campaña",
                description=f"Error al enviar campaña {campain.name}",
                exception=e,
            )
