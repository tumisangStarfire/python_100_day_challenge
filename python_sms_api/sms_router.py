import fastapi
from services.sms_service import SMSService

router = fastapi.APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World"}


@router.get("/send-sms")
async def send_message():
    phone = "+26776710242"
    message = "Test1"
    sms = SMSService()
    response = sms.publish_text_message(phone, message)
    return {"response": response }
