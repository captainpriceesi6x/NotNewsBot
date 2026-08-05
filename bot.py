import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

coins = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "the-open-network": "TON",
    "notcoin": "NOT",
    "binancecoin": "BNB",
    "solana": "SOL"
}

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": ",".join(coins.keys()),
    "vs_currencies": "usd",
    "include_24hr_change": "true"
}

data = requests.get(url, params=params).json()

text = "📊 بازار کریپتو | بروزرسانی\n\n"

for coin, symbol in coins.items():
    price = data[coin]["usd"]
    change = data[coin]["usd_24h_change"]

    emoji = "🟢" if change >= 0 else "🔴"

    text += f"{emoji} {symbol}: ${price} ({change:.2f}%)\n"

text += "\n🚀 @NotNewsPersian"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": text
    }
)
