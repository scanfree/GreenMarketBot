def analyze_market(symbol):

    symbol = symbol.upper()

    if symbol == "XAUUSD":
        return {
            "trend": "Bullish 📈",
            "bos": "Confirmed ✅",
            "choch": "None",
            "fvg": "Detected 🟩",
            "liquidity": "Above Highs",
            "entry": "3362.50",
            "sl": "3355.20",
            "tp": "3378.80",
            "confidence": "89%"
        }

    return {
        "trend": "Unknown",
        "bos": "None",
        "choch": "None",
        "fvg": "None",
        "liquidity": "None",
        "entry": "-",
        "sl": "-",
        "tp": "-",
        "confidence": "0%"
    }