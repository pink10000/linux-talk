import collections

INPUT_FILE = "trader.log"

def parse_trader_log():
    print(f"Parsing '{INPUT_FILE}' with Python...")
    
    error_messages = []
    try:
        with open(INPUT_FILE, 'r') as f:
            for line in f:
                if 'ERROR' in line:
                    try:
                        message = line.split('"')[1]
                        error_messages.append(message)
                    except IndexError:
                        continue
    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        return

    message_counts = collections.Counter(error_messages)

    sorted_counts = message_counts.most_common()

    print("\n--- Top Errors ---")
    for message, count in sorted_counts:
        print(f"{count:>7} {message}")

if __name__ == "__main__":
    parse_trader_log()