from django.db import models
from ticket_app.models import Ticket
from organizations.models import Organization
from event_app.models import EventInfo
import uuid

# Create your models here.
class Checkout(models.Model):
    user = models.EmailField()
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING, related_name='checkouts')
    quantity = models.IntegerField()
    paystack_reference = models.CharField(max_length=65, blank=True)
    amount = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=8, blank=True)
    created_at =models.DateTimeField(auto_now_add= True)

    @property
    def total_price(self):
        return self.ticket.price * self.quantity

    def __str__(self):
        return f"{self.ticket.event.name}"


class ListOfBank(models.Model):
    bank_name = models.CharField(max_length = 67)
    bank_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.bank_name

BANK_CHOICES = (
    ('Access Bank', '044'),
('Access Bank (Diamond)', '063'),
('Accion Microfinance Bank', '602'),
('Ahmadu Bello University Microfinance Bank', '50036'),
('Airtel Smartcash PSB', '120004'),
('AKU Microfinance Bank', '51336'),
('ALAT by WEMA', '035A'),
('Amju Unique MFB', '50926'),
('AMPERSAND MICROFINANCE BANK', '51341'),
('Aramoko MFB', '50083'),
('ASO Savings and Loans', '401'),
('Astrapolaris MFB LTD', 'MFB50094'),
('Bainescredit MFB', '51229'),
('Banc Corp Microfinance Bank', '50117'),
('Bowen Microfinance Bank', '50931'),
('Branch International Financial Services Limited', 'FC40163'),
('Carbon', '565'),
('CASHCONNECT MFB', '865'),
('CEMCS Microfinance Bank', '50823'),
('Chanelle Microfinance Bank Limited', '50171'),
('Citibank Nigeria', '023'),
('Consumer Microfinance Bank', '50910'),
('Corestep MFB', '50204'),
('Coronation Merchant Bank', '559'),
('County Finance Limited', 'FC40128'),
('Crescent MFB', '51297'),
('Dot Microfinance Bank', '50162'),
('Ecobank Nigeria', '050'),
('Ekimogun MFB', '50263'),
('Ekondo Microfinance Bank', '098'),
('Eyowo', '50126'),
('Fairmoney Microfinance Bank', '51318'),
('Fidelity Bank', '070'),
('Firmus MFB', '51314'),
('First Bank of Nigeria', '011'),
('First City Monument Bank', '214'),
('FirstTrust Mortgage Bank Nigeria', '107'),
('FLOURISH MFB', '50315'),
('FSDH Merchant Bank Limited', '501'),
('Gateway Mortgage Bank LTD', '812'),
('Globus Bank', '00103'),
('GoMoney', '100022'),
('Goodnews Microfinance Bank', '50739'),
('Greenwich Merchant Bank', '562'),
('Guaranty Trust Bank', '058'),
('Hackman Microfinance Bank', '51251'),
('Hasal Microfinance Bank', '50383'),
('Heritage Bank', '030'),
('HopePSB', '120002'),
('Ibile Microfinance Bank', '51244'),
('Ikoyi Osun MFB', '50439'),
('Infinity MFB', '50457'),
('Jaiz Bank', '301'),
('Kadpoly MFB', '50502'),
('Keystone Bank', '082'),
('Kredi Money MFB LTD', '50200'),
('Kuda Bank', '50211'),
('Links MFB', '50549'),
('Living Trust Mortgage Bank', '031'),
('Lotus Bank', '303'),
('Mayfair MFB', '50563'),
('Mint MFB', '50304'),
('Moniepoint MFB', '50515'),
('MTN Momo PSB', '120003'),
('Optimus Bank Limited', '00107'),
('Paga', '100002'),
('PalmPay', '999991'),
('Parallex Bank', '104'),
('Parkway - ReadyCash', '311'),
('Paycom', '999992'),
('Peace Microfinance Bank', '50743'),
('Personal Trust MFB', '51146'),
('Petra Mircofinance Bank Plc', '50746'),
('Polaris Bank', '076'),
('Polyunwana MFB', '50864'),
('PremiumTrust Bank', '105'),
('Providus Bank', '101'),
('QuickFund MFB', '51293'),
('Rand Merchant Bank', '502'),
('Refuge Mortgage Bank', '90067'),
('ROCKSHIELD MICROFINANCE BANK', '50767'),
('Rubies MFB', '125'),
('Safe Haven MFB', '51113'),
('Safe Haven Microfinance Bank Limited', '951113'),
('Shield MFB', '50582'),
('Solid Allianze MFB', '51062'),
('Solid Rock MFB', '50800'),
('Sparkle Microfinance Bank', '51310'),
('Stanbic IBTC Bank', '221'),
('Standard Chartered Bank', '068'),
('Stellas MFB', '51253'),
('Sterling Bank', '232'),
('Suntrust Bank', '100'),
('Supreme MFB', '50968'),
('TAJ Bank', '302'),
('Tanadi Microfinance Bank', '090560'),
('Tangerine Money', '51269'),
('TCF MFB', '51211'),
('Titan Bank', '102'),
('Titan Paystack', '100039'),
('U&C Microfinance Bank Ltd (U AND C MFB)', '50840'),
('Uhuru MFB', 'MFB51322'),
('Unaab Microfinance Bank Limited', '50870'),
('Unical MFB', '50871'),
('Unilag Microfinance Bank', '51316'),
('Union Bank of Nigeria', '032'),
('United Bank For Africa', '033'),
('Unity Bank', '215'),
('VFD Microfinance Bank Limited', '566'),
('Wema Bank', '035'),
('Zenith Bank', '057'),
)

class BankDetail(models.Model):
    account_number = models.IntegerField()
    bank_name = models.CharField(max_length= 20, blank=True)
    bank_code = models.CharField(choices=BANK_CHOICES,max_length=67)
    account_name = models.CharField(max_length= 50, blank=True)
    recipient_code = models.CharField(max_length= 45, blank=True)
    owner = models.OneToOneField(Organization, on_delete=models.CASCADE, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.bank_name} {self.account_number} - {self.owner.name}"

class WithdrawEventEarning(models.Model):
    event = models.OneToOneField(EventInfo, on_delete=models.CASCADE)
    bank_detail = models.ForeignKey(BankDetail, on_delete=models.DO_NOTHING)
    reference_code = models.UUIDField(uuid.uuid4, max_length = 45, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="Pending", max_length=24)
    
    def __str__(self):
        return f"{self.event.name}, {self.reference_code}"