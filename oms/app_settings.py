# We can add more statuses as in when required
ORDER_STATUS = (
    ('CRT', 'Created'),
    ('IP', 'In Progress'),
    ('PP', 'Payment Pending'),
    ('CMP', 'Completed'),
    ('DL', 'Delivered'),
    ('CAN', 'Cancelled'),
)
DEFAULT_ORDER_STATUS = 'CRT'

PAYMENT_MODE = (
    ('COD', 'Cash On Delivery'),
    ('CC', 'Credit Card'),
    ('DC', 'Debit Card'),
    ('NB', 'NetBanking'),
)
DEFAULT_PAYMENT_MODE = 'COD'

CURRENCIES = (
    ('INR', 'Indian Rupee'),
    ('USD', 'US Dollar'),
)

DEFAULT_CURRENCY = 'INR'