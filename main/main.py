import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key="celj5d2ad3i9ttohjiq0celj5d2ad3i9ttohjiqg")

# Stock candles
print(finnhub_client.stock_candles('AAPL', '1', 1671777000, 1671800400))

