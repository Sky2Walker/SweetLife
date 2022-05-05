from SweetShop.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task()
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Замовлення №. {}'.format(order_id)
    message = 'Слава Україні {},\n\n Ваше замовлення успішно створене.\
                Номер замовлення - {}.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@sweetshop.com',
                          [order.email])
    return mail_sent