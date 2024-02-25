from os import getenv
from base64 import b64decode
import base64
from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    5185945994,
]

API_ID = int(getenv("API_ID", "26346822"))


API_HASH = getenv("API_HASH", "8cd2f31ad1da38dc2e37625dc7322dc3")

BOT_TOKEN = getenv("BOT_TOKEN", "6798327025:AAF6rQnjyZQN2cg0vrYc2ZfdLsUfuiqRYlk")
OWNER = int(getenv(
    "OWNER",
    b64decode("NTE4NTk0NTk5NA==").decode(
        "utf-8"
    ),
)
           )

MAX_BOT = int(getenv("MAX_BOT", "20"))

SELLER_GROUP=int(getenv("SELLER_GROUP", "-1002076523008"))

RESI = getenv(
    "RESI", "26646379b9945347b1fc403cb40bcbc6407f1f8106ba8d4b02a9b399999d100c")

LOGS = int(getenv("LOGS", "-1002123323971"))

COMMAND = getenv("COMMAND", ". - ! ?")
cmd = COMMAND.split()

blacklist_chat_encoded = "LTEwMDE2OTI3NTE4MjEgLTEwMDE0NzM1NDgyODMgLTEwMDE0NTk4MTI2NDQgLTEwMDE0MzMyMzg4MjkgLTEwMDE0NzY5MzY2OTYgLTEwMDEzMjcwMzI5NSAtMTAwMTI5NDE4MTQ5OSAtMTAwMTQxOTUxNjk4NyAtMTAwMTIwOTQzMjA3MCAtMTAwMTI5NjkzNDU4NSAtMTAwMTQ4MTM1NzU3MCAtMTAwMTQ1OTcwMTA5OSAtMTAwMTEwOTgzNzg3MCAtMTAwMTQ4NTM5MzY1MiAtMTAwMTM1NDc4Njg2MiAtMTAwMTEwOTUwMDkzNiAtMTAwMTM4NzY2Njk0NCAtMTAwMTM5MDU1MjkyNiAtMTAwMTc1MjU5Mjc1MyAtMTAwMTc3NzQyODI0NCAtMTAwMTc3MTQzODI5OCAtMTAwMTI4NzE4ODgxNyAtMTAwMTgxMjE0Mzc1MCAtMTAwMTg4Mzk2MTQ0NiAtMTAwMTc1Mzg0MDk3NSAtMTAwMTg5NjA1MTQ5MSAtMTAwMTU3ODA5MTgyNyAtMTAwMTkyNzkwNDQ1OSAtMTAwMTU3ODg1NDE1MA=="
decoded_blacklist_chat = base64.b64decode(blacklist_chat_encoded).decode("utf-8")
blacklist_chat_list = decoded_blacklist_chat.split()
blacklist_chat_integers = list(map(int, blacklist_chat_list))
BLACKLIST_CHAT = blacklist_chat_integers


MONGO_URL = getenv(
    "MONGO_URL",
    "mongodb+srv://jarbot:jarbot@cluster0.rrfszcc.mongodb.net/?retryWrites=true&w=majority",
)

SESSION = getenv(
    "SESSION",
    "BQGSBUYAV2onDRMD4zGpkz2BB0bg6x5_FeEsWv2qq66oX3pLj-Zq0u3etVmblIvfUcYzdcB1bzO_9wk38NG9ubhmzXBSafTdtq8Pt3awAQWoK6rVYAeBZQPbxSzchd7c1HuT2orCP5Fpm_USmYQOYVVVXU7dZJ9LYV5Oni4F1akStO5w4xzsy0RLBxM-STM7xGQMD-01GrE-xkuanUzZ3VvE-FGQf8IrE8t7DYs66CwaimD0O03XNQE6qMpazq245bichxKRAzFqRn0MSp2iizHKTu9G90pmhe75KPq0vcUsdcm8UmZxkSiVRz86KgRoWjdfBHqeIkSbqKBWCaD4-ZoZHrhRGwAAAAE1G0GKAA",
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