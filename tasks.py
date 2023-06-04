from event_core import settings
import requests
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_checkout_email(self, receiver_email_address, event_name):
    subject, from_email, to = "Knock Knock, Tickets from PassMaster Here!", "farmdistronigeria@gmail.com", receiver_email_address
    text_content = f"Hello {receiver_email_address}, "
    html_content = f"<p>This is your confirmation ticket mail for<strong>{event_name}</strong></p>"
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)
    return "Ticket mail sent"




def charged_ticket_price(price):
    price += price * 0.09
    return price

def remove_charge_from_earnings(earning):
    earning -= earning * 0.09
    return earning

headers= {"Authorization":f"Bearer {settings.PAYSTACK_SECRET_KEY}"}

def paystack_charge(email, amount):
    url = "https://api.paystack.co/transaction/initialize"
    data = {"email": email,
    "amount": amount,
    }
    response = requests.post(url=url, headers=headers, data=data)
    return response.json()


def verify_bank_details(account_number, bank_code):
    url =f"https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bank_code}"
    response = requests.get(url=url, headers=headers)
    return response.json()


def create_tranfer_recipient(full_name, account_number, bank_code):
    "This is to confirm and create a receiver"

    url = "https://api.paystack.co/transferrecipient"
    data = {
        "type":"nuban",
        "name":full_name,
        "account_number":account_number,
        "bank_code": bank_code,
        "currency":"NGN"
    }
    response = requests.post(url=url, headers=headers, data=data)
    return response.json()

def tranfer_earnings(amount, recipient_code, unique_reference, reason):
    """For the withdraw earning endpoint/ Send Money to Event Organiser"""
    url ="https://api.paystack.co/transfer"
    data= { "source": "balance", 
      "amount": amount,
      "reference": unique_reference, 
      "recipient": recipient_code, 
      "reason": reason 
    }
    response =requests.post(url=url, headers=headers, data=data, verify=False)
    return response.json()


def list_banks():
    url ="https://api.paystack.co/bank?country=nigeria"
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    return response.json()
        