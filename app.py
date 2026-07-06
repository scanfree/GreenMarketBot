from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import TOKEN, BOT_NAME
from signal_engine import analyze_market

# -------------------------
# START COMMAND
# -------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"""🟢 Welcome to {BOT_NAME}

AI Smart Money Concepts Trading Bot

Available Commands:

/help
/status
/analyze XAUUSD

More features are coming soon...
"""
    )

# -------------------------
# HELP COMMAND
# -------------------------
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
📚 Green Market Commands

/start - Start the bot
/help - Show commands
/status - Check bot status
/analyze XAUUSD - Analyze Gold
"""
    )

# -------------------------
# STATUS COMMAND
# -------------------------
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🟢 Green Market

Status: ONLINE
Version: 1.0

Everything is working correctly.
"""
    )

# -------------------------
# ANALYZE COMMAND
# -------------------------
async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text("Usage:\n/analyze XAUUSD")
        return

    symbol = context.args[0]
    result = analyze_market(symbol)

    text = f"""
📊 Market Analysis

Symbol: {symbol.upper()}

Trend: {result['trend']}
BOS: {result['bos']}
CHOCH: {result['choch']}
FVG: {result['fvg']}
Liquidity: {result['liquidity']}

Entry: {result['entry']}
Stop Loss: {result['sl']}
Take Profit: {result['tp']}

Confidence: {result['confidence']}
"""

    await update.message.reply_text(text)

# -------------------------
# MAIN
# -------------------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("analyze", analyze))

    print("🟢 Green Market Bot Started...")

    app.run_polling()

if __name__ == "__main__":
    main()