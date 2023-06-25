# Scripts to trigger messages in WhatsApp:

# For getting the access_token and phone_number_id you have to follow steps 1–7 given below and run the script below to see the magic.

from heyoo import WhatsApp

messenger = WhatsApp('EAALHfLeY0LoBAPtf7ZCiKM1cUPeD4jeAZBKXsJ8TZCGU8KAa58m9eDfmTQaMDg07iqgKuWrR3eoxyOCu12ZBTPb2kIIhZC3vn5NuBakctDSRfome20K4ZCGpERwC840J85rH0zGiLG3zuTTNNkYdenf9dZCWXFMKs0kO85DqAyyUcPdZAKMFCzeP3atF5Hz137Nxk1mmD1pWDQZDZD',phone_number_id='101700846313526')

# For sending a Text messages
messenger.send_message('Hello', '6285173200421')

# For sending an Image
messenger.send_image(
        image="https://pict.sindonews.net/dyn/850/pena/news/2022/01/13/39/655579/harga-fotofoto-ghozali-bikin-melongo-ada-yang-laku-rp42-miliiar-fwx.jpg",
        recipient_id="6285173200421",
    )