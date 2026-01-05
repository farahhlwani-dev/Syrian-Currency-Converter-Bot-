📌 Syrian Currency Converter Bot
A Telegram bot built with Python using the python-telegram-bot library.
This bot helps users convert old Syrian currency to the new system after the removal of two zeros, where 100 old SYP = 1 new SYP.
It also provides real‑time USD exchange rates and live gold prices.
✨ Features
- Convert old Syrian currency to the new redenominated value.
- Display real‑time USD exchange rates.
- Show live gold prices.
- Simple and user‑friendly interface.
- Activation through following the Binary Team Instagram account.
- /start command displays bot creators and activation instructions.
👩‍💻 Created By
- Engineer Farah Hlwani
- Engineer Nadia Al‑Zaeem

🚀 How It Works
- User sends /start.
- Bot displays creators’ names and asks the user to follow the Binary Team on Instagram.
- After activation, the user can:
- Enter any old‑currency amount.
- Receive the converted value instantly.
- View live USD and gold prices.

🛠 Technologies Used
- Python
- python‑telegram‑bot
- Requests / APIs for price updates
- Environment variables for secure token handling

📂 Project Structure
main.py
handlers/
    start.py
    converting.py
    prices.py
    check_insta.py
keyboards/
    inline_keyboard.py
.gitignore

📬 Contact
For updates and more projects, follow Binary Team on Instagram.
https://www.instagram.com/binary_team_10




