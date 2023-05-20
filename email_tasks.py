from django.core.mail import EmailMultiAlternatives

def send_checkout_email(receiver_email_address, event_name):
    subject, from_email, to = "Knock Knock, Tickets from PassMaster Here!", "passmaster@gmail.com", receiver_email_address
    text_content = f"Hello {receiver_email_address}, This is your confirmation ticket mail for {event_name}"
    html_content = "<p>This is an <strong>important</strong> message.</p>"
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)

