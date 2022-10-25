import boto3
import logging
from botocore.exceptions import ClientError
from models.sms import SMS
from config.aws_config import sms_client


class SMSService:
    """Encapsulates Amazon SNS topic and subscription functions."""
    def __init__(self):
        """
        : A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sms_client

    def publish_text_message(self, phone_number: str, message: str):
        """ Publishes a text message directly to a phone number without need for a
               subscription.
               :param phone_number: The phone number that receives the message. This must be
                                        in E.164 format. For example, a United States phone
                                        number might be +12065550101.
                   :param message: The message to send.
               :return: The ID of the message.
               """
        sender_id = "Ignis"
        try:
            response = self.sns_resource.publish(
                PhoneNumber=phone_number,
                Message=message,
                MessageAttributes={
                    'AWS.SNS.SMS.SenderID': {
                        'DataType': 'String',
                        'StringValue': sender_id
                    },
                    'AWS.SNS.SMS.SMSType': {
                        'DataType': 'String',
                        'StringValue': 'Promotional',
                    }
                }
            )
            message_id = response['MessageId']
            logging.info("Published message to %s.", phone_number)
        except ClientError:
            logging.exception("Couldn't publish message to %s.", phone_number)
            raise
        else:
            return response
