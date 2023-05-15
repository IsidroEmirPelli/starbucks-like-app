import boto3
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
import os
from email.header import Header
from email.utils import formataddr


from issue_tracker.utils import create_issue


def send_email(
    subject,
    from_email,
    recipients,
    from_name,
    html_content,
    reply_to=None,
    cc_recipients=None,
    bcc_recipients=None,
    attachments=None,
):
    """
    Sends email using AWS SES with all same parameters as rest of send methods.
    """
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    aws_ses_region_name = os.environ.get("AWS_SES_REGION_NAME")

    client = boto3.client(
        "ses",
        region_name=aws_ses_region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    reply_list = (
        [
            reply_to,
        ]
        if reply_to
        else []
    )
    # encodes as RFC2047 using Q encoding
    # https://docs.python.org/3.5/library/email.header.html#module-email.header
    encoded_name = Header(from_name).encode()
    source = formataddr((encoded_name, from_email))
    try:
        response = client.send_email(
            Destination={
                "ToAddresses": recipients,
                "CcAddresses": cc_recipients or [],
                "BccAddresses": bcc_recipients or [],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": html_content,
                    },
                    "Text": {
                        "Charset": "UTF-8",
                        "Data": "Contenido de email no disponible aún en sólo texto, enviado como HTML.",
                    },
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": subject,
                },
            },
            ReplyToAddresses=reply_list,
            Source=source,
            # If using a configuration set, uncomment the following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    except Exception as e:
        create_issue(
            title="Error al enviar email",
            description=f"Error al enviar email a {recipients}",
            exception=e,
        )


def send_campain_email(html, subject, recipients, reply_to=None):
    from_email = os.environ.get("EMAIL_FROM_CAMPAIN")
    from_name = os.environ.get("FROM_NAME")
    html_content = render_to_string(html)
    send_email(
        subject=subject,
        from_email=from_email,
        recipients=recipients,
        from_name=from_name,
        html_content=html_content,
        reply_to=reply_to,
    )
