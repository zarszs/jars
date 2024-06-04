from os import getenv
from base64 import b64decode
import base64
from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1478997683,
]

API_ID = int(getenv("API_ID", "23423461"))


API_HASH = getenv("API_HASH", "55224304c3d8ded1c6d968398372d1af")

BOT_TOKEN = getenv("BOT_TOKEN", "7473462293:AAH3ArLiLjdo4fxTHzlINLVoovYRNhrVceM")
OWNER = int(getenv(
    "OWNER",
    b64decode("MTQ3ODk5NzY4Mw==").decode(
        "utf-8"
    ),
)
           )

MAX_BOT = int(getenv("MAX_BOT", "20"))

SELLER_GROUP=int(getenv("SELLER_GROUP", "-1002129638870"))

RESI = getenv(
    "RESI", "26646379b9945347b1fc403cb40bcbc6407f1f8106ba8d4b02a9b399999d100c")

LOGS = int(getenv("LOGS", "-1002129638870"))

COMMAND = getenv("COMMAND", ". - ! ?")
cmd = COMMAND.split()

blacklist_chat_encoded = "LTEwMDE2OTI3NTE4MjEgLTEwMDE0NzM1NDgyODMgLTEwMDE0NTk4MTI2NDQgLTEwMDE0MzMyMzg4MjkgLTEwMDE0NzY5MzY2OTYgLTEwMDEzMjcwMzI5NSAtMTAwMTI5NDE4MTQ5OSAtMTAwMTQxOTUxNjk4NyAtMTAwMTIwOTQzMjA3MCAtMTAwMTI5NjkzNDU4NSAtMTAwMTQ4MTM1NzU3MCAtMTAwMTQ1OTcwMTA5OSAtMTAwMTEwOTgzNzg3MCAtMTAwMTQ4NTM5MzY1MiAtMTAwMTM1NDc4Njg2MiAtMTAwMTEwOTUwMDkzNiAtMTAwMTM4NzY2Njk0NCAtMTAwMTM5MDU1MjkyNiAtMTAwMTc1MjU5Mjc1MyAtMTAwMTc3NzQyODI0NCAtMTAwMTc3MTQzODI5OCAtMTAwMTI4NzE4ODgxNyAtMTAwMTgxMjE0Mzc1MCAtMTAwMTg4Mzk2MTQ0NiAtMTAwMTc1Mzg0MDk3NSAtMTAwMTg5NjA1MTQ5MSAtMTAwMTU3ODA5MTgyNyAtMTAwMTkyNzkwNDQ1OSAtMTAwMTU3ODg1NDE1MA=="
decoded_blacklist_chat = base64.b64decode(blacklist_chat_encoded).decode("utf-8")
blacklist_chat_list = decoded_blacklist_chat.split()
blacklist_chat_integers = list(map(int, blacklist_chat_list))
BLACKLIST_CHAT = blacklist_chat_integers


MONGO_URL = getenv(
    "MONGO_URL",
    "mongodb+srv://jar:jar@cluster0.zsjrxpc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)

SESSION = getenv(
    "SESSION",
    "BQFlaeUAS_6oGQVhrBRSaijIknEJfbcKnWau5SsJrPDSwoIUAoDnlZ2zNIYQScZFhB5GsxiFqdPO3hTPC-1OnMNQPOT-rm9GrHb0rEZMpqXGt6Ha7aANQls7x3LGxvWK4NnEsuiG6PBbmLWtfkAx_CS6pbQbfcXrMQ3WLZL40FzwgE358HPZDl1sMz28Vaty-GlDDJF2tYJl6oU4xlTglLnw7KXNHNSLAROUssmqIv2ilHI9xle3Uq3zeUUWOxp_fB4rF4znYMj2hgn24FN7zyjrVQ_E3qpVBgAWGUUmMyNDbN5-CD4SldyNlK7t8M08RQSb4AnHt32Cn_FgONM4Std5pi9ywwAAAABYJ7azAA",
)

TEXT_PAYMENT = getenv(
    "TEXT_PAYMENT",
    """
<b>💬 SILAHKAN MELAKUKAN PEMBAYARAN SEBESAR RP25.000 = 1 BULAN</b>

<b> METODE PEMBAYARAN:</b>
   <b>┣ DANA/GOPAY/OVO VIA QRIS</b>
   <b>┗   </b> <a href=https://t.me/nDuit/14>KLIK DISINI</a>

<b>✅ KLIK TOMBOL KONFIRMASI UNTUK KIRIM BUKTI PEMBAYARAN ANDA</b>
""",
)
