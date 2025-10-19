import datetime
import random

OUTPUT_FILE = "trader.log"
TOTAL_LINES = 10000000

CLUB_TICKERS = ["ACM", "IEEE", "CSES", "HKN", "WIC"]

INFO_MESSAGES = [
    "Placed order for 100 shares of ACM",
    "Placed order for 50 shares of IEEE",
    "Market data feed for ACM is active",
    "Received trade confirmation: ID 775b10a3",
    "System health check OK",
    "User authentication successful",
    "Cancelled order for 200 shares of CSES",
]

WARN_MESSAGES = [
    "High latency detected on market data feed",
    "API response time exceeds 50ms threshold",
    "Disk space is nearing 85% capacity",
]

ERROR_MESSAGES = [
    # High Frequency (Core Logic/Risk)
    "Risk check failed: Position limit exceeded",
    "Risk check failed: Position limit exceeded",
    "Risk check failed: Position limit exceeded",
    "Risk check failed: Position limit exceeded",
    "Invalid symbol format",
    "Invalid symbol format",
    
    # Medium Frequency (Connectivity/API)
    "Connection to exchange timed out",
    "Connection to exchange timed out",
    "APIError: Invalid message type",
    "APIError: Sequence number mismatch",

    # Low Frequency (More specific issues)
    "Order price out of band",
    "Insufficient funds",
    "Database connection lost",
    "Compliance check failed: Fat finger protection",
]

# Templates for errors that will include a specific ticker
TICKER_ERROR_TEMPLATES = [
    "Order rejected by exchange: Unknown symbol {ticker}",
    "Compliance check failed: {ticker} is on the restricted list",
    "Market data for {ticker} is currently halted",
    "Trade bust: No liquidity for {ticker}",
]

def main():
    print(f"Generating {TOTAL_LINES} log entries into '{OUTPUT_FILE}'...")
    
    current_time = datetime.datetime.now(datetime.timezone.utc)
    
    with open(OUTPUT_FILE, "w") as f:
        for _ in range(TOTAL_LINES):
            current_time += datetime.timedelta(seconds=random.randint(0, 3))
            timestamp = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')

            log_type = random.choices(
                population=["INFO", "WARN", "ERROR"],
                weights=[0.80, 0.15, 0.05],
                k=1
            )[0]
            
            if log_type == "INFO":
                message = random.choice(INFO_MESSAGES)
            elif log_type == "WARN":
                message = random.choice(WARN_MESSAGES)
            else: # ERROR
                # 70% chance of a generic error, 30% chance of a ticker-specific error
                if random.random() < 0.6:
                    message = random.choice(ERROR_MESSAGES)
                else:
                    template = random.choice(TICKER_ERROR_TEMPLATES)
                    ticker = random.choice(CLUB_TICKERS)
                    message = template.format(ticker=ticker)

            f.write(f"{timestamp} [{log_type}] \"{message}\"\n")
            
    print(f"Done. Log file '{OUTPUT_FILE}' has been created.")

if __name__ == "__main__":
    main()