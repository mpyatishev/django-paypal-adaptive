"""
IPN constants

"""

from pytz import timezone

IPN_TYPE_PAYMENT = 'Adaptive Payment PAY'
IPN_TYPE_ADJUSTMENT = 'Adjustment'
IPN_TYPE_PREAPPROVAL = 'Adaptive Payment PREAPPROVAL'

IPN_STATUS_CREATED = 'CREATED'
IPN_STATUS_COMPLETED = 'COMPLETED'
IPN_STATUS_INCOMPLETE = 'INCOMPLETE'
IPN_STATUS_ERROR = 'ERROR' 
IPN_STATUS_REVERSALERROR = 'REVERSALERROR'
IPN_STATUS_PROCESSING = 'PROCESSING'
IPN_STATUS_PENDING = 'PENDING'

IPN_ACTION_TYPE_PAY = 'PAY'
IPN_ACTION_TYPE_CREATE = 'CREATE'

IPN_TXN_STATUS_COMPLETED = 'Completed'
IPN_TXN_STATUS_PENDING = 'Pending'
IPN_TXN_STATUS_REFUNDED = 'Refunded'

IPN_TXN_SENDER_STATUS_SUCCESS = 'SUCCESS' 
IPN_TXN_SENDER_STATUS_PENDING = 'PENDING'
IPN_TXN_SENDER_STATUS_CREATED = 'CREATED' 
IPN_TXN_SENDER_STATUS_PARTIALLY_REFUNDED = 'PARTIALLY_REFUNDED' 
IPN_TXN_SENDER_STATUS_DENIED = 'DENIED' 
IPN_TXN_SENDER_STATUS_PROCESSING = 'PROCESSING' 
IPN_TXN_SENDER_STATUS_REVERSED = 'REVERSED' 
IPN_TXN_SENDER_STATUS_REFUNDED = 'REFUNDED' 
IPN_TXN_SENDER_STATUS_FAILED = 'FAILED'

IPN_FEES_PAYER_SENDER = 'SENDER'
IPN_FEES_PAYER_PRIMARYRECEIVER = 'PRIMARYRECEIVER'
IPN_FEES_PAYER_EACHRECEIVER = 'EACHRECEIVER'
IPN_FEES_PAYER_SECONDARYONLY = 'SECONDARYONLY'

IPN_REASON_CODE_CHARGEBACK = 'Chargeback' 
IPN_REASON_CODE_SETTLEMENT = 'Settlement'
IPN_REASON_CODE_ADMIN_REVERSAL = 'Admin reversal'
IPN_REASON_CODE_REFUND = 'Refund'

IPN_PAYMENT_PERIOD_NO_PERIOD_SPECIFIED = 'NO_PERIOD_SPECIFIED'
IPN_PAYMENT_PERIOD_DAILY = 'DAILY'
IPN_PAYMENT_PERIOD_WEEKLY = 'WEEKLY'
IPN_PAYMENT_PERIOD_BIWEEKLY = 'BIWEEKLY'
IPN_PAYMENT_PERIOD_SEMIMONTHLY = 'SEMIMONTHLY'
IPN_PAYMENT_PERIOD_MONTHLY = 'MONTHLY'
IPN_PAYMENT_PERIOD_ANNUALLY = 'ANNUALLY'

IPN_PIN_TYPE_NOT_REQUIRED = 'NOT_REQUIRED'
IPN_PIN_TYPE_REQUIRED = 'REQUIRED'

IPN_TIMEZONES = {'PDT': timezone('US/Pacific'),
                 'PST': timezone('US/Pacific')}