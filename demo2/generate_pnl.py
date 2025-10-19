import csv
import datetime
import random

# --- Configuration ---
OUTPUT_FILE = "pnl_over_time.csv"
START_DATE = datetime.date(2024, 1, 1)
NUM_DAYS = 500  # Number of trading days to simulate
INITIAL_CAPITAL = 100000.0

# --- Simulation Parameters ---
# Represents the average daily return (positive drift)
DAILY_DRIFT = 0.001  # 0.1% average daily gain
# Represents the daily volatility
DAILY_VOLATILITY = 0.02  # 2% standard deviation

def generate_pnl_data():
    """Generates a CSV file with simulated daily PnL data."""
    print(f"Generating simulated PnL data into '{OUTPUT_FILE}'...")
    
    current_date = START_DATE
    cumulative_pnl = INITIAL_CAPITAL
    
    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(['Date', 'CumulativePnL'])
        
        # Write the initial state
        writer.writerow([current_date.strftime('%Y-%m-%d'), f"{cumulative_pnl:.2f}"])
        
        for _ in range(NUM_DAYS):
            # Move to the next day
            current_date += datetime.timedelta(days=1)
            
            # Simulate a daily return using a normal distribution
            # This creates a more realistic "random walk"
            daily_return = random.gauss(DAILY_DRIFT, DAILY_VOLATILITY)
            
            # Update the PnL
            cumulative_pnl *= (1 + daily_return)
            
            # Write the new data point to the file
            writer.writerow([current_date.strftime('%Y-%m-%d'), f"{cumulative_pnl:.2f}"])
            
    print("Done.")

if __name__ == "__main__":
    generate_pnl_data()